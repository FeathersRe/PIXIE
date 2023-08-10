import torch
from safetensors.torch import load_file
from diffusers import DPMSolverMultistepScheduler
from diffusers import StableDiffusionPipeline

def generation(SD_path, Lora_path, prompt, output_path, height, width):
    
    #Loading the SD model
    pipeline = StableDiffusionPipeline.from_pretrained(SD_path,torch_dtype=torch.float32)
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)

    #Loading the Lora model
    state_dict = load_file(Lora_path)

    '''
    Fusing Lora model on top of SD base model
    Credits to Haofan Wang, Qixun Wang: https://github.com/haofanwang/Lora-for-Diffusers
    '''

    LORA_PREFIX_UNET = 'lora_unet'
    LORA_PREFIX_TEXT_ENCODER = 'lora_te'

    alpha = 1.0

    visited = []

    # directly update weight in diffusers model
    for key in state_dict:
        
        # it is suggested to print out the key, it usually will be something like below
        # "lora_te_text_model_encoder_layers_0_self_attn_k_proj.lora_down.weight"
        
        # as we have set the alpha beforehand, so just skip
        if '.alpha' in key or key in visited:
            continue
            
        if 'text' in key:
            layer_infos = key.split('.')[0].split(LORA_PREFIX_TEXT_ENCODER+'_')[-1].split('_')
            curr_layer = pipeline.text_encoder
        else:
            layer_infos = key.split('.')[0].split(LORA_PREFIX_UNET+'_')[-1].split('_')
            curr_layer = pipeline.unet

        # find the target layer
        temp_name = layer_infos.pop(0)
        while len(layer_infos) > -1:
            try:
                curr_layer = curr_layer.__getattr__(temp_name)
                if len(layer_infos) > 0:
                    temp_name = layer_infos.pop(0)
                elif len(layer_infos) == 0:
                    break
            except Exception:
                if len(temp_name) > 0:
                    temp_name += '_'+layer_infos.pop(0)
                else:
                    temp_name = layer_infos.pop(0)
        
        # org_forward(x) + lora_up(lora_down(x)) * multiplier
        pair_keys = []
        if 'lora_down' in key:
            pair_keys.append(key.replace('lora_down', 'lora_up'))
            pair_keys.append(key)
        else:
            pair_keys.append(key)
            pair_keys.append(key.replace('lora_up', 'lora_down'))
        
        # update weight
        if len(state_dict[pair_keys[0]].shape) == 4:
            weight_up = state_dict[pair_keys[0]].squeeze(3).squeeze(2).to(torch.float32)
            weight_down = state_dict[pair_keys[1]].squeeze(3).squeeze(2).to(torch.float32)
            curr_layer.weight.data += alpha * torch.mm(weight_up, weight_down).unsqueeze(2).unsqueeze(3)
        else:
            weight_up = state_dict[pair_keys[0]].to(torch.float32)
            weight_down = state_dict[pair_keys[1]].to(torch.float32)
            curr_layer.weight.data += alpha * torch.mm(weight_up, weight_down)
            
        # update visited list
        for item in pair_keys:
            visited.append(item)

    #Generating the needed picture through the pipeline
    pipeline = pipeline.to("cuda")
    with torch.no_grad():
        #Giving additional commands to the SD engine to style the pictures. Prompt generated from the resource picture is used here.
        image = pipeline(prompt=prompt, height=height, width=width, num_inference_steps=25,).images[0]

    image.save(output_path)
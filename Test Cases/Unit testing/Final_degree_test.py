import os
from AIProcessing import generation
from pathlib import Path

image_in = r'./s_1.png'
image_out = r'./'

for i in range(5):
    deepdanbooru_model_path = './deepdanbooru_model'
    os.system("deepdanbooru evaluate {}... --project-path {} --allow-folder --save-txt".format(image_in, deepdanbooru_model_path))
    tag_path = Path(image_in).with_suffix('.txt')
    with open(tag_path, 'r') as file:
        content = file.readline().split(',')
        del content[-1]
        content = ", ".join(content)

    SD_path = './sd_model/SDV15'
    Lora_path = './lora_model/pixel-portrait-v1.safetensors'

    #Generating the picture from functions in AIProcessing.py
    generation(SD_path, Lora_path, content, image_out + str(i) + '.png' , height = 512, width = 512)
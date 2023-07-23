# USER MANUAL

## Hardware Requirements
PIXIE utilises AI image rendering algorithms which could take a toll on low-end machines. To ensure a favourable usage experience, we would highly recommend the the program to be functioning on a device with following specs: 
- CPU:  Any modern AMD or Intel CPU
- RAM: A minimum of 16 gigabytes of DDR4 or DDR5 RAM
- Storage: Any SATA or NVMe solid-state drive from a reputable company that is 256 gigabytes or larger. You need at least 10 gigabytes of free space available. Typically, one terabyte drives offer the best price per gigabyte of storage.
- GPU: Any GeForce RTX GPU with a minimum of 8 gigabytes of GDDR6 memory.

## Installation Guide

### Necessary Software Platforms/Libraries
To execute PIXIE, you will need the following platforms/libraries (they can mostly be installed with PIP):
- A Python of version 3.10 (Higher versions exists compatibility issues with Pytorch)
- Pytorch (compatible with CUDA 11.7)
- Diffusers (https://github.com/huggingface/diffusers)
- Transformers (https://github.com/huggingface/transformers)
- Deepdanbooru (https://github.com/KichangKim/DeepDanbooru)
- Tensorflow
- Tensorflow-io
- Click
- Requests
- Scikit-image
- Six 
- Pillow
- Numpy
- OpenCV
- Ttkbootstrap

### Necessary AI models
Apart from the library requirements, AI image processing also forms an integral portion of PIXIE’s functions. The following section will walkthrough how required modules will be installed in the program’s execution.

#### Stable Diffusion V1.5 Base model (Loaded to diffusers)
- Obtain a checkpoint file of the V1.5 based model. (For our purposes the pruned-emaonly file is sufficient) (v1-5-pruned-emaonly.ckpt)
- In the Diffusers library’s directory, find convert_original_stable_diffusion_to_diffusers.py. In your command panel, execute
python ./scripts/convert_original_stable_diffusion_to_diffusers.py --checkpoint_path xxx.ckpt  --dump_path save_dir to load the model into diffusers format.
- Move the resulted output to PIXIE’s directory, under the sd_model folder.This will mark the successful installation of the Stable diffusion base model.

  










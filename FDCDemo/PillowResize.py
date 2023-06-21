from PIL import Image

def pillow_process(image_path, output_path):

    img = Image.open(image_path)
    o_width, o_height = img.size
    
    pixel_size = int(max(o_width,o_height) * 0.03)
    if pixel_size > 10:
        pixel_size = 10
    processed_width = o_width // pixel_size
    processed_height = o_height // pixel_size

    img = img.resize((processed_width, processed_height), resample=Image.BICUBIC)
    img = img.resize((o_width, o_height), resample=Image.NEAREST)

    img.save(output_path)

import numpy as np
from cv2 import imread, IMREAD_COLOR, resize, INTER_CUBIC, INTER_NEAREST, IMREAD_GRAYSCALE, Sobel, CV_64F, imwrite
'''
Pixelating Image using advance functions from cv2 and numpy (Emphasies Outlines, Lower Colour Steps)
'''
def cv_process(image_path, output_path, pixel_size, acceptance, colour_units, ink_percentage):
    img = imread(image_path, IMREAD_COLOR)
    height, width, null = img.shape

    processed_height = height // pixel_size
    processed_width = width // pixel_size

    processed_img = resize(img, (processed_width, processed_height), interpolation = INTER_CUBIC)
    resulted_img = resize(processed_img, (width, height), interpolation = INTER_NEAREST) #Resizing function if required size is smaller. In this case is redundant.
    

    base_img = imread(image_path, IMREAD_GRAYSCALE) #Obtaining grayscale image for gradient calculation
    gradient_x = Sobel(base_img, CV_64F, 1, 0, ksize = 5)
    gradient_y = Sobel(base_img, CV_64F, 0, 1, ksize = 5)
    gradient_map = np.sqrt(np.power(gradient_x, 2) + np.power(gradient_y, 2)) #Obtain colour gradients using Sobel

    for y in range(height):
        for x in range(width):
            particular_gradient_value = abs(gradient_map[y][x]) #Obtain only the absolute differences
            if particular_gradient_value < acceptance:
                particular_gradient_value = 0 #Clearing the differences for other areas to avoid processing them as outlines
            gradient_map[y][x] = particular_gradient_value 
    
    img_outline = resize(gradient_map, (width, height), interpolation= INTER_NEAREST) #Produce Image map of only outlines

    colour_interval = 255/colour_units
    for y in range(height):
        for x in range(width):
            for rgb_values in range(3):
                resulted_img[y][x][rgb_values] = int(resulted_img[y][x][rgb_values]/colour_interval) * colour_interval #Lowering the coloursteps of the original image
                if (img_outline[y][x] != 0):
                    resulted_img[y][x][rgb_values] = int(resulted_img[y][x][rgb_values] * ink_percentage) #Processing the outlines
    
    imwrite(img = resulted_img, filename = output_path)

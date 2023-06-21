import numpy as np
from cv2 import *
'''
Pixelating Image using advance functions from cv2 and numpy (Emphasies Outlines, Lower Colour Steps)
'''
def cv_process(image_path, output_path):
    img = imread(image_path, IMREAD_COLOR)
    height, width, null = img.shape

    resulted_img = resize(img, (width, height), interpolation = INTER_NEAREST) #Resizing function if required size is smaller. In this case is redundant.
    

    base_img = imread(image_path, IMREAD_GRAYSCALE) #Obtaining grayscale image for gradient calculation
    gradient_map = Laplacian(base_img, CV_64F, ksize = 5) #Obtain colour gradients using Laplacian
    acceptance = 700 #Tolerance for gradient differences. A very high difference indicates outline

    for y in range(height):
        for x in range(width):
            particular_gradient_value = abs(gradient_map[y][x]) #Obtain only the absolute differences
            if particular_gradient_value < acceptance:
                particular_gradient_value = 0 #Clearing the differences for other areas to avoid processing them as outlines
            gradient_map[y][x] = particular_gradient_value 
    
    img_outline = resize(gradient_map, (width, height), interpolation= INTER_NEAREST) #Produce Image map of only outlines

    colour_units = 16 #Indication of the colour steps of the new image
    colour_interval = 255/colour_units
    ink_percentage = 0.4 #Indicate how darken the outlines of the new image is. Lower value means higher emphasis on the lines
    for y in range(height):
        for x in range(width):
            for rgb_values in range(3):
                resulted_img[y][x][rgb_values] = int(resulted_img[y][x][rgb_values]/colour_interval) * colour_interval #Lowering the coloursteps of the original image
                if (img_outline[y][x] != 0):
                    resulted_img[y][x][rgb_values] = int(resulted_img[y][x][rgb_values] * ink_percentage) #Processing the outlines
    
    imwrite(img = resulted_img, filename = output_path)

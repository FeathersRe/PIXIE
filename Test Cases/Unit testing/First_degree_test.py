from OpencvResize import cv_process

#Initialising image test cases
image_in = r'Insert input path here'
image_out = r'Insert output path here'

#Test settings for first degree conversion
test_variables = [(5, 750, 16, 0.3), (6, 800, 32, 0.5), (7, 850, 64, 0.6), (8, 900, 128, 0.7), (10, 1000, 256, 0.7)]

for i in range(len(test_variables)):
    cv_process(image_in, image_out + str(i) + '\.png', test_variables[i][0], test_variables[i][1], test_variables[i][2], test_variables[i][3])
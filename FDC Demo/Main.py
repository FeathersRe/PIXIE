import OpencvResize
import os
import PySimpleGUI as ui
import shutil

'''
PIXIE 1.0
Last adjusted on 24/6/23
'''

#Setting up the UI panel
ui.theme('DarkPurple1')
lst = ['OpenCV']
layout = [[ui.Text('Welcome to PIXIE 1.0 User Menu', font=('Arial Bold', 20), size = 20, expand_x = True, justification = 'center')], \
         [ui.Text('Please select your conversion medium!', font=('Arial Bold', 15), size = 15, expand_x = True, justification = 'center')], \
         [ui.Combo(lst, size=(30,6), key ='-MD-', enable_events=True, expand_x = True)], \
         [ui.Text('Please select your desired file!', font=('Arial Bold', 15), size = 15, expand_x = True, justification = 'center')], \
         [ui.Input(enable_events=True, key='-IN-',font=('Arial Bold', 12),expand_x=True), ui.FileBrowse()], \
         [ui.Button('Start', font=('Arial Bold', 12), key= '-ST-', size = 12, pad = ((160,0), (20,0)), enable_events=True)]]
window = ui.Window('PIXIE 1.0', layout, size=(500,250))

#Running the Main Program
while True:
    event,values = window.read()
    if event == None:
        break
    if event == '-ST-': #If the Start Button is pushed
        selected_mode = values['-MD-'] #Read for the Mode Input
        selected_file = values['-IN-'] #Read for the Picture Input
        
        #Creating the necessary folders to store input and output
        if not os.path.exists(os.path.join(os.getcwd(),"Inputs")):
            os.mkdir(os.path.join(os.getcwd(),"Inputs"))
        if not os.path.exists(os.path.join(os.getcwd(),"Outputs")):
            os.mkdir(os.path.join(os.getcwd(),"Outputs"))
        
        #Processing administrative operations on the file
        filename = os.path.basename(selected_file) #Obtaining the filename
        image_path = os.path.join(os.path.join(os.getcwd(),"Inputs"), filename) 
        output_path = os.path.join(os.path.join(os.getcwd(),"Outputs"), filename)
        shutil.copyfile(selected_file, image_path) #Storing the file in the input location

        if selected_mode == "OpenCV":
            pixel_size = 5 #Size of an indiviudal pixel in the final drawing
            acceptance = 700 #Tolerance for gradient differences. A very high difference indicates outline
            colour_units = 16 ##Indication of the colour steps of the new image
            ink_percentage = 0.4 #Indicate how darken the outlines of the new image is. Lower value means higher emphasis on the lines
            result = OpencvResize.cv_process(image_path, output_path, pixel_size, acceptance, colour_units, ink_percentage) #Rune OpenCV processing module
            
        ui.popup_no_buttons('This is your resulted image!', title='Result', keep_on_top=True, image=output_path) #Display processed image
        break
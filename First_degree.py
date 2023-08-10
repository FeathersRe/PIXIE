import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from OpencvResize import cv_process
from ttkbootstrap.dialogs import Messagebox
from PIL import ImageTk, Image


class first_degree_interface(ttk.Frame):
    def __init__(self, master, image_path, output_path):
        super().__init__(master)
        self.root = master
        self.path = image_path
        self.out = output_path
        self.pack(fill=BOTH, expand = YES)
        self.image = Image.open(self.path)
        self.filename = ImageTk.PhotoImage(self.image.resize((500, 500)))

        for i in range(2):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

        col1 = ttk.Frame(self, padding=10)
        col1.grid(row=0, column=0, sticky=NSEW)

        col2 = ttk.Frame(self, padding = 10)
        col2.grid(row=0, column=1, sticky = NSEW)
        
        #Setting up the control panel for user settings
        self.create_control_panel(col1)

        #Setting up the picture preview section
        self.create_picture_preview(col2)

        #Setting up the confirmation button and cancel button section
        self.create_confirm_section(col2)
    
    #Setting up the interactive scale bars
    def create_bar(self, master, value):
        self.setvar(value[0], value[1])

        frame = ttk.Frame(master)
        frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(frame, text=value[0]+":\t")
        lbl.pack(side=LEFT)

        #Setting up the adjustment bar
        adjustment_bar = ttk.Scale(master=frame, value = value[1], from_=value[2], to=value[3], command=lambda x=value[1], y=value[0]: self.update_value(x, y)) #Operation is linked to the update_value function to consistently update the display value
        adjustment_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

        val = ttk.Label(master=frame, textvariable=value[0])
        val.pack(padx = 5)

    #Consistently update of the display value after user input
    def update_value(self, value, name):
        self.setvar(name, f"{float(value):.0f}")

    def create_control_panel(self, master):

        control_info = ttk.Labelframe(master, text="Pixelation Settings", padding = 10)
        control_info.pack(side=TOP, fill=BOTH, expand=YES)

        settings = [("Pixel size", 5, 1, 10), ("Acceptance Level", 700, 300, 1000), ("Colour Step", 16, 1, 256), ("Ink percentage(%)", 50, 30, 70)]

        for value in settings:
            self.create_bar(control_info, value)
        
    def create_picture_preview(self, master):
        
        picture_display = ttk.Labelframe(master, text = "Picture Preview", padding = 10)
        picture_display.pack(side=TOP, fill=BOTH, expand=YES)

        picture = ttk.Label(master=picture_display, image=self.filename)
        picture.pack()
    

    def create_confirm_section(self, master):
        confirm_section = ttk.Frame(master, padding = 10)
        confirm_section.pack(fill=X, expand=YES)

        conf_btn = ttk.Button(master = confirm_section, text = "Render", command  = self.confirm, bootstyle=SUCCESS, width=6,)
        conf_btn.pack()

        done_btn = ttk.Button(master = confirm_section, text = "Done", command = self.done, bootstyle = PRIMARY, width = 6, )
        done_btn.pack()

        cnl_btn = ttk.Button(master=confirm_section, text="Cancel", command=self.cancel, bootstyle=DANGER, width = 6, )
        cnl_btn.pack()
        
    def confirm(self):
        pixel_size = self.getvar("Pixel size")
        acceptance = self.getvar("Acceptance Level")
        colour_step = self.getvar("Colour Step")
        ink_percentage = round(self.getvar("Ink percentage(%)")*0.01, 1)
        img_path = self.path
        output_path = self.out
        cv_process(img_path, output_path, pixel_size, acceptance, colour_step, ink_percentage)

    def done(self):
        Messagebox.show_info(message="Your image is in the output folder!", title="Success")
        self.quit()
    
    def cancel(self):
        self.quit()
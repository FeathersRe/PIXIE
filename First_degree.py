import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from OpencvResize import cv_process
from ttkbootstrap.dialogs import Messagebox


class first_degree_interface(ttk.Frame):
    def __init__(self, master, image_path, output_path):
        super().__init__(master)
        self.root = master
        self.path = image_path
        self.out = output_path
        self.pack(fill=BOTH, expand = YES)
        self.pixel_size = ttk.IntVar()
        self.acceptance = ttk.IntVar()
        self.colour = ttk.IntVar()
        self.ink = ttk.DoubleVar()

        self.filename = ttk.PhotoImage(file=self.path)

        for i in range(2):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

        col1 = ttk.Frame(self, padding=10)
        col1.grid(row=0, column=0, sticky=NSEW)

        col2 = ttk.Frame(self, padding = 10)
        col2.grid(row=0, column=1, sticky = NSEW)
        
        self.create_control_bar(col1, self.pixel_size, self.acceptance, self.colour, self.ink)
        self.create_picture_preview(col2)
        self.create_confirm_section(col2)

    def create_control_bar(self, master, pixel_size, acceptance, colour_step, ink):

        control_info = ttk.Labelframe(master, text="Pixelation Settings", padding = 10)
        control_info.pack(side=TOP, fill=BOTH, expand=YES)

        pixel_frame = ttk.Frame(control_info)
        pixel_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(pixel_frame, text="Pixel Size:\t")
        lbl.pack(side=LEFT)
        
        pixel_bar = ttk.Scale(pixel_frame, variable = pixel_size, value = 5, from_=1, to=10)
        pixel_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

        acceptance_frame = ttk.Frame(control_info)
        acceptance_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(acceptance_frame, text="Acceptance Level:\t")
        lbl.pack(side=LEFT)

        acceptance_bar = ttk.Scale(acceptance_frame, variable = acceptance, value = 700, from_=300, to=1000)
        acceptance_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

        colour_frame = ttk.Frame(control_info)
        colour_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(colour_frame, text="Colour Step:\t")
        lbl.pack(side=LEFT)

        colour_bar = ttk.Scale(colour_frame, variable = colour_step, value = 16, from_=1, to=256)
        colour_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

        ink_frame = ttk.Frame(control_info)
        ink_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(ink_frame, text="Ink percentage:\t")
        lbl.pack(side=LEFT)

        ink_bar = ttk.Scale(ink_frame, variable = ink, value = 0.5, from_=0.3, to=0.7)
        ink_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

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
        pixel_size = self.pixel_size.get()
        acceptance = self.acceptance.get()
        colour_step = self.colour.get()
        ink_percentage = round(self.ink.get(), 1)
        img_path = self.path
        output_path = self.out
        cv_process(img_path, output_path, pixel_size, acceptance, colour_step, ink_percentage)


    def done(self):
        Messagebox.show_info(message="Your image is in the output folder!", title="Success")
        self.quit()
    
    def cancel(self):
        self.quit()
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class first_degree_interface(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        self.pack(fill=BOTH, expand = YES)
    
        for i in range(2):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)

        #Control panel - Column 1
        col1 = ttk.Frame(self, padding=10)
        col1.grid(row=0, column=0, sticky=NSEW)

        control_info = ttk.Labelframe(col1, text="Pixelation Settings", padding = 10)
        control_info.pack(side=TOP, fill=BOTH, expand=YES)

        pixel_frame = ttk.Frame(control_info)
        pixel_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(pixel_frame, text="Pixel Size:")
        lbl.pack(side=LEFT)

        pixel_bar = ttk.Scale(pixel_frame, value = 5, from_=1, to=30)
        pixel_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

        acceptance_frame = ttk.Frame(control_info)
        acceptance_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(acceptance_frame, text="Acceptance Level:")
        lbl.pack(side=LEFT)

        acceptance_bar = ttk.Scale(acceptance_frame, value = 700, from_=100, to=2000)
        acceptance_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

        colour_frame = ttk.Frame(control_info)
        colour_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(colour_frame, text="Colour Step:")
        lbl.pack(side=LEFT)

        colour_bar = ttk.Scale(colour_frame, value = 16, from_=1, to=256)
        colour_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)

        ink_frame = ttk.Frame(control_info)
        ink_frame.pack(fill=X, padx=(20,0), pady=5)

        lbl = ttk.Label(ink_frame, text="Ink percentage:")
        lbl.pack(side=LEFT)

        ink_bar = ttk.Scale(ink_frame, value = 0.5, from_=0, to=1)
        ink_bar.pack(side=LEFT, fill=X, expand=YES, padx=5)


if __name__ == '__main__':

    app = ttk.Window("Magic Mouse", "yeti")
    first_degree_interface(app)
    app.mainloop()

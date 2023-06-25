import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from tkinter.filedialog import askopenfilename
from First_degree import first_degree_interface

class start(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding = (20,10))
        self.root = master
        self.filename = ttk.StringVar()
        self.pack(fill=BOTH, expand = YES)

        self.mode = ttk.StringVar(value="")
        self.filename = ttk.StringVar(value="")

        hdr_txt = "Welcome to PIXIE 2.0"
        hdr  = ttk.Label(master=self, font="-size 12", anchor=CENTER, text = hdr_txt, width = 50)
        hdr.pack(fill = X, expand=YES, pady = 10)

        self.create_mode(self.mode)
        self.create_filebrowse(self.filename)
        self.create_action()

    def create_mode(self, input_variable):
        lbl_text = "Select your desired conversion mode!"
        lbl_menu = ["First Degree Conversion(FDC1)", "Final Degree Conversion(FDC2)"]

        section = ttk.Frame(self)
        section.pack(fill=X, expand = YES)
        
        lbl = ttk.Label(master=section, font="-size 10", text = lbl_text, anchor = CENTER, width = 30)
        lbl.pack(fill = X, expand=YES, pady = 10)

        mode = ttk.OptionMenu(section, input_variable, "", *lbl_menu) 
        mode.pack(fill=X, expand=YES) 

    def create_filebrowse(self, input_variable):
        lbl_text = "Select your desired character image!"
        
        section = ttk.Frame(self)
        section.pack(fill = X, expand = YES)
        
        lbl = ttk.Label(master=section, font="-size 10", text = lbl_text, anchor = CENTER, width = 30)
        lbl.pack(fill = X, expand=YES, pady = 10)

        image_input = ttk.Entry(master=section, textvariable = input_variable)
        image_input.pack(side=LEFT, fill=X, expand = YES, padx=(0, 5), pady=10)

        browse_button = ttk.Button(master=section, text="Browse", command = self.search_file)
        browse_button.pack(side=RIGHT, fill=X, padx = (5,0), pady = 10)

    def create_action(self):
        section = ttk.Frame(self)
        section.pack(fill=X, expand=YES, pady=(15, 10))

        cnl_btn = ttk.Button(master=section, text="Cancel", command=self.cancel, bootstyle=DANGER, width = 6, )
        cnl_btn.pack(side=RIGHT, padx = 5)

        conf_btn = ttk.Button(master = section, text = "Submit", command  = self.confirm, bootstyle=SUCCESS, width=6,)
        conf_btn.pack(side=RIGHT, padx = 5)

    
    def search_file(self):
        path = askopenfilename()
        if path:
            self.filename.set(path)

    def cancel(self):
        self.quit()

    def confirm(self):
        selected_mode = self.mode.get()
        if selected_mode == "First Degree Conversion(FDC1)":
            img_path = self.filename.get()
            first_degree_interface(self.root, img_path)
        elif selected_mode == "Final Degree Conversion(FDC2)":
            Messagebox.show_info(message="Function under development. Stay tuned!", title="Final Degree Conversion Module")

if __name__ == "__main__":
    app = ttk.Window("PIXIE 2.0", "litera", resizable = (False, False))
    start(app)
    app.mainloop()
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from AIProcessing import generation
from ttkbootstrap.dialogs import Messagebox
from pathlib import Path

class final_degree_interface(ttk.Frame):
    def __init__(self, master, image_path, output_path, filename):
        super().__init__(master)
        self.root = master
        self.path = image_path
        self.out = output_path
        self.filename = filename.split(".")[0]
        self.pack(fill=BOTH, expand = YES)

        self.create_confirm_section()

    def create_confirm_section(self):
        lbl_text = "Click Render to begin Conversion!"
        confirm_section = ttk.Frame(self.root, padding = 10)
        confirm_section.pack(fill=X, expand=YES)

        lbl = ttk.Label(master=confirm_section, font="-size 10", text = lbl_text, anchor = CENTER, width = 30)
        lbl.pack(fill = X, expand=YES, pady = 10)
        conf_btn = ttk.Button(master = confirm_section, text = "Render", command  = self.render, bootstyle=SUCCESS, width=6,)
        conf_btn.pack(fill = X)
        cnl_btn = ttk.Button(master=confirm_section, text="Cancel", command=self.cancel, bootstyle=DANGER, width = 6,)
        cnl_btn.pack(fill = X)

    def render(self):
        Messagebox.show_info(message="Conversion is ongoing, please wait!", title="Ongoing")
        deepdanbooru_model_path = './deepdanbooru_model'
        os.system("deepdanbooru evaluate {}... --project-path {} --allow-folder --save-txt".format(self.path, deepdanbooru_model_path))
        tag_path = Path(self.path).with_suffix('.txt')
        with open(tag_path, 'r') as file:
            content = file.readline().split(',')
            del content[-1]
            content = ", ".join(content)
        SD_path = './sd_model/SDV15'
        Lora_path = './lora_model/pixel-portrait-v1.safetensors'
        generation(SD_path, Lora_path, content, self.out, height = 512, width = 512)
        Messagebox.show_info(message="Your image is in the output folder!", title="Success")
        self.quit()

    def cancel(self):
        self.quit()
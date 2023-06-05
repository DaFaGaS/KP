import customtkinter as tk

from db.models.models import *
from frames.baseframe import Frame
from tkinter import messagebox

class CommentWindow(Frame):
    def __init__(self, root, controller, dir_model: RequestsModel):
        super().__init__(root, controller)
        self.model = dir_model
        self.root = root
        self.controller = controller

    def create_widgets(self, controller):
        self.label_comment = tk.CTkLabel(self, text="Комментарий")
        self.label_comment.pack()

        self.cooment_entry = tk.CTkTextbox(self, width=350, height=200)
        self.cooment_entry.insert("0.0", self.model.comment)
        self.cooment_entry.pack()

        self.but_destroy = tk.CTkButton(self, text="ОК", command=lambda: controller.temp_win.destroy())
        self.but_destroy.pack(padx=0, pady=[0,30], side=tk.BOTTOM)

        self.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

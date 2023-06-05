import customtkinter as tk
from frames.baseframe import Frame
from db.models.models import *
from tkinter import messagebox

class ChangeStatusWindow(Frame):
    def __init__(self, root, controller, but : int):
        super().__init__(root, controller)
        self.but = but
        self.root = root
        self.controller = controller

    def create_widgets(self, controller):
        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

        self.status = tk.CTkLabel(self, text = "Статус: ")
        self.status.pack(pady=10)
        self.status_combo = tk.CTkComboBox(self, values=["Выберите...", "В процессе","Задержка","Готово"])
        self.status_combo.pack(pady=10)

        self.status_change = tk.CTkButton(self,text="Обновить", command= lambda : controller.change_status(self.but))
        self.status_change.pack(padx=10, side = tk.RIGHT)

        self.status_dismiss = tk.CTkButton(self, text="Отмена", fg_color="#ab6d09", hover_color="#945e07", command=lambda : self.root.destroy())
        self.status_dismiss.pack(padx=10, side=tk.LEFT)

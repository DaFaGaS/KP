import customtkinter as tk
from frames.baseframe import Frame
from tkinter import messagebox

class AddRequestWindow(Frame):
    def create_widgets(self, controller):
        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

        self.hardware = tk.CTkLabel(self, text = "С каким оборудованием проблемы?: ")
        self.hardware.pack()
        self.hardware_combo = tk.CTkComboBox(self, values=["Выберите...","Периферия","Компьютер","Специальное", "Программное Обеспечение","Другое (Комментарий)"])
        self.hardware_combo.pack()

        self.kind_of_help = tk.CTkLabel(self, text="Какого характера нужна помощь?: ")
        self.kind_of_help.pack()
        self.kind_of_help_combo = tk.CTkComboBox(self, values=["Выберите...","Ремонт", "Обновление", "Консультация"])
        self.kind_of_help_combo.pack()

        self.department = tk.CTkLabel(self, text="Укажите ваш отдел: ")
        self.department.pack()
        self.department_combo = tk.CTkComboBox(self, values=["Выберите...","Цокольный этаж", "Первый этаж", "Второй этаж", "Третий этаж"])
        self.department_combo.pack()

        self.comment = tk.CTkLabel(self, text="Оставьте комментарий (если есть):")
        self.comment.pack()
        self.comment_entry = tk.CTkTextbox(self, height=155, width=300)
        self.comment_entry.insert("0.0", "Клиент: " + controller.showed_frame.user_login.cget("text") + "\n")
        self.comment_entry.pack()

        self.request_create = tk.CTkButton(self,text="Создать", command= lambda:controller.add_request())
        self.request_create.pack(padx=50, side = tk.RIGHT)

        self.request_dismiss = tk.CTkButton(self, text="Отмена", fg_color="#ab6d09", hover_color="#945e07", command=lambda : self.root.destroy())
        self.request_dismiss.pack(padx=50, side=tk.LEFT)

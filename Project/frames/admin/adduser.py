import customtkinter as tk
from frames.baseframe import Frame
from tkinter import messagebox

class AddUserWindow(Frame):
    def create_widgets(self, controller):
        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

        self.login = tk.CTkLabel(self, text="Введите логин пользователя:")
        self.login.pack()

        self.entry_login = tk.CTkEntry(self)
        self.entry_login.pack()

        self.password = tk.CTkLabel(self, text="Введите пароль пользователя:")
        self.password.pack()

        self.entry_password = tk.CTkEntry(self)
        self.entry_password.pack()

        self.role = tk.CTkLabel(self, text="Выберите роль пользователя: ")
        self.role.pack()
        self.role_combo = tk.CTkComboBox(self, values=["Выберите...","Клиент", "Специалист", "Администратор"])
        self.role_combo.pack()

        self.user_create = tk.CTkButton(self,text="Создать", command= lambda:controller.add_user())
        self.user_create.pack(padx=50, side = tk.RIGHT)

        self.user_dismiss = tk.CTkButton(self, text="Отмена", fg_color="#ab6d09", hover_color="#945e07", command=lambda : self.root.destroy())
        self.user_dismiss.pack(padx=30, side=tk.LEFT)

import customtkinter as tk

from db.models.models import *
from frames.baseframe import Frame
from tkinter import messagebox

class UserEditWindow(Frame):
    def __init__(self, root, controller, dir_model: UserModel):
        super().__init__(root, controller)
        self.model = dir_model
        self.root = root
        self.controller = controller
        self.roles_dict_temp = {
            "Администратор": "admin", "Менеджер Рейсов": "flight_manager", "Менеджер ЛС": "crew_manager",
            "Менеджер ВС": "plane_manager", "Пилот/Стюардесса": "pilot"
        }
        self.roles_dict = {y: x for x, y in self.roles_dict_temp.items()}

    def create_widgets(self, controller):
        self.label_login = tk.CTkLabel(self, text="Логин")
        self.label_login.pack()

        self.entry_login = tk.CTkEntry(self)
        self.entry_login.insert(0, self.model.login)
        self.entry_login.pack()

        #print(self.entry_full_name.get())

        self.label_password = tk.CTkLabel(self, text="Пароль")
        self.label_password.pack()

        self.entry_password = tk.CTkEntry(self)
        self.entry_password.insert(0, self.model.password)
        self.entry_password.pack()

        self.label_role = tk.CTkLabel(self, text="Роль")
        self.label_role.pack()

        self.entry_role = tk.CTkEntry(self,justify=tk.CENTER)
        self.entry_role.insert(0, self.model.role)
        self.entry_role.configure(state=tk.DISABLED)
        self.entry_role.pack()

        self.user_refresh = tk.CTkButton(self, text="Изменить", command=lambda: controller.edit_user())
        self.user_refresh.pack(padx=50, pady= [70,0], side=tk.RIGHT)

        self.user_delete = tk.CTkButton(self, text="Удалить",fg_color="#FF7CA3", command=lambda: controller.delete_user_dialog(self.model.id))
        self.user_delete.place(relx=0.5,rely=0.6, anchor=tk.CENTER)

        self.user_dismiss = tk.CTkButton(self, text="Отмена", fg_color="#ab6d09", hover_color="#945e07", command=lambda: self.root.destroy())
        self.user_dismiss.pack(padx=50, pady= [70,0], side=tk.LEFT)

        self.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

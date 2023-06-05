import customtkinter as tk
from frames.baseframe import Frame
from db.models.models import *


class User():
    def __init__(self, user_model : UserModel, controller, parent_frame):
        self.user_model = user_model


        dir_rect = tk.CTkFrame(parent_frame, height=80, width=1300)
        name = tk.CTkLabel(dir_rect, text="Пользователь: " + self.user_model.login, font=("Verdana", 26))
        edit_button = tk.CTkButton(dir_rect, text="Редактировать", font=("Verdana", 16), command = lambda: controller.edit_user_window(self.user_model))


        dir_rect.pack(fill=tk.X, pady=1)
        name.place(relheight=1, x=30)
        edit_button.place(relheight=1, relx=0.86)
import customtkinter as tk
from frames.baseframe import Frame
from db.models.models import *


class Request():
    def __init__(self, requests_model : RequestsModel, controller, parent_frame):
        self.requests_model = requests_model


        dir_rect = tk.CTkFrame(parent_frame, height=80, width=1300)
        name = tk.CTkLabel(dir_rect, text="Оборудование -  " + self.requests_model.hard + "; Помощь - " + self.requests_model.help + "; Отдел - " + self.requests_model.department, font=("Verdana", 20))
        comm_button = tk.CTkButton(dir_rect, text="Комментарий", font=("Verdana", 16), command = lambda: controller.show_comment_window(self.requests_model))
        edit_button = tk.CTkButton(dir_rect, text="Взять", font=("Verdana", 16), command = lambda: controller.take_request(self.requests_model))


        dir_rect.pack(fill=tk.X, pady=1)
        name.place(relheight=1, x=30)
        comm_button.place(relheight=1, relx=0.75)
        edit_button.place(relheight=1, relx=0.86)
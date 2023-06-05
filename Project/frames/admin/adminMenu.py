import customtkinter as tk
from frames.baseframe import Frame
from frames.scrollFrame import ScrollFrame
import db.database as db
from tkinter import messagebox



class AdminMenu(Frame):
    def create_widgets(self, controller):
        self.configure(width=1024, height=1024, fg_color="gray90")
        self.place(relwidth=1, relheight=1)



        #       ----------BORDERS----------
        self.upper_frame = tk.CTkFrame(self, height=65, width=1100, fg_color="#65ab9e")
        self.upper_frame.place(relwidth=1)

        self.upper_info = tk.CTkLabel(self, text=f'Главное меню Администратора:', font=("Verdana", 20),fg_color="#65ab9e")
        self.upper_info.place(y=5, relwidth=1)

        self.user_login = tk.CTkLabel(self, text="Test_User", font=("Verdana", 20),fg_color="#65ab9e")
        self.user_login.place(y=30, relwidth=1)

        self.lower_frame = tk.CTkFrame(self)
        self.lower_frame.configure(height=165, width=1100, fg_color="#65ab9e")
        self.lower_frame.place(relwidth=1, rely=0.85, relx=0)

        self.lower_info = tk.CTkLabel(self, justify='left',text="Общество с Ограниченной Ответственностью ''Обитель сна''\nНе несёт ответственности за работоспособность программного обеспечения\nПроконсультируйтесь со своим лечащим врачом",font=("Verdana", 10), fg_color="#65ab9e")
        self.lower_info.place(x=10, rely=0.87, relx=0.0)

        self.lower_info1 = tk.CTkLabel(self, width=100, justify='left', text="©2023-2023", font=("Verdana", 10),fg_color="#65ab9e")
        self.lower_info1.place(x=-5, relx=0.0, rely=0.92)

        self.request_leave = tk.CTkButton(self, width=200, height=64, bg_color="black", text="Зарегистрировать\nпользователя", command= lambda : controller.add_user_window())
        self.request_leave.place(anchor='w', relx=0, y=32)

        self.user_unauth = tk.CTkButton(self, width=200, height=65, bg_color="#65ab9e", text="Выйти",command=lambda: controller.unauthorize())
        self.user_unauth.place(relx=1, rely=0, anchor="ne")

        #       ----------BORDERS----------


        #       ----------USERFRAME----------
        self.content_panel = ScrollFrame(self)
        controller.show_users()
        #       ----------USERFRAME----------
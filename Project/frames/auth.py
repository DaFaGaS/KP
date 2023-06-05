import customtkinter as tk
from frames.baseframe import Frame


class Authentification(Frame):
    def create_widgets(self, controller):
        self.configure(width=1024, height=1024, fg_color="gray90")
        self.place(relwidth=1, relheight=1)


#       ----------BORDERS----------
        self.upper_frame = tk.CTkFrame(self)
        self.upper_frame.configure(height=65, width=1100, fg_color="#65ab9e")
        self.upper_frame.place(relwidth=1)

        self.upper_info = tk.CTkLabel(self, text = "Добро пожаловать на сервер \n''Курсовой Проект''!", font = ("Verdana", 20), fg_color="#65ab9e")
        self.upper_info.place(y=5, relwidth=1)

        self.lower_frame = tk.CTkFrame(self)
        self.lower_frame.configure(height=165, width=1100, fg_color="#65ab9e")
        self.lower_frame.place(relwidth=1, rely=0.85, relx=0)

        self.lower_info = tk.CTkLabel(self, justify='left', text="Общество с Ограниченной Ответственностью ''Обитель сна''\nНе несёт ответственности за работоспособность программного обеспечения\nПроконсультируйтесь со своим лечащим врачом", font=("Verdana", 10),fg_color="#65ab9e")
        self.lower_info.place(x=10,rely=0.87, relx=0.0)

        self.lower_info1 = tk.CTkLabel(self, width=100,justify='left',text="©2023-2023",font=("Verdana", 10), fg_color="#65ab9e")
        self.lower_info1.place(x=-5, relx=0.0, rely=0.92)
#       ----------BORDERS----------


#       ----------AUTHFRAME----------
        self.auth_frame = tk.CTkFrame(self,fg_color="#86e3d2",width=300, height=300)
        self.auth_frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        self.login = tk.CTkLabel(self.auth_frame, text='Логин', fg_color="transparent", corner_radius=0)
        self.login.pack(padx=100,pady=(10,0))
        self.login_entry = tk.CTkEntry(self.auth_frame, width=200, placeholder_text="Введите свой логин...")
        self.login_entry.pack()

        self.passwd = tk.CTkLabel(self.auth_frame, text='Пароль', fg_color="#86e3d2")
        self.passwd.pack(pady=(10,0))
        self.passwd_entry = tk.CTkEntry(self.auth_frame, width=200,placeholder_text="Введите свой пароль...", show="*")
        self.passwd_entry.pack()

        self.button = tk.CTkButton(self.auth_frame, text="Войти в аккаунт", command = lambda : controller.auth_login())
        self.button.pack(pady=(20,15))
#       ----------AUTHFRAME----------


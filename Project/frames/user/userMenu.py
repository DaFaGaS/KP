import customtkinter as tk
from frames.baseframe import Frame
import db.database as db
from tkinter import messagebox



class UserMenu(Frame):
    def create_widgets(self, controller):
        self.configure(width=1024, height=1024, fg_color="gray90")
        self.place(relwidth=1, relheight=1)



        #       ----------BORDERS----------
        self.upper_frame = tk.CTkFrame(self)
        self.upper_frame.configure(height=65, width=1100, fg_color="#65ab9e")
        self.upper_frame.place(relwidth=1)

        self.upper_info = tk.CTkLabel(self, text=f'Главное меню Клиента:', font=("Verdana", 20),fg_color="#65ab9e")
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

        self.request_leave = tk.CTkButton(self, width=200, height=64, bg_color="black", text="Оставить\nзаявку",command=lambda: controller.add_request_window())
        self.request_leave.place(anchor='w', relx=0, y=32)

        self.user_unauth = tk.CTkButton(self, width=200, height=65, bg_color="#65ab9e", text="Выйти",command=lambda: controller.unauthorize())
        self.user_unauth.place(relx=1, rely=0, anchor="ne")

        self.updatebutton=tk.CTkButton(self,width=200, height=64,text="Обновить", bg_color="black", command=lambda : controller.update_user())
        self.updatebutton.place(anchor='w', relx=0.1565, y=32)
        #       ----------BORDERS----------


        #       ----------USERFRAME----------
        self.request1_frame = tk.CTkFrame(self,fg_color="#86e3d2", width=500, height=175,)
        self.request1_frame.place(x=25, rely=0.11)

        self.request2_frame = tk.CTkFrame(self, fg_color="#86e3d2", width=500, height=175)
        self.request2_frame.place(x=25, rely=0.36)

        self.request3_frame = tk.CTkFrame(self, fg_color="#86e3d2", width=500, height=175)
        self.request3_frame.place(x=25, rely=0.61)

        self.info_frame = tk.CTkFrame(self, fg_color="gray80", width=700, height=590)
        self.info_frame.place(x= 1300, y=358, anchor='e')
        #       ----------USERFRAME----------


        #       ----------REQUEST_FRAMES----------
        self.req1_label = tk.CTkLabel(self, text=f'Заявка №1', font=("Verdana", 16), fg_color="#86e3d2")
        self.req1_label.place(x=225, rely=0.12)
        self.req1_button = tk.CTkButton(self, width=300, text="Информация", bg_color="#86e3d2", command= lambda : controller.see_content_user(1))
        self.req1_button.place(x=125, rely=0.17)
        self.req1_status = tk.CTkLabel(self,width=300, text="Обновите, чтобы узнать статус", corner_radius=5,font=("Verdana", 16), fg_color="#0cc27c", text_color="gray90", bg_color="#86e3d2")
        self.req1_status.place(x=125, rely=0.22)
        self.req1_close = tk.CTkButton(self, width=300, state="disabled", text="Закрыть", bg_color="#86e3d2",fg_color="#088a58", command= lambda : controller.close_request(0))
        self.req1_close.place(x=125, rely=0.27)


        self.req2_label = tk.CTkLabel(self, text=f'Заявка №2', font=("Verdana", 16), fg_color="#86e3d2")
        self.req2_label.place(x=225, rely=0.37)
        self.req2_button = tk.CTkButton(self, width=300, text="Информация", bg_color="#86e3d2", command= lambda : controller.see_content_user(2))
        self.req2_button.place(x=125, rely=0.42)
        self.req2_status = tk.CTkLabel(self, width=300, text="Обновите, чтобы узнать статус", corner_radius=5, font=("Verdana", 16), fg_color="#0cc27c", text_color="gray90", bg_color="#86e3d2")
        self.req2_status.place(x=125, rely=0.47)
        self.req2_close = tk.CTkButton(self, width=300, state="disabled", text="Закрыть", bg_color="#86e3d2",fg_color="#088a58", command= lambda : controller.close_request(1))
        self.req2_close.place(x=125, rely=0.52)

        self.req3_label = tk.CTkLabel(self, text=f'Заявка №3', font=("Verdana", 16), fg_color="#86e3d2")
        self.req3_label.place(x=225, rely=0.62)
        self.req3_button = tk.CTkButton(self, width=300, text="Информация", bg_color="#86e3d2", command= lambda : controller.see_content_user(3))
        self.req3_button.place(x=125, rely=0.67)
        self.req3_status = tk.CTkLabel(self, width=300, text="Обновите, чтобы узнать статус", font=("Verdana", 16), corner_radius=5, fg_color="#0cc27c",text_color="gray90", bg_color="#86e3d2")
        self.req3_status.place(x=125, rely=0.72)
        self.req3_close = tk.CTkButton(self, state = "disabled", width=300, text="Закрыть", bg_color="#86e3d2", fg_color="#088a58", command= lambda : controller.close_request(2))
        self.req3_close.place(x=125, rely=0.77)
        #       ----------REQUEST_FRAMES----------


        #       ----------INFO_FRAME----------
        self.info_hardware = tk.CTkLabel(self, text="Оборудование: ", font=("Verdana", 16), fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_hardware.place(x=650,y=100)
        self.info_hardware_answer = tk.CTkLabel(self, text="***", font=("Verdana", 16), fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_hardware_answer.place(x=800, y=100)

        self.info_help = tk.CTkLabel(self, text="Характер помощи: ", font=("Verdana", 16), fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_help.place(x=650, y=150)
        self.info_help_answer = tk.CTkLabel(self, text="***", font=("Verdana", 16),fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_help_answer.place(x=830, y=150)

        self.info_department = tk.CTkLabel(self, text="Отдел: ", font=("Verdana", 16), fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_department.place(x=650, y=200)
        self.info_department_answer = tk.CTkLabel(self, text="***", font=("Verdana", 16), fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_department_answer.place(x=730, y=200)

        self.info_comment = tk.CTkLabel(self, text="Комментарий ", font=("Verdana", 16), fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_comment.place(x=900, y=250)
        self.info_comment_answer = tk.CTkTextbox(self, font=("Verdana", 16),width=520, fg_color="gray80", text_color="gray10", bg_color="gray80")
        self.info_comment_answer.insert("0.0","***")
        self.info_comment_answer.place(x=640, y=300)
        #       ----------INFO_FRAME----------


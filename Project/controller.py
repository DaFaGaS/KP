import customtkinter as tk
import db.database as db

from frames.baseframe import Frame
from tkinter import messagebox
from frames.auth import Authentification
from frames.user.userMenu import UserMenu
from frames.admin.user_panel import User
from frames.admin.adminMenu import AdminMenu
from frames.tech.techMenu import *
from frames.tech.request_panel import Request
from frames.tech.commentWindow import CommentWindow
from frames.tech.changeStatus import ChangeStatusWindow
from frames.scrollFrame import ScrollFrame
from frames.user.addrequestframe import AddRequestWindow
from frames.admin.adduser import AddUserWindow
from frames.admin.useredit import *
from db.models.models import *



class Controller():
    def __init__(self, root):
        self.root = root
        self.showed_frame = ""
        self.db = db.DB()
        self.current_content = ""
        self.role = ""
        self.id_user = ""
        self.login = ""

        self.title_dict = \
        {
            "Authentification": "Авторизация",
            "UserMenu": "Меню Клиента",
            "AdminMenu": "Меню Администратора",
            "TechMenu":"Меню Специалиста"
        }

        self.roles_dict = {
            "Администратор": "Admin", "Клиент": "User", "Техник": "Tech"
        }

        self.showed_frame = Authentification(root, self)
        self.showed_frame.create_widgets(self)


    def switch_to_frame(self, frame_name_show : str):
        """
        Переключает отображаемый фрейм по названию
        Args:
            frame_name_show :
                Наименование фрейма для переключения
        """
        self.showed_frame.destroy()
        if frame_name_show in self.title_dict.keys():
            frame_class = globals()[frame_name_show]
            self.showed_frame = frame_class(self.root, self)
            self.showed_frame.create_widgets(self)
            self.change_title(self.title_dict[frame_name_show])

    def auth_login(self):
        """
        Подтверждение входа (по нажатию кнопки ВХОД)
        """
        self.login = self.showed_frame.login_entry.get()
        password = self.showed_frame.passwd_entry.get()
        response = self.db.authenticate(self.login, password)

        if not response.fail:
            self.switch_to_frame(response.frame())
            self.showed_frame.user_login.configure(text=response.login)
            self.id_user = response.id
            self.role = response.role
        else:
            messagebox.showerror("Ошибка", "Такого пользователя не существует, или пароль неверный")

    def unauthorize(self):
        ans = messagebox.askokcancel("Выход из аккаунта", "Вы действительно хотите выйти из аккаунта?")
        if ans:
            self.role = ""
            self.id_user = ""
            self.switch_to_frame("Authentification")

    def change_title(self, title : str):
        self.root.title(title)


#       ----------USER----------


    def see_content_user(self, req_frame : int):
        """
        Просмотреть содержимое заявки.
        :param id: Айдишник конкретной панели
        :return: Нихуя
        """

        request_model = self.filter_models()
        if req_frame == 1:
            if len(request_model) < 1:
                self.showed_frame.info_hardware_answer.configure(text="*Нет информации*")
                self.showed_frame.info_help_answer.configure(text="*Нет информации*")
                self.showed_frame.info_department_answer.configure(text="*Нет информации*")
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", "*Нет информации*")
                self.showed_frame.req1_status.configure(text="Отсутствует")
            else:
                self.showed_frame.info_hardware_answer.configure(text = request_model[0].hard)
                self.showed_frame.info_help_answer.configure(text=request_model[0].help)
                self.showed_frame.info_department_answer.configure(text=request_model[0].department)
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", request_model[0].comment)
                self.showed_frame.req1_status.configure(text=request_model[0].pick_flag)
                if request_model[0].pick_flag == "Готово":
                    self.showed_frame.req1_close.configure(state = "normal", fg_color="#0cc27c")
                else:
                    self.showed_frame.req1_close.configure(state = "disabled", fg_color="#088a58")

        if req_frame == 2:
            if len(request_model) < 2:
                self.showed_frame.info_hardware_answer.configure(text="*Нет информации*")
                self.showed_frame.info_help_answer.configure(text="*Нет информации*")
                self.showed_frame.info_department_answer.configure(text="*Нет информации*")
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", "*Нет информации*")
                self.showed_frame.req2_status.configure(text="Отсутствует")
            else:
                self.showed_frame.info_hardware_answer.configure(text=request_model[1].hard)
                self.showed_frame.info_help_answer.configure(text=request_model[1].help)
                self.showed_frame.info_department_answer.configure(text=request_model[1].department)
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", request_model[1].comment)
                self.showed_frame.req2_status.configure(text=request_model[1].pick_flag)
                if request_model[1].pick_flag == "Готово":
                    self.showed_frame.req2_close.configure(state = "normal", fg_color="#0cc27c")
                else:
                    self.showed_frame.req2_close.configure(state = "disabled", fg_color="#088a58")
        if req_frame == 3:
            if len(request_model) < 3:
                self.showed_frame.info_hardware_answer.configure(text="*Нет информации*")
                self.showed_frame.info_help_answer.configure(text="*Нет информации*")
                self.showed_frame.info_department_answer.configure(text="*Нет информации*")
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", "*Нет информации*")
                self.showed_frame.req3_status.configure(text="Отсутствует")
            else:
                self.showed_frame.info_hardware_answer.configure(text=request_model[2].hard)
                self.showed_frame.info_help_answer.configure(text=request_model[2].help)
                self.showed_frame.info_department_answer.configure(text=request_model[2].department)
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", request_model[2].comment)
                self.showed_frame.req3_status.configure(text=request_model[2].pick_flag)
                if request_model[2].pick_flag == "Готово":
                    self.showed_frame.req3_close.configure(state = "normal", fg_color="#0cc27c")
                else:
                    self.showed_frame.req3_close.configure(state = "disabled", fg_color="#088a58")

    def filter_models(self):
        """
        Отфильтровать модели
        :return: отфильтрованные модели
        """
        req_model = self.db.get_all_where("requests", "UserID", self.id_user)
        filt_model = [i for i in req_model if i.pick_flag !="Закрыто"]
        return filt_model

    def update_user(self):
        request_model = self.filter_models()

        if len(request_model) < 1:
            self.showed_frame.req1_status.configure(text="Отсутствует")
        else:
            self.showed_frame.req1_status.configure(text=request_model[0].pick_flag)
            if request_model[0].pick_flag == "Готово":
                self.showed_frame.req1_close.configure(state="normal", fg_color="#0cc27c")
            else:
                self.showed_frame.req1_close.configure(state="disabled", fg_color="#088a58")

        if len(request_model) < 2:
            self.showed_frame.req2_status.configure(text="Отсутствует")
        else:
            self.showed_frame.req2_status.configure(text=request_model[1].pick_flag)
            if request_model[1].pick_flag == "Готово":
                self.showed_frame.req2_close.configure(state="normal", fg_color="#0cc27c")
            else:
                self.showed_frame.req2_close.configure(state="disabled", fg_color="#088a58")

        if len(request_model) < 3:
            self.showed_frame.req3_status.configure(text="Отсутствует")
        else:
            self.showed_frame.req3_status.configure(text=request_model[2].pick_flag)
            if request_model[2].pick_flag == "Готово":
                self.showed_frame.req3_close.configure(state="normal", fg_color="#0cc27c")
            else:
                self.showed_frame.req3_close.configure(state="disabled", fg_color="#088a58")

    def close_request(self, but: int):
        """
        Закрыть заявку, если есть статус "Готово"
        :return: Смена статуса заявки на "Закрыто"
        """
        request_model = self.db.get_all_where("requests", "UserID", self.id_user)
        self.db.alter("requests", request_model[but].id, "Picked", "Закрыто")
        if but == 0:
            self.showed_frame.req1_status.configure(text="Закрыто")
            self.showed_frame.req1_close.configure(state="disabled", fg_color="#088a58")
        if but == 1:
            self.showed_frame.req2_status.configure(text="Закрыто")
            self.showed_frame.req2_close.configure(state="disabled", fg_color="#088a58")
        if but == 2:
            self.showed_frame.req3_status.configure(text="Закрыто")
            self.showed_frame.req3_close.configure(state="disabled", fg_color="#088a58")

    def add_request_window(self):
        requests = self.filter_models()
        if len(requests) == 3:
            messagebox.showerror("Ошибка!", "Превышен лимит заявок!")
        else:
            self.temp_win = tk.CTkToplevel(self.root)
            self.temp_win.title("Добавление заявки")
            self.temp_win.geometry("500x420")
            self.temp_win_frame = AddRequestWindow(self.temp_win,self)
            self.temp_win_frame.create_widgets(self)

    def add_request(self):
        bad_option = "Выберите..."
        _hard=self.temp_win_frame.hardware_combo.get()
        _help=self.temp_win_frame.kind_of_help_combo.get()
        _department = self.temp_win_frame.department_combo.get()
        _comment = self.temp_win_frame.comment_entry.get("0.0", "end")
        _pick_flag = "Создано"
        _user_id = str(self.id_user)
        _tech_id = "0"
        if _hard == bad_option or _help == bad_option or _department == bad_option:
            messagebox.showerror("Ошибка!", "Выберите все опции!")
        else:
            self.db.add_record("requests", _hard + ";" + _help + ";" + _department + ";" + str(_comment) + ";" + _pick_flag + ";" + _user_id + ";" + _tech_id + ";")
            messagebox.showinfo("Успех", "Заявка успешно добавлена!")
            self.temp_win.destroy()


#       ----------USER----------


#       ----------ADMIN----------


    def show_users(self):
        """
        Заполнить поле для контента обьектами из базы

        Args:
            content_name:
                Название контента для заполнения в формате "table", то есть то же имя, что и у файла таблицы БД
        """
        models = self.db.get_all_from("users")
        self.showed_frame.content_panel.destroy()
        self.showed_frame.content_panel = ScrollFrame(self.showed_frame)
        scrollbar = tk.CTkScrollbar
        for model in models:
            user = User(model, self, self.showed_frame.content_panel.scroll_frame)
        self.showed_frame.content_panel.pack(side = tk.TOP,expand = 1, ipadx=450, ipady=155, pady= [0,50])

    def add_user_window(self):
        self.temp_win = tk.CTkToplevel(self.root)
        self.temp_win.title("Добавление пользователя")
        self.temp_win.geometry("450x300")
        self.temp_win_frame = AddUserWindow(self.temp_win,self)
        self.temp_win_frame.create_widgets(self)

    def add_user(self):
        bad_option = ""
        _login = self.temp_win_frame.entry_login.get()
        _passwd = self.temp_win_frame.entry_password.get()
        _role = self.temp_win_frame.role_combo.get()

        if _role == "Клиент":
            _role = "User"
        elif _role == "Специалист":
            _role = "Tech"
        else:
            _role = "Admin"

        if _login == bad_option or _passwd == bad_option or _role == "Выберите...":
            messagebox.showerror("Ошибка!", "Заполните все поля!")
        if self.db.get_all_where("users", "Login", _login):
            messagebox.showerror("Ошибка!", "Такой пользователь уже существует!")
        else:
            self.db.add_record("users", _login + ";" + _passwd+ ";" + _role + ";")
            messagebox.showinfo("Успех", "Пользователь успешно добавлен!")
            self.temp_win.destroy()
            self.show_users()

    def edit_user_window(self, user_model : UserModel):
        self.temp_win = tk.CTkToplevel(self.root)
        self.temp_win.title("Редактирование пользователя")
        self.temp_win.geometry("500x320")
        self.temp_win_frame = UserEditWindow(self.temp_win, self, user_model)
        self.temp_win_frame.create_widgets(self)

    def edit_user(self):
        model = self.temp_win_frame.model
        _login = self.temp_win_frame.entry_login.get()
        _password = self.temp_win_frame.entry_password.get()
        self.db.alter("users", model.id, "Login", _login)
        self.db.alter("users", model.id, "Password", _password)
        messagebox.showinfo("Успех", "Данные пользователя успешно обновлены!")
        self.temp_win.destroy()
        self.show_users()

    def delete_user_dialog(self, userID):
        dialog = tk.CTkInputDialog(text="Введите свой пароль администратора:", title="Проверка")
        passwd = dialog.get_input()
        check = self.db.get_all_where("users", "ID", self.id_user)
        if passwd != check[0].password:
            messagebox.showerror("Ошибка!", "Неправильный пароль!")
        else:
            ans = messagebox.askokcancel("Подтверждение", "Вы действительно хотите удалить аккаунт?\nДанные нельзя будет восстановить!")
            if ans:
                self.db.delete_by_id("users", userID)
                self.temp_win.destroy()
                self.show_users()
            else:
                pass


#       ----------ADMIN----------


#       ----------TECH----------


    def show_requests_list(self):
        models = self.db.get_all_where("requests", "Picked", "Создано")
        self.showed_frame.requests_list.destroy()
        self.showed_frame.requests_list = ScrollFrame(self.showed_frame)
        scrollbar = tk.CTkScrollbar
        for model in models:
            request = Request(model, self, self.showed_frame.requests_list.scroll_frame)
        self.showed_frame.requests_list.pack(side=tk.TOP, expand=1, ipadx=450, ipady=155, pady=[0, 50])

    def show_taken_requests(self):
        self.showed_frame.requests_list.destroy()

    def show_comment_window(self, requests_model : RequestsModel):
        self.temp_win = tk.CTkToplevel(self.root)
        self.temp_win.title("Комментарий заявки")
        self.temp_win.geometry("500x320")
        self.temp_win_frame = CommentWindow(self.temp_win, self, requests_model)
        self.temp_win_frame.create_widgets(self)

    def take_request(self, model):
        check = self.db.get_all_where("requests", "TechID", self.id_user)
        if len(check) == 3:
            messagebox.showerror("Ошибка!", "Превышен лимит заявок!")
        else:

            ans = messagebox.askokcancel("Подтверждение", "Вы действительно хотите взять заявку?")
            if ans:
                self.db.alter("requests", model.id, "Picked", "В процессе")
                self.db.alter("requests", model.id, "TechID", self.id_user)
                messagebox.showinfo("Успех", "Заявка взята!")
                self.show_requests_list()

    def filter_models_tech(self):
        """
        Отфильтровать модели
        :return: отфильтрованные модели
        """
        req_model = self.db.get_all_where("requests", "TechID", self.id_user)
        filt_model = [i for i in req_model if i.pick_flag !="Закрыто"]
        return filt_model

    def update_tech(self):
        request_model = self.filter_models_tech()

        if len(request_model) < 1:
            self.showed_frame.req1_status.configure(text="Отсутствует")
        else:
            self.showed_frame.req1_status.configure(text=request_model[0].pick_flag)
        if self.showed_frame.req1_status.cget("text") != "Отсутствует":
            self.showed_frame.req1_change.configure(state="normal", fg_color="#0cc27c")
        else:
            pass

        if len(request_model) < 2:
            self.showed_frame.req2_status.configure(text="Отсутствует")
        else:
            self.showed_frame.req2_status.configure(text=request_model[1].pick_flag)
        if self.showed_frame.req2_status.cget("text") != "Отсутствует":
            self.showed_frame.req2_change.configure(state="normal", fg_color="#0cc27c")
        else:
            pass

        if len(request_model) < 3:
            self.showed_frame.req3_status.configure(text="Отсутствует")
        else:
            self.showed_frame.req3_status.configure(text=request_model[2].pick_flag)
        if self.showed_frame.req3_status.cget("text") != "Отсутствует":
            self.showed_frame.req3_change.configure(state="normal",fg_color="#0cc27c")
        else:
            pass

    def see_content_tech(self, req_frame : int):
        """
        Просмотреть содержимое заявки.
        :param id: Айдишник конкретной панели
        :return: Нихуя
        """

        request_model = self.filter_models_tech()
        if req_frame == 1:
            if len(request_model) < 1:
                self.showed_frame.info_hardware_answer.configure(text="*Нет информации*")
                self.showed_frame.info_help_answer.configure(text="*Нет информации*")
                self.showed_frame.info_department_answer.configure(text="*Нет информации*")
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", "*Нет информации*")
                self.showed_frame.req1_status.configure(text="Отсутствует")
            else:
                self.showed_frame.info_hardware_answer.configure(text = request_model[0].hard)
                self.showed_frame.info_help_answer.configure(text=request_model[0].help)
                self.showed_frame.info_department_answer.configure(text=request_model[0].department)
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", request_model[0].comment)
                self.showed_frame.req1_status.configure(text=request_model[0].pick_flag)
                if self.showed_frame.req1_status.cget("text") != "Отсутствует":
                    self.showed_frame.req1_change.configure(state="normal", fg_color="#0cc27c")

        if req_frame == 2:
            if len(request_model) < 2:
                self.showed_frame.info_hardware_answer.configure(text="*Нет информации*")
                self.showed_frame.info_help_answer.configure(text="*Нет информации*")
                self.showed_frame.info_department_answer.configure(text="*Нет информации*")
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", "*Нет информации*")
                self.showed_frame.req2_status.configure(text="Отсутствует")
            else:
                self.showed_frame.info_hardware_answer.configure(text=request_model[1].hard)
                self.showed_frame.info_help_answer.configure(text=request_model[1].help)
                self.showed_frame.info_department_answer.configure(text=request_model[1].department)
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", request_model[1].comment)
                self.showed_frame.req2_status.configure(text=request_model[1].pick_flag)
                if self.showed_frame.req2_status.cget("text") != "Отсутствует":
                    self.showed_frame.req2_change.configure(state="normal", fg_color="#0cc27c")

        if req_frame == 3:
            if len(request_model) < 3:
                self.showed_frame.info_hardware_answer.configure(text="*Нет информации*")
                self.showed_frame.info_help_answer.configure(text="*Нет информации*")
                self.showed_frame.info_department_answer.configure(text="*Нет информации*")
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", "*Нет информации*")
                self.showed_frame.req3_status.configure(text="Отсутствует")
            else:
                self.showed_frame.info_hardware_answer.configure(text=request_model[2].hard)
                self.showed_frame.info_help_answer.configure(text=request_model[2].help)
                self.showed_frame.info_department_answer.configure(text=request_model[2].department)
                self.showed_frame.info_comment_answer.delete("0.0", "end")
                self.showed_frame.info_comment_answer.insert("0.0", request_model[2].comment)
                self.showed_frame.req3_status.configure(text=request_model[2].pick_flag)
                if self.showed_frame.req3_status.cget("text") != "Отсутствует":
                    self.showed_frame.req3_change.configure(state="normal", fg_color="#0cc27c")

    def change_status_window(self, but: int):
        self.temp_win = tk.CTkToplevel(self.root)
        self.temp_win.title("Статус заявки")
        self.temp_win.geometry("300x200")
        self.temp_win_frame = ChangeStatusWindow(self.temp_win, self, but)
        self.temp_win_frame.create_widgets(self)

    def change_status(self, but : int):
        request_model = self.db.get_all_where("requests", "TechID", self.id_user)
        if self.temp_win_frame.status_combo.get() == "Выберите...":
            messagebox.showerror("Ошибка!", "Вы не изменили статус!")
        else:
            ans = messagebox.askokcancel("Подтверждение", "Вы действительно хотите сменить статус?")
            if ans:
                messagebox.showinfo("Успех", "Статус заявки обновлён!")
                self.db.alter("requests", request_model[but].id, "Picked", self.temp_win_frame.status_combo.get())
                self.temp_win.destroy()
                self.update_tech()




#       ----------TECH----------

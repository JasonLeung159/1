import tkinter as tk
from login_page import LoginPage
from stu_page import *
from database import Database
from tch_page import *

class AcademicSystemApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Academic System")
        self.geometry("1440x950")
        self.resizable(True, True)
        self.db = Database()
        self.user = None

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, Stu_MenuPage,Course_stu,stu_Attendance,stu_Profile ,TCH_MeanPage,Course_TCH):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        if page != LoginPage:
            frame.update_data()
        if page == stu_Attendance:
            frame.update_date_display(date.today())
        frame.tkraise()

    def show_Courseframe(self, frame_class, *args):
        frame = self.frames[frame_class]
        frame.update_data(*args)
        frame.tkraise()

    def close_database(self):
        self.db.close()

    def set_user(self, user):
        self.user = user
    
    def get_user(self):
        return self.user
    
    def logout(self):
        self.user = None
        print('logout')
        self.show_frame(LoginPage)

    def on_exit(self):
        self.close_database()
        self.destroy()


if __name__ == "__main__":
    app = AcademicSystemApp()
    app.protocol("WM_DELETE_WINDOW", app.on_exit)
    app.mainloop()

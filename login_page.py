import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from database import Database
from user import User
from stu_page import Stu_MenuPage
from tch_page import TCH_MeanPage

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("img/img.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        title_label = tk.Label(self, text="Academic Record System", font=("Arial Bold", 25))
        title_label.pack(pady=45)

        border = tk.LabelFrame(self, text='Login', bg='white', bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=300, pady=225)
        
        username_frame = tk.Frame(border)
        username_frame.pack(pady=25)

        Label1 = tk.Label(username_frame, text="Username 使用者名稱", font=("Arial Bold", 15), highlightbackground='white')
        Label1.pack(side="left")

        self.username_entry = tk.Entry(username_frame, width=25, bd=5)
        self.username_entry.pack(side="left",padx=20)

        password_frame = tk.Frame(border)
        password_frame.pack(pady=25)

        Label2 = tk.Label(password_frame, text="Password 密碼", font=("Arial Bold", 15))
        Label2.pack(side="left")

        self.password_entry = tk.Entry(password_frame, width=25, show='*', bd=5)
        self.password_entry.pack(side="left",padx=20)


        def login():
            #username = 'sophiachen@abcu.edu.hk'
            #password = 'pwd006'
            #username = 'johndoe@abcu.edu.hk'
            #password = 'pwd001'

            #username = '01234567@stu.abcu.edu.hk'
            #password = 'Jacob123'
            username = self.username_entry.get()
            password = self.password_entry.get()
            if username.count('stu') != 0:
                if controller.db.authenticate(username, password) is not None:
                    data = controller.db.authenticate(username, password)
                    studid = data[2]
                    studName = data[3]
                    user = User(studName,studid)
                    controller.set_user(user)
                    controller.show_frame(Stu_MenuPage)
                else:
                    messagebox.showinfo("Error", "Please provide correct username and password!")
            else:
                if controller.db.teacher_authenticate(username, password):
                    data = controller.db.teacher_authenticate(username, password)
                    teacherid = data[2]
                    teacherName = data[3]
                    user = User(teacherName,teacherid)
                    controller.set_user(user)
                    controller.show_frame(TCH_MeanPage)
                else:
                    messagebox.showinfo("Error", "Please provide correct username and password!")


        button_frame = tk.Frame(border)
        button_frame.pack(pady=10,side='bottom')

        login_button = tk.Button(button_frame,text="Enter 登入",bd=1, font=("Arial", 15), command=login,relief='solid')
        login_button.pack()


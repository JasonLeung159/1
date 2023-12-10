import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from database import Database
from datetime import date
from datetime import timedelta
import datetime
import calendar

class Stu_MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        current_date = datetime.datetime.now()
        self.year = current_date.year
        self.month = current_date.month
        self.reminders = {}

        student_name = ''
        self.configure(bg='white')

        style = ttk.Style()
        style.configure("Menu.TButton", foreground="white", background="#333", font=("Helvetica", 12))

        username_frame = tk.Frame(self, bg="#333", height=50)
        username_frame.pack(side="top", fill="x")
        
        self.username_label = tk.Label(username_frame, text='', font=("Helvetica", 12), fg="white", bg="#333")
        self.username_label.pack(side="right", padx=20, pady=10)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(side="top", fill="x")

        menu_frame = tk.Frame(self, bg="#333")
        menu_frame.pack(side="left", fill="y")

        
        menu_label = tk.Label(menu_frame, text="Menu", font=("Helvetica", 14), fg="white", bg="#333")
        menu_label.pack(side="top", padx=5, pady=5)

        line = tk.Frame(menu_frame, height=2, width=200, bg="white")
        line.pack(fill="x", padx=0, pady=10)

        Home_image = Image.open("img/Mainpage.png")
        Home_image = Home_image.resize((24, 24))
        self.Home_icon = ImageTk.PhotoImage(Home_image)

        Course_image = Image.open("img/Course.png")
        Course_image = Course_image.resize((24, 24))
        self.Course_icon = ImageTk.PhotoImage(Course_image)

        Attend_image = Image.open("img/attend.png")
        Attend_image = Attend_image.resize((24, 24))
        self.Attend_icon = ImageTk.PhotoImage(Attend_image)

        Profile_image = Image.open("img/Profile.png")
        Profile_image = Profile_image.resize((24, 24))
        self.Profile_icon = ImageTk.PhotoImage(Profile_image)

        Home_button = ttk.Button(menu_frame, text="Home", image=self.Home_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Stu_MenuPage))
        Home_button.pack(side="top", fill="x", padx=10, pady=5)

        Course_button = ttk.Button(menu_frame, text="Course", image=self.Course_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Course_stu))
        Course_button.pack(side="top", fill="x", padx=10, pady=5)

        Attend_button = ttk.Button(menu_frame, text="Attend", image=self.Attend_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Attendance))
        Attend_button.pack(side="top", fill="x", padx=10, pady=5)

        Profile_button = ttk.Button(menu_frame, text="Profile", image=self.Profile_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Profile))
        Profile_button.pack(side="top", fill="x", padx=10, pady=5)

        Logout_image = Image.open("img/logout_icon.png")
        Logout_image = Logout_image.resize((24, 24))
        self.Logout_icon = ImageTk.PhotoImage(Logout_image)

        logout_button = ttk.Button(menu_frame, text="Logout", image=self.Logout_icon, compound="left", style="Menu.TButton", command=lambda: controller.logout())
        logout_button.pack(side="bottom", fill="x", padx=10, pady=15)

        # main stage
        self.main_stage = tk.Frame(self, bg="white",borderwidth=2,relief="solid")
        self.main_stage.pack(side="left", fill="both", expand=True)

        content_label = tk.Label(self.main_stage, text="Home", font=("Helvetica", 24),bg='white')
        content_label.pack(padx=50, pady=50)
        
        display_frame = tk.Frame(self.main_stage, bg='white')
        display_frame.pack()

        self.prev_button = tk.Button(display_frame, text="Previous", command=self.prev_month)
        self.prev_button.pack(side='left',padx=5)

        month_year_frame = tk.Frame(display_frame, bg='white',borderwidth=2, relief="solid")
        month_year_frame.pack(side='left')
        
        self.label_month = tk.Label(month_year_frame, text=calendar.month_name[self.month], font=("Arial", 16, "bold"),bg='white')
        self.label_month.pack(side='left')

        self.label_year = tk.Label(month_year_frame, text=str(self.year), font=("Arial", 14),bg='white')
        self.label_year.pack(side='left')

        self.next_button = tk.Button(display_frame, text="Next", command=self.next_month)
        self.next_button.pack(side='right',padx=5)

        self.days_labels_frame = tk.Frame(self.main_stage,borderwidth=2, relief="solid")
        self.days_labels_frame.pack(pady=5)

        for day in calendar.weekheader(3).split():
            label = tk.Label(self.days_labels_frame, text=day, font=("Arial", 12, "bold"), width=11,bg='white')
            label.pack(side='left')

        self.calendar_frame = tk.Frame(self.main_stage,borderwidth=2, relief="solid")
        self.calendar_frame.pack()

    def update_data(self):
        self.reminders = {}
        user = self.controller.get_user()
        student_name = user.get_username()
        self.fetch_reminders_from_database()
        self.update_calendar()

        self.username_label.configure(text=student_name)
    def fetch_reminders_from_database(self):
        student_id = self.controller.get_user().get_userID()
        rows = self.controller.db.time_table(student_id)

        for row in rows:
            date = row[0].strftime("%Y-%m-%d")
            course_code = row[1]
            course_group = row[2]
            reminder = f"{course_code}"
            
            day_month = date.split('-')[2] + '-' + date.split('-')[1]
            if day_month not in self.reminders:
                self.reminders[day_month] = []
        
            self.reminders[day_month].append(reminder)
        

    def update_calendar(self):
        self.label_month.configure(text=calendar.month_name[self.month])
        self.label_year.configure(text=str(self.year))

        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        cal = calendar.monthcalendar(self.year, self.month)
    
        for week in cal:
            week_frame = tk.Frame(self.calendar_frame,bg='white')
            week_frame.pack()

            for day in week:
                if day != 0:
                    day_frame = tk.Frame(week_frame,bg='white')
                    day_frame.pack(side=tk.LEFT)

                    label = tk.Label(day_frame, text=str(day), font=("Arial", 14), width=10,bg='white')
                    label.pack()

                    day_month = f"{day:02d}-{self.month:02d}"

                    if day_month in self.reminders:
                        for reminder in self.reminders[day_month]:
                            reminder_label = tk.Label(day_frame, text=reminder, font=("Arial", 8), fg="red",bg='white')
                            reminder_label.pack()
                    else:
                        reminder_label = tk.Label(day_frame, text=" ", font=("Arial", 8),bg='white')
                        reminder_label.pack()
                else:
                    label = tk.Label(week_frame, text=" ", font=("Arial", 14), width=10,bg='white')
                    label.pack(side=tk.LEFT)

    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1

        self.reminders = {}
        self.fetch_reminders_from_database()
        self.update_calendar()

    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.reminders = {}
        self.fetch_reminders_from_database()
        self.update_calendar()

        

class Course_stu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        student_name = ''
        
        style = ttk.Style()
        style.configure("Menu.TButton", foreground="white", background="#333", font=("Helvetica", 12))

        username_frame = tk.Frame(self, bg="#333", height=50)
        username_frame.pack(side="top", fill="x")
        
        self.username_label = tk.Label(username_frame, text='', font=("Helvetica", 12), fg="white", bg="#333")
        self.username_label.pack(side="right", padx=20, pady=10)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(side="top", fill="x")

        menu_frame = tk.Frame(self, bg="#333")
        menu_frame.pack(side="left", fill="y")

        menu_label = tk.Label(menu_frame, text="Menu", font=("Helvetica", 14), fg="white", bg="#333")
        menu_label.pack(side="top", padx=5, pady=5)

        line = tk.Frame(menu_frame, height=2, width=200, bg="white")
        line.pack(fill="x", padx=0, pady=10)

        Home_image = Image.open("img/Mainpage.png")
        Home_image = Home_image.resize((24, 24))
        self.Home_icon = ImageTk.PhotoImage(Home_image)

        Course_image = Image.open("img/Course.png")
        Course_image = Course_image.resize((24, 24))
        self.Course_icon = ImageTk.PhotoImage(Course_image)

        Attend_image = Image.open("img/attend.png")
        Attend_image = Attend_image.resize((24, 24))
        self.Attend_icon = ImageTk.PhotoImage(Attend_image)

        Profile_image = Image.open("img/Profile.png")
        Profile_image = Profile_image.resize((24, 24))
        self.Profile_icon = ImageTk.PhotoImage(Profile_image)

        Home_button = ttk.Button(menu_frame, text="Home", image=self.Home_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Stu_MenuPage))
        Home_button.pack(side="top", fill="x", padx=10, pady=5)

        Course_button = ttk.Button(menu_frame, text="Course", image=self.Course_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Course_stu))
        Course_button.pack(side="top", fill="x", padx=10, pady=5)

        Attend_button = ttk.Button(menu_frame, text="Attend", image=self.Attend_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Attendance))
        Attend_button.pack(side="top", fill="x", padx=10, pady=5)

        Profile_button = ttk.Button(menu_frame, text="Profile", image=self.Profile_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Profile))
        Profile_button.pack(side="top", fill="x", padx=10, pady=5)

        Logout_image = Image.open("img/logout_icon.png")
        Logout_image = Logout_image.resize((24, 24))
        self.Logout_icon = ImageTk.PhotoImage(Logout_image)

        logout_button = ttk.Button(menu_frame, text="Logout", image=self.Logout_icon, compound="left", style="Menu.TButton", command=lambda: controller.logout())
        logout_button.pack(side="bottom", fill="x", padx=10, pady=15)

        # main stage
        self.main_stage = tk.Frame(self, bg="white")
        self.main_stage.pack(side="left", fill="both", expand=True)

        content_label = tk.Label(self.main_stage, text="Course", font=("Helvetica", 24))
        content_label.pack(padx=50, pady=50)


    def update_data(self):
        user = self.controller.get_user()
        student_name = user.get_username()

        self.username_label.configure(text=student_name)

        db = Database()
        student_id = self.controller.get_user().get_userID()
        result = db.student_course(student_id)
        db.close()

        if self.main_stage.winfo_children():
            for widget in self.main_stage.winfo_children():
                widget.destroy()


        content_frame = tk.Frame(self.main_stage,bg='white')
        content_frame.pack()

        content_label = tk.Label(content_frame, text="Course", font=("Helvetica", 24),bg='white')
        content_label.pack(padx=50, pady=50)

        contain_header_frame = tk.Frame(content_frame, bg="white")
        contain_header_frame.pack(side='top',fill="x", padx=10, pady=2)
        
        header_frame = tk.Frame(contain_header_frame, bg="white")
        header_frame.pack(fill="x", padx=10, pady=5)

        course_code_header = tk.Label(header_frame, text="CourseCode", font=("Helvetica", 12), width=15,bg='white')
        course_code_header.pack(side="left", padx=(10, 5))

        course_title_header = tk.Label(header_frame, text="CourseTitle", font=("Helvetica", 12), width=40,bg='white')
        course_title_header.pack(side="left", padx=(0, 5))

        line = tk.Frame(contain_header_frame, height=2, width=240, bg="black")
        line.pack(side="top",fill="x", padx=0, pady=3)
        if result:
            for row in result:
                # main stage
                
                
                course_frame = tk.Frame(contain_header_frame, bg="white", pady=10)
                course_frame.pack(fill="x", padx=10, pady=5)

                course_code_label = tk.Label(course_frame, text=row[0], font=("Helvetica", 12), width=15,bg='white')
                course_code_label.pack(side="left", padx=(10, 5))

                course_title_label = tk.Label(course_frame, text=row[1], font=("Helvetica", 12), width=40,bg='white')
                course_title_label.pack(side="left", padx=(0, 5))

                button_frame = tk.Frame(course_frame, bg="white")
                button_frame.pack(side="left")

                view_button = tk.Button(button_frame, text="View", font=("Helvetica", 12), command=lambda code=row[0]: self.show_course_page(code,row[1]))
                view_button.pack(padx=(0, 10))

    def go_back_to_course_page(self):
        self.controller.show_frame(Course_stu)

    def show_course_page(self, course_code,course_title):

        if self.main_stage.winfo_children():
            for widget in self.main_stage.winfo_children():
                widget.destroy()

        def navigate_to_Attendance_page():
            
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10,bg="white")
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,bg="white")
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")
            
            
            back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=(10,0))
            Title = tk.Label(topline, text='My Attendance', font=("Helvetica", 16), pady=10,bg='white')
            Title.pack()

            content_frame = tk.Frame(self.main_stage,bg='white')
            content_frame.pack()
            
            # Student can check the attendance in this page
            # add code here
            student_id = self.controller.get_user().get_userID()
            data = self.controller.db.check_course_attend(student_id,course_code)

            contain_header_frame = tk.Frame(content_frame, bg="white")
            contain_header_frame.pack(side='top',fill="x", padx=10, pady=2)
            
            header_frame = tk.Frame(contain_header_frame, bg="white")
            header_frame.pack(fill="x", padx=10, pady=5)

            EventName_header = tk.Label(header_frame, text="EventName", width=15,bg="white")
            EventName_header.pack(side="left", padx=(10, 0))

            Date_header = tk.Label(header_frame, text="Date", width=15,bg="white")
            Date_header.pack(side="left", padx=(0, 0))

            Time_header = tk.Label(header_frame, text="Time", width=15,bg="white")
            Time_header.pack(side="left", padx=(0, 0))

            line = tk.Frame(contain_header_frame, height=2, bg="black")
            line.pack(side="top",fill="x", padx=0, pady=3)
            if data:
                i = 0
                for row in data:
                    # main stage
                    if i == 1:
                        result_frame = tk.Frame(contain_header_frame, bg="white", pady=5)
                        result_frame.pack(fill="x", padx=10, pady=1)

                        course_type_label = tk.Label(result_frame, text=row[1],  width=15)
                        course_type_label.pack(side="left", padx=(10, 0))

                        Date_label = tk.Label(result_frame, text=row[2], width=15)
                        Date_label.pack(side="left", padx=(0, 0))
                        Time_label = tk.Label(result_frame, text=row[3],  width=15)
                        Time_label.pack(side="left", padx=(0, 0))
                        i = 0
                    else:
                        result_frame = tk.Frame(contain_header_frame, bg="white", pady=5)
                        result_frame.pack(fill="x", padx=10, pady=1)

                        course_type_label = tk.Label(result_frame, text=row[1],  width=15,bg="white")
                        course_type_label.pack(side="left", padx=(10, 0))

                        Date_label = tk.Label(result_frame, text=row[2], width=15,bg="white")
                        Date_label.pack(side="left", padx=(0, 0))
                        Time_label = tk.Label(result_frame, text=row[3],  width=15,bg="white")
                        Time_label.pack(side="left", padx=(0, 0))
                        i =+ 1


        def navigate_to_GPA_page():
            student_id = self.controller.get_user().get_userID()
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10, bg="white")
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,  bg="white")
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")

            back_frame = tk.Frame(topline, bg="white")
            back_frame.pack(fill="x", padx=10, pady=5)
            
            back_button = tk.Button(back_frame, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=10)

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack(fill="x", padx=10, pady=5)

            
            # student can view their GPA in this page
            # add code here
            
            data = self.controller.db.get_student_thier_GPA(student_id,course_code)

            if data:
                Title_label = tk.Label(topline, text='My GPA', font=("Helvetica", 16), pady=10,bg='white')
                Title_label.pack()

                GPA_Result_frame = tk.Frame(self.main_stage, bg="white",borderwidth=1, relief="solid")
                GPA_Result_frame.pack(side='top')

                
                result_line_left = tk.Frame(GPA_Result_frame, bg="white")
                result_line_left.pack(side = 'left')

                Course_label = tk.Label(result_line_left, text= ' Course : ', font=("Helvetica", 16), pady=10,bg='white')
                Course_label.pack(side='left',pady = (30,180), padx=10)

                result_Course_label = tk.Label(result_line_left, text= course_code +' '+course_title, font=("Helvetica", 16), pady=10,bg='white')
                result_Course_label.pack(side='left',pady = (30,180), padx=10)
                
     

                result_line_right = tk.Frame(GPA_Result_frame, bg="white")
                result_line_right.pack(side = 'top')

                Coures_Grade_label = tk.Label(result_line_right, text='Grade : ', font=("Helvetica", 16), pady=10,bg='white')
                Coures_Grade_label.pack(side='left',pady = (30,100),padx= (20,10))

                

                result_Coures_Grade_label = tk.Label(result_line_right, text=data[0][2], font=("Helvetica", 16), pady=10,bg='white')
                result_Coures_Grade_label.pack(side='right',pady = (30,100),padx= (20,10))
                


                right_corner = tk.Frame(GPA_Result_frame,bg="white")
                right_corner.pack(side='bottom')

                Student_ID_label =tk.Label(right_corner, text='Student ID : ', pady=10,bg='white')
                Student_ID_label.pack(side='left',pady = (30,0),padx= (20,0))
                
                student_ID = tk.Label(right_corner, text= data[0][0], pady=10,bg='white')
                student_ID.pack(side='left',pady = (30,0),padx= (0,10))

                Student_name_label =tk.Label(right_corner, text='Student Name : ', pady=10,bg='white')
                Student_name_label.pack(side='left',pady = (30,0),padx= (20,0))
                
                student_name = tk.Label(right_corner, text= data[0][1], pady=10,bg='white')
                student_name.pack(side='left',pady = (30,0),padx= (0,10))
            else:
                content_label = tk.Label(content_frame, text="Your GPA is not allowed to be viewed", font=("Helvetica", 14))
                content_label.pack(padx=50, pady=50)

            
        courseheader_frame = tk.Frame(self.main_stage, bg="white")
        courseheader_frame.pack(fill="x", padx=10, pady=5)

        inner_frame = tk.Frame(courseheader_frame, bg="white")
        inner_frame.pack()

        course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10, bg="white")
        course_code_label.pack(side="left", padx=(0, 1),pady=20)

        course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10, bg="white")
        course_title_label.pack(side="left")

        line = tk.Frame(self.main_stage, height=2, bg="black")
        line.pack(side="top",fill="x", padx=0, pady=3)
        
        course_function_frame = tk.Frame(self.main_stage, bg="white")
        course_function_frame.pack(side='top' ,padx=40, pady=5)

        left_frame = tk.Frame(course_function_frame, bg="white")
        left_frame.pack(side='left', padx=40, pady=5)

        attendance_Course_image = Image.open("img/Attendance.png")
        attendance_Course_image = attendance_Course_image.resize((200, 200))
        self.attendance_icon = ImageTk.PhotoImage(attendance_Course_image)

        Attend_button = tk.Button(left_frame, image=self.attendance_icon,command=navigate_to_Attendance_page,bd=0)
        Attend_button.pack(side="left", padx=10)

        right_frame = tk.Frame(course_function_frame, bg="white")
        right_frame.pack( side='right', padx=40, pady=5)

        GPA_image = Image.open("img/GPA.png")
        GPA_image = GPA_image.resize((200, 200))
        self.GPA_icon = ImageTk.PhotoImage(GPA_image)

        GPA_button = tk.Button(right_frame,image=self.GPA_icon,command=navigate_to_GPA_page,bd=0)
        GPA_button.pack(side="right", padx=10)

        
class stu_Attendance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        student_name = ''
        self.configure(bg='white')
        self.date = date.today()
        
        self.courses = []

        style = ttk.Style()
        style.configure("Menu.TButton", foreground="white", background="#333", font=("Helvetica", 12))

        username_frame = tk.Frame(self, bg="#333", height=50)
        username_frame.pack(side="top", fill="x")
        
        self.username_label = tk.Label(username_frame, text='', font=("Helvetica", 12), fg="white", bg="#333")
        self.username_label.pack(side="right", padx=20, pady=10)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(side="top", fill="x")

        menu_frame = tk.Frame(self, bg="#333")
        menu_frame.pack(side="left", fill="y")

        
        menu_label = tk.Label(menu_frame, text="Menu", font=("Helvetica", 14), fg="white", bg="#333")
        menu_label.pack(side="top", padx=5, pady=5)

        line = tk.Frame(menu_frame, height=2, width=200, bg="white")
        line.pack(fill="x", padx=0, pady=10)

        Home_image = Image.open("img/Mainpage.png")
        Home_image = Home_image.resize((24, 24))
        self.Home_icon = ImageTk.PhotoImage(Home_image)

        Course_image = Image.open("img/Course.png")
        Course_image = Course_image.resize((24, 24))
        self.Course_icon = ImageTk.PhotoImage(Course_image)

        Attend_image = Image.open("img/attend.png")
        Attend_image = Attend_image.resize((24, 24))
        self.Attend_icon = ImageTk.PhotoImage(Attend_image)

        Profile_image = Image.open("img/Profile.png")
        Profile_image = Profile_image.resize((24, 24))
        self.Profile_icon = ImageTk.PhotoImage(Profile_image)

        Home_button = ttk.Button(menu_frame, text="Home", image=self.Home_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Stu_MenuPage))
        Home_button.pack(side="top", fill="x", padx=10, pady=5)

        Course_button = ttk.Button(menu_frame, text="Course", image=self.Course_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Course_stu))
        Course_button.pack(side="top", fill="x", padx=10, pady=5)

        Attend_button = ttk.Button(menu_frame, text="Attend", image=self.Attend_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Attendance))
        Attend_button.pack(side="top", fill="x", padx=10, pady=5)

        Profile_button = ttk.Button(menu_frame, text="Profile", image=self.Profile_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Profile))
        Profile_button.pack(side="top", fill="x", padx=10, pady=5)

        Logout_image = Image.open("img/logout_icon.png")
        Logout_image = Logout_image.resize((24, 24))
        self.Logout_icon = ImageTk.PhotoImage(Logout_image)

        logout_button = ttk.Button(menu_frame, text="Logout", image=self.Logout_icon, compound="left", style="Menu.TButton", command=lambda: controller.logout())
        logout_button.pack(side="bottom", fill="x", padx=10, pady=15)

        # main stage
        self.main_stage = tk.Frame(self, bg="white")
        self.main_stage.pack(side="left", fill="both", expand=True)

        tick_image = Image.open("img/check.png")
        tick_image = tick_image.resize((24, 24))
        self.tick_icon = ImageTk.PhotoImage(tick_image)
        
        content_label = tk.Label(self.main_stage, text="Attendance", font=("Helvetica", 24),bg='white')
        content_label.pack(padx=50, pady=15)

        arrow_frame = tk.Frame(self.main_stage)
        arrow_frame.pack(pady=5)

        left_arror_image = Image.open("img/arrow_left_circle_icon_128950.png")
        left_arror_image = left_arror_image.resize((24, 24))
        self.left_arror_icon = ImageTk.PhotoImage(left_arror_image)

        right_arror_image = Image.open("img/right-arrow.png")
        right_arror_image = right_arror_image.resize((24, 24))
        self.right_arror_icon = ImageTk.PhotoImage(right_arror_image)

        left_arrow = tk.Button(arrow_frame, text="" ,image=self.left_arror_icon, compound="left", command=lambda: self.previous_date())
        left_arrow.pack(side="left", padx=5, pady=5)
        
        self.date_label = tk.Label(arrow_frame, text='', font=("Helvetica", 12))
        self.date_label.pack(side="left",padx=5, pady=5)

        right_arrow = tk.Button(arrow_frame, text="" , image=self.right_arror_icon,compound="right", command=lambda: self.next_date())
        right_arrow.pack(side="right", padx=5, pady=5)

        self.course_boxes = []
        
       
        self.take_attendance_button = tk.Button(self.main_stage, fg="black", bg="grey", text="Take Attendance",font=("Arial", 16))
        self.take_attendance_button.config(state="disabled")
        self.take_attendance_button.pack(side='bottom', pady=(10,20))
        
    def update_data(self):
        user = self.controller.get_user()
        student_name = user.get_username()
        student_id = user.get_userID()


        self.username_label.configure(text=student_name)
        courses = self.controller.db.get_courses_for_date(student_id,self.date)

    def previous_date(self):
        self.date = self.date - timedelta(days=1)
        self.update_date_display(self.date)

    def next_date(self):
        self.date = self.date + timedelta(days=1)
        self.update_date_display(self.date)

    def update_date_display(self,date):
        formatted_date = date.strftime('%Y-%m-%d')
        self.date_label.configure(text=formatted_date)
        student_id = self.controller.get_user().get_userID()
        self.date = date
        self.courses = self.controller.db.get_courses_for_date(student_id,self.date)
        self.display_courses()

    def display_courses(self):
        for box in self.course_boxes:
            box.destroy()
            
        self.course_boxes = []
        if len(self.courses) != 0:
            for course in self.courses:
                course_box = tk.Frame(self.main_stage,bg='white')
                course_box.pack(side="top", fill="both",pady=10)

                date_frame = tk.LabelFrame(course_box, padx=10,pady=2, bg="white")
                date_frame.pack(fill="x",padx=200)
                
                start_time_str = str(course[3])[:-3]
                end_time_str = str(course[4])[:-3]
                start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
                end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
                Now = datetime.datetime.now().time()
                Today = datetime.datetime.now().date()

                student_id = self.controller.get_user().get_userID()
                goingline = tk.Frame(date_frame ,bg='white')
                goingline.pack(fill="x")

                if self.controller.db.check_attend(student_id,self.date,course[0]):
                    icon_label = tk.Label(goingline, image=self.tick_icon,bg='white')
                    icon_label.pack(side='right')
                
                if start_time <= Now <= end_time and course[2] == Today:
                    Going_On_label = tk.Label(goingline, text="On-Going", fg="white", bg="green", font=("Arial", 12))
                    Going_On_label.pack(side="top", fill="x", pady=4)
                else :
                    pass

                class_frame = tk.LabelFrame(date_frame, padx=10, pady=10, font=("Arial", 16), bg="#f2f2f2")
                class_frame.pack(pady=5,fill="x")

                left_frame = tk.LabelFrame(class_frame, padx=10, pady=10, font=("Arial", 12), bg="#f2f2f2",borderwidth=0, highlightthickness=0)
                left_frame.pack(side='left',fill="x",pady=5)

                class1 = tk.Label(left_frame, text=course[0], font=("Arial", 14))
                class1.pack(padx=20,fill="x",pady=7)
                class2 = tk.Label(left_frame, text=course[6],  font=("Arial", 14))
                class2.pack(padx=20,fill="x",pady=7)

                right_frame = tk.LabelFrame(class_frame, pady=10, font=("Arial", 16), bg="#f2f2f2")
                right_frame.pack(side='right',fill="x",pady=4)

                lineone_frame = tk.Frame(right_frame)
                lineone_frame.pack(fill="x")
                
                time = str(course[3])
                time2 = str(course[4])
                class3 = tk.Label(lineone_frame, text="Time : ",font= 14)
                class3.pack(side='left',padx=10)
                class3 = tk.Label(lineone_frame, text=str(course[3]) + " - " + str(course[4]),font= 14)
                class3.pack(side='left',padx=10)

                line = tk.Frame(right_frame, height=1, bg="green")
                line.pack(fill="x", padx=0, pady=4)

                linetwo_frame = tk.Frame(right_frame)
                linetwo_frame.pack(fill="x")
                class4 = tk.Label(linetwo_frame, text="Group : ",font= 14)
                class4.pack(side='left',padx=10)
                class4 = tk.Label(linetwo_frame, text=course[1],font=14)
                class4.pack(side='left',padx=10)

                line = tk.Frame(right_frame, height=1, bg="green")
                line.pack(fill="x", padx=0, pady=4)

                linethree_frame = tk.Frame(right_frame)
                linethree_frame.pack(fill="x")
                class4 = tk.Label(linethree_frame, text="Venue : ",font= 14)
                class4.pack(side='left',padx=10)
                class4 = tk.Label(linethree_frame, text=course[5],font=14)
                class4.pack(side='left',padx=10)
                
                if course[2] == Today and start_time <= Now <= end_time:
                    self.take_attendance_button.config(state="normal")
                    self.take_attendance_button.configure(fg="white", bg="green")
                    self.take_attendance_button.configure(command=lambda: self.take_attendance(course[0],course[1]))
                else:
                    self.take_attendance_button.config(state="disabled")
                    self.take_attendance_button.configure(bg="grey",fg='black')
                self.course_boxes.append(course_box)


        else:
            self.take_attendance_button.config(state="disabled")
            self.take_attendance_button.configure(bg="grey",fg='black')


    def take_attendance(self,CourseCode,Group_type):
        student_id = self.controller.get_user().get_userID()
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.strftime("%H:%M:%S")
        if not self.controller.db.check_attend(student_id,current_date,CourseCode):
            self.controller.db.take_attendance(student_id,current_date,current_time,CourseCode,Group_type)
        else:
            pass
        self.controller.show_frame(stu_Attendance) 



class stu_Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.editable = False
        self.form_visible = False

       
        student_name = ''
        self.configure(bg='white')

        style = ttk.Style()
        style.configure("Menu.TButton", foreground="white", background="#333", font=("Helvetica", 12))

        username_frame = tk.Frame(self, bg="#333", height=50)
        username_frame.pack(side="top", fill="x")
        
        self.username_label = tk.Label(username_frame, text='', font=("Helvetica", 12), fg="white", bg="#333")
        self.username_label.pack(side="right", padx=20, pady=10)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(side="top", fill="x")

        menu_frame = tk.Frame(self, bg="#333")
        menu_frame.pack(side="left", fill="y")

        menu_label = tk.Label(menu_frame, text="Menu", font=("Helvetica", 14), fg="white", bg="#333")
        menu_label.pack(side="top", padx=5, pady=5)

        line = tk.Frame(menu_frame, height=2, width=200, bg="white")
        line.pack(fill="x", padx=0, pady=10)

        Home_image = Image.open("img/Mainpage.png")
        Home_image = Home_image.resize((24, 24))
        self.Home_icon = ImageTk.PhotoImage(Home_image)

        Course_image = Image.open("img/Course.png")
        Course_image = Course_image.resize((24, 24))
        self.Course_icon = ImageTk.PhotoImage(Course_image)

        Attend_image = Image.open("img/attend.png")
        Attend_image = Attend_image.resize((24, 24))
        self.Attend_icon = ImageTk.PhotoImage(Attend_image)

        Profile_image = Image.open("img/Profile.png")
        Profile_image = Profile_image.resize((24, 24))
        self.Profile_icon = ImageTk.PhotoImage(Profile_image)

        Home_button = ttk.Button(menu_frame, text="Home", image=self.Home_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Stu_MenuPage))
        Home_button.pack(side="top", fill="x", padx=10, pady=5)

        Course_button = ttk.Button(menu_frame, text="Course", image=self.Course_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Course_stu))
        Course_button.pack(side="top", fill="x", padx=10, pady=5)

        Attend_button = ttk.Button(menu_frame, text="Attend", image=self.Attend_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Attendance))
        Attend_button.pack(side="top", fill="x", padx=10, pady=5)

        Profile_button = ttk.Button(menu_frame, text="Profile", image=self.Profile_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(stu_Profile))
        Profile_button.pack(side="top", fill="x", padx=10, pady=5)

        Logout_image = Image.open("img/logout_icon.png")
        Logout_image = Logout_image.resize((24, 24))
        self.Logout_icon = ImageTk.PhotoImage(Logout_image)

        logout_button = ttk.Button(menu_frame, text="Logout", image=self.Logout_icon, compound="left", style="Menu.TButton", command=lambda: controller.logout())
        logout_button.pack(side="bottom", fill="x", padx=10, pady=15)

        # main stage
        self.main_stage = tk.Frame(self, bg="white")
        self.main_stage.pack(side="left", fill="both", expand=True)
        
        content_label = tk.Label(self.main_stage, text="Profile", font=("Helvetica", 24),bg = 'white')
        content_label.pack(padx=50, pady=(50,30))

        line = tk.Frame(self.main_stage, height=2, width=240, bg="black")
        line.pack(side="top",fill="x", padx=0, pady=(0,20))

        self.title_label = tk.Label(self.main_stage,text='Personal Info :',font=("Helvetica", 14), justify=tk.LEFT ,bg = 'white')
        self.title_label.pack(pady=2)
        

        self.profile_label = tk.Label(self.main_stage,font=(12), justify=tk.LEFT)
        self.profile_label.pack(pady=(1,10))

        self.show_form_button = tk.Button(self.main_stage, text="Show", command=self.toggle_edit_form)
        self.show_form_button.pack(pady=10)

        self.form_frame = tk.Frame(self.main_stage,bg="white",borderwidth=2, relief="solid",padx=30,pady=10)
        self.form_frame.pack(pady=10)



    def validate_input_name(self,value):
        if all(char.isalpha() or char.isspace() for char in value) or value == "":
            return True
        else:
            return False

    def validate_input_age(self,value):
        try:
            # don't let the input be alphabet
            if len(value) > 0:
                int(value)
            # limit the age under 2 length
            if len(value) <= 2:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_phone_number(self,value):
        try:
            int(value)
            if len(value) <= 8:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def update_data(self):
        if self.form_frame:
            self.editable = False
            self.form_visible = False
            self.form_frame.destroy()
            
        user = self.controller.get_user()
        student_name = user.get_username()
        student_id = self.controller.get_user().get_userID()

        
        Info = self.controller.db.get_pesonal_info(student_id)

        self.name = Info[0][1]
        self.ID = Info[0][0]
        self.age = Info[0][3]
        self.gender = Info[0][4]
        self.year = Info[0][2]
        self.SpLD = Info[0][6]
        self.phonenum = Info[0][5]
        self.editable = False


        self.display_student_profile()
        self.username_label.configure(text=student_name)

        self.form_frame = tk.Frame(self.main_stage,bg="white",borderwidth=2, relief="solid",padx=30,pady=10)
        self.form_frame.pack(pady=10)

        
        button_frame = tk.Frame(self.form_frame,bg="white")
        button_frame.pack()

        left_button =tk.Frame(button_frame,bg="white")
        left_button.pack(side='left',padx=5)

        right_button = tk.Frame(button_frame,bg="white")
        right_button.pack(side='right',padx=5)
                
        self.edit_button = tk.Button(left_button, text="edit", command=self.edit_student_profile)
        self.edit_button.pack()

        self.submit_button = tk.Button(right_button, text="submit", command=self.submit_student_profile, state=tk.DISABLED)
        self.submit_button.pack(pady=10)

        title_form = tk.Label(self.form_frame,text='Edit Form :',font=("Helvetica", 14), justify=tk.LEFT ,bg = 'white')
        title_form.pack(pady=2)

        ID_label = tk.Label(self.form_frame, text="Student ID:")
        ID_label.pack()
        self.ID_entry = tk.Entry(self.form_frame, state=tk.NORMAL)
        self.ID_entry.insert(0,self.ID)
        self.ID_entry.pack(pady=10)
        self.ID_entry.configure(state=tk.DISABLED)

        name_label = tk.Label(self.form_frame, text="Student name:")
        name_label.pack()
        self.name_entry = tk.Entry(self.form_frame, state=tk.NORMAL)
        self.name_entry.insert(0,self.name)
        self.name_entry.pack(pady=10)
        self.name_entry.configure(state=tk.DISABLED)
        validate_Name = (self.form_frame.register(self.validate_input_name), '%P')
        self.name_entry.configure(validate='key', validatecommand=validate_Name)



        age_label = tk.Label(self.form_frame, text="Age:")
        age_label.pack()
        self.age_entry = tk.Entry(self.form_frame, state=tk.NORMAL)
        self.age_entry.insert(0,self.age)
        self.age_entry.pack(pady=10)
        self.age_entry.configure(state=tk.DISABLED)
        validate_age = (self.form_frame.register(self.validate_input_age), '%P')
        self.age_entry.configure(validate='key', validatecommand=validate_age)
        

        phonenum_label = tk.Label(self.form_frame, text="Phone Number:")
        phonenum_label.pack()
        self.phonenum_entry = tk.Entry(self.form_frame, state=tk.NORMAL)
        self.phonenum_entry.insert(0,self.phonenum)
        self.phonenum_entry.pack(pady=10)
        self.phonenum_entry.configure(state=tk.DISABLED)
        validate_phoneNum = (self.form_frame.register(self.validate_phone_number), '%P')
        self.phonenum_entry.configure(validate='key', validatecommand=validate_phoneNum)
        


        SpLD_label = tk.Label(self.form_frame, text="Specific Learning Difficulty:")
        SpLD_label.pack()
    
        spld_list = ["Dyslexia", "Dysgraphia", "Dyscalculia", "ADHD", "SLI", "APD", "Visual Processing Disorder",'None']
        count = 0
        for i in spld_list:
            count += 1
            if i.lower() == self.SpLD.lower():
                count -= 1
                break
        self.selected_spld = tk.StringVar(value = spld_list[count])
        self.spld_dropdown = ttk.Combobox(self.form_frame,textvariable=self.selected_spld,state=tk.NORMAL)
        self.spld_dropdown['values'] = spld_list
        self.spld_dropdown.pack()
        self.spld_dropdown.configure(state=tk.DISABLED)

        

        self.form_frame.pack_forget()

    def display_profile(self):
        profile_text = f"Student Name: {self.name}\nStudent ID : {self.ID}\nAge: {self.age}\nGender : {self.gender}\nPhone Number : {self.phonenum} \n Year : {self.year}\nSpecific Learning Difficulty : {self.SpLD}"
        return profile_text

    def edit_profile(self):
        if self.editable == False:
            self.editable = True
        else:
            self.editable = False
    def toggle_edit_form(self):
        if self.form_visible:
            self.form_frame.pack_forget()
            self.form_visible = False
            self.show_form_button.configure(text="Show")
        else:
            self.form_frame.pack()
            self.form_visible = True
            self.show_form_button.configure(text="Hide")

    def toggle_edit_mode(self):
        if not self.editable:
            self.editable = False
            self.edit_button.configure(text="edit")
            self.submit_button.configure(state=tk.DISABLED)
            self.disable_entry_fields()  
        else:
            self.editable = True
            self.edit_button.configure(text="cancel")
            self.submit_button.configure(state=tk.NORMAL)
            self.enable_entry_fields()
    def enable_entry_fields(self):
        self.name_entry.configure(state=tk.NORMAL)
        self.age_entry.configure(state=tk.NORMAL)
        self.phonenum_entry.configure(state=tk.NORMAL)
        self.spld_dropdown.configure(state=tk.NORMAL)
        
    def disable_entry_fields(self):
        self.name_entry.configure(state=tk.DISABLED)
        self.age_entry.configure(state=tk.DISABLED)
        self.phonenum_entry.configure(state=tk.DISABLED)
        self.spld_dropdown.configure(state=tk.DISABLED)
        
    def display_student_profile(self):
        profile_text =  self.display_profile()
        self.profile_label.configure(text=profile_text)

    def edit_student_profile(self):
        self.edit_profile()
        self.toggle_edit_mode()
        

    def submit_student_profile(self):
        name = self.name_entry.get()
        ID = self.ID_entry.get()
        age = self.age_entry.get()
        PhoneNum = self.phonenum_entry.get()
        SpLD = self.selected_spld.get()
        
        if not 18 <= int(age) <= 40:
            messagebox.showerror("Error", "Your age is wrong !")

        elif len(PhoneNum) != 8:
            messagebox.showerror("Error", "Your PhoneNumber is wrong !")

        else:
            self.controller.db.update_personal_info(ID,name,age,SpLD,PhoneNum)
            self.controller.show_frame(stu_Profile)
        

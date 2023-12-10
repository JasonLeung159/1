import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from database import Database
from tkinter import simpledialog
from tkcalendar import Calendar
from datetime import datetime, time

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, course_code, controller):
        self.coursecode = course_code
        self.controller = controller
        super().__init__(parent)
    def body(self, master):
        Event_frame = tk.Frame(master)
        Event_frame.pack()
        tk.Label(Event_frame, text="Group: ").pack(side='left')
        group_options = ['Lecture','Laboratory']
        self.group_combobox = ttk.Combobox(Event_frame, values=group_options)
        self.group_combobox.pack(side='left',pady=3)
        

        Venue_frame = tk.Frame(master)
        Venue_frame.pack()
        tk.Label(Venue_frame, text="Venue: ").pack(side='left')
        venue_options = ['Lecture Hall A','Lab 101','Lecture Hall B','Lab 102','Lecture Hall C','Lab 103','Lecture Hall D','Lab 104']
        self.venue_combobox = ttk.Combobox(Venue_frame, values=venue_options)
        self.venue_combobox.pack(side='left',pady=3)

        date_frame = tk.Frame(master)
        date_frame.pack()
        tk.Label(date_frame, text="Date: ").pack(side='left')
        self.date_entry = tk.Entry(date_frame)
        self.date_entry.pack(side='left',pady=2)
        
        Calendar_image = Image.open("img/calendar_icon.png")
        Calendar_image = Calendar_image.resize((24, 24))
        self.Calendar_icon = ImageTk.PhotoImage(Calendar_image)
        
        self.calendar_button = tk.Button(date_frame, image=self.Calendar_icon, command=self.open_calendar)
        self.calendar_button.pack(side='left',padx=3)
        time_frame = tk.Frame(master)
        time_frame.pack()
        tk.Label(time_frame, text="Time: ").pack(side='left')

        time_options = [f"{hour:02}:00" for hour in range(0, 24)]
        self.time_combobox = ttk.Combobox(time_frame, values=self.get_time_values(),width = 10)
        self.time_combobox.pack(side='left',padx=3)
        tk.Label(time_frame, text=" to ").pack(side='left')
        self.time_combobox2 = ttk.Combobox(time_frame, values=self.get_time_values(),width = 10)
        self.time_combobox2.pack(side='left',padx=3)

    def apply(self):
        venue = self.venue_combobox.get()
        eventname = self.group_combobox.get()
        selected_date = self.date_entry.get()
        selected_time = self.time_combobox.get()
        selected_time2 = self.time_combobox2.get()

        if not selected_date or not selected_time or not selected_time2 or not eventname or not venue:
            tk.messagebox.showerror("Error", "Please complete the form.")
            self.result = None
        else:
            time1 = datetime.strptime(selected_time, "%H:%M:%S").time()
            time2 = datetime.strptime(selected_time2, "%H:%M:%S").time()

            if time1 >= time2:
                tk.messagebox.showerror("Error", "Time 1 must be smaller than Time 2.")
                self.result = None
            else:
                self.result = (venue, eventname, selected_date, time1, time2, self.coursecode)
                self.controller.show_frame(Course_TCH)
    def get_time_values(self):
        times = []
        for hour in range(0, 24):
            for minute in range(0, 60, 30):
                time_obj = time(hour, minute)
                times.append(time_obj.strftime("%H:%M:%S"))

        return times

    def open_calendar(self):
        def set_selected_date():
            selected_date = cal.selection_get().strftime("%Y-%m-%d")
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(tk.END, selected_date)
            top.destroy()

        top = tk.Toplevel(self)
        cal = Calendar(top, selectmode="day")
        cal.pack()
        confirm_button = tk.Button(top, text="Select", command=set_selected_date)
        confirm_button.pack()
        
class StudentDialog(simpledialog.Dialog):
    def __init__(self, parent, course_code, controller):
        self.coursecode = course_code
        self.controller = controller
        super().__init__(parent)

    def body(self, master):
        StudentID_frame = tk.Frame(master)
        StudentID_frame.pack()
        tk.Label(StudentID_frame, text="StudentID: ").pack(side='left')
        self.StudentID_entry = tk.Entry(StudentID_frame)
        self.StudentID_entry.pack(side='left',pady=2)
        
    def apply(self):
        StudentID = self.StudentID_entry.get()

        if not StudentID:
            tk.messagebox.showerror("Error", "Please complete the form.")
            self.result = None
        else:
            self.result = (self.coursecode, StudentID)
            self.controller.show_frame(Course_TCH)
            
class TCH_MeanPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Teacher_name = ''
        self.configure(bg='white')

        style = ttk.Style()
        style.configure("Menu.TButton", foreground="white", background="#57a6fa", font=("Helvetica", 12))

        username_frame = tk.Frame(self, bg="#57a6fa", height=50)
        username_frame.pack(side="top", fill="x")
        
        self.username_label = tk.Label(username_frame, text='', font=("Helvetica", 12),fg="white",bg="#57a6fa")
        self.username_label.pack(side="right", padx=20, pady=10)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(side="top", fill="x")

        menu_frame = tk.Frame(self, bg="#57a6fa")
        menu_frame.pack(side="left", fill="y")

        menu_label = tk.Label(menu_frame, text="Menu", font=("Helvetica", 14),fg="white",bg="#57a6fa")
        menu_label.pack(side="top", padx=5, pady=5)

        line = tk.Frame(menu_frame, height=2, width=200, bg="white")
        line.pack(fill="x", padx=0, pady=10)
        
        Home_image = Image.open("img/Mainpage.png")
        Home_image = Home_image.resize((24, 24))  
        self.Home_icon = ImageTk.PhotoImage(Home_image)

        Course_image = Image.open("img/Course.png")
        Course_image = Course_image.resize((24, 24))
        self.Course_icon = ImageTk.PhotoImage(Course_image)
        
        Home_button = ttk.Button(menu_frame, text="Home", image=self.Home_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(TCH_MeanPage))
        Home_button.pack(side="top", fill="x", padx=10, pady=5)

        Course_button = ttk.Button(menu_frame, text="Course", image=self.Course_icon, compound="left", style="Menu.TButton", command=lambda: controller.show_frame(Course_TCH))
        Course_button.pack(side="top", fill="x", padx=10, pady=5)

        Logout_image = Image.open("img/logout_icon.png")
        Logout_image = Logout_image.resize((24, 24))
        self.Logout_icon = ImageTk.PhotoImage(Logout_image)

        logout_button = ttk.Button(menu_frame, text="Logout", image=self.Logout_icon, compound="left", style="Menu.TButton", command=lambda: controller.logout())
        logout_button.pack(side="bottom", fill="x", padx=10, pady=15)

        # main stage
        self.main_stage = tk.Frame(self, bg="white")
        self.main_stage.pack(side="left", fill="both", expand=True)
        

    def update_data(self):
        user = self.controller.get_user()
        Teacher_name = user.get_username()

        self.username_label.configure(text=Teacher_name)

        if self.main_stage.winfo_children():
            for widget in self.main_stage.winfo_children():
                widget.destroy()

        content_label = tk.Label(self.main_stage, text="Home Page", font=("Helvetica", 24),bg = 'white')
        content_label.pack(padx=50, pady=70)

        Welcome_frame = tk.Frame(self.main_stage,borderwidth=2, relief="solid", pady=100, padx=150)
        Welcome_frame.pack(side="top")

        welcome_label =tk.Label(Welcome_frame, text="Welcome back, " + Teacher_name + ' !', font=("Helvetica", 15))
        welcome_label.pack(side='bottom')

        

        

class Course_TCH(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Teacher_name = ''
        self.courses = []
        self.homework_entry = None
        self.Test_entry = None
        self.Exam_entry = None

        style = ttk.Style()
        style.configure("Menu.TButton", foreground="white", background="#57a6fa", font=("Helvetica", 12))

        username_frame = tk.Frame(self, bg="#57a6fa", height=50)
        username_frame.pack(side="top", fill="x")
        
        self.username_label = tk.Label(username_frame, text='', font=("Helvetica", 12), fg="white", bg="#57a6fa")
        self.username_label.pack(side="right", padx=20, pady=10)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(side="top", fill="x")

        menu_frame = tk.Frame(self, bg="#57a6fa")
        menu_frame.pack(side="left", fill="y")

        menu_label = tk.Label(menu_frame, text="Menu", font=("Helvetica", 14), fg="white", bg="#57a6fa")
        menu_label.pack(side="top", padx=5, pady=5)

        line = tk.Frame(menu_frame, height=2, width=200, bg="white")
        line.pack(fill="x", padx=0, pady=10)

        Home_image = Image.open("img/Mainpage.png")
        Home_image = Home_image.resize((24, 24)) 
        self.Home_icon = ImageTk.PhotoImage(Home_image)

        Course_image = Image.open("img/Course.png")
        Course_image = Course_image.resize((24, 24))
        self.Course_icon = ImageTk.PhotoImage(Course_image)

        Home_button = ttk.Button(menu_frame, text="Home", image=self.Home_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(TCH_MeanPage))
        Home_button.pack(side="top", fill="x", padx=10, pady=5)

        Course_button = ttk.Button(menu_frame, text="Course", image=self.Course_icon, compound="left", style="Menu.TButton", command=lambda:controller.show_frame(Course_TCH))
        Course_button.pack(side="top", fill="x", padx=10, pady=5)

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

    def create_course(self):
        dialog = CustomDialog(self.main_stage,self.course_code, self.controller)
        selected = dialog.result
        if selected:
            self.controller.db.create_course(selected[0],selected[1],selected[2],selected[3],selected[4],selected[5])

    def addStudentToCourse(self):
        dialog = StudentDialog(self.main_stage,self.course_code, self.controller)
        selected = dialog.result
        if selected:
            self.controller.db.create_StudentToCourse(selected[0],selected[1])

    def update_data(self):
        user = self.controller.get_user()
        Teacher_name = user.get_username()

        self.username_label.configure(text=Teacher_name)


        db = Database()
        teacher_id = self.controller.get_user().get_userID()
        result = db.teacher_course(teacher_id)
        db.close()

        if self.main_stage.winfo_children():
            for widget in self.main_stage.winfo_children():
                widget.destroy()
   
        content_frame = tk.Frame(self.main_stage,bg='white')
        content_frame.pack()
        
        content_label = tk.Label(content_frame, text="Course", font=("Helvetica", 24), bg="white")
        content_label.pack(padx=50, pady=50)

        contain_header_frame = tk.Frame(content_frame, bg="white")
        contain_header_frame.pack(side='top',fill="x", padx=10, pady=2)

        header_frame = tk.Frame(contain_header_frame, bg="white")
        header_frame.pack(fill="x", padx=10, pady=5)

        course_code_header = tk.Label(header_frame, text="CourseCode", font=("Helvetica", 12), width=15, bg="white")
        course_code_header.pack(side="left", padx=(10, 5))

        course_title_header = tk.Label(header_frame, text="CourseTitle", font=("Helvetica", 12), width=40, bg="white")
        course_title_header.pack(side="left", padx=(0, 5))

        line = tk.Frame(contain_header_frame, height=2, width=240, bg="black")
        line.pack(side="top",fill="x", padx=0, pady=3)
        if result:
            for row in result:
                # main stage
                
                course_frame = tk.Frame(contain_header_frame, bg="white", pady=10)
                course_frame.pack(fill="x", padx=10, pady=5)

                course_code_label = tk.Label(course_frame, text=row[0], font=("Helvetica", 12), width=15, bg="white")
                course_code_label.pack(side="left", padx=(10, 5))

                course_title_label = tk.Label(course_frame, text=row[1], font=("Helvetica", 12), width=40, bg="white")
                course_title_label.pack(side="left", padx=(0, 5))

                button_frame = tk.Frame(course_frame, bg="white")
                button_frame.pack(side="left")

                view_button = tk.Button(button_frame, text="View", font=("Helvetica", 12), command=lambda code=row[0],course_title=row[1],leader=row[3]: (self.show_course_page(code,course_title,leader)))
                view_button.pack(padx=(0, 10))
                
    def go_back_to_course_page(self):
        self.controller.show_frame(Course_TCH)  

    def display_message(self,Course_Code,Date,Time_Start):
        result = messagebox.askquestion("Warning", "Did you want to cancel the Class?")
        
        if result == "yes":
            print("Runing...")
            self.controller.db.delete_course(Course_Code,Date,Time_Start)
            self.controller.show_frame(Course_TCH)

            
        else:
            print("Cancelled.")
    def Attendance_by_course(self,CourseCode,Course_Title,selected_Date):
        if self.main_stage.winfo_children():
            for widget in self.main_stage.winfo_children():
                widget.destroy()
        courseheader_frame = tk.Frame(self.main_stage, bg="white")
        courseheader_frame.pack(fill="x", padx=10, pady=5)

        inner_frame = tk.Frame(courseheader_frame, bg="white")
        inner_frame.pack()

        course_code_label = tk.Label(inner_frame, text=CourseCode, font=("Helvetica", 16), pady=10)
        course_code_label.pack(side="left", padx=(0, 1),pady=20)

        course_title_label = tk.Label(inner_frame, text=Course_Title, font=("Helvetica", 16), pady=10)
        course_title_label.pack(side="left")

        topline = tk.Frame(self.main_stage,bg="white")
        topline.pack(fill="x")
            
            
        back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
        back_button.pack(side="left", padx=(10,0))
        Title = tk.Label(topline, text='Course Attendance', font=("Helvetica", 16), pady=10,bg='white')
        Title.pack()

        content_frame = tk.Frame(self.main_stage,bg='white')
        content_frame.pack()
            
        student_id = self.controller.get_user().get_userID()
        data = self.controller.db.course_attendance_TCH(student_id,CourseCode,selected_Date)

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

        StudentID_header =tk.Label(header_frame, text="Student ID", width=15,bg="white")
        StudentID_header.pack(side="left", padx=(0, 0))


        line = tk.Frame(contain_header_frame, height=2, width=240, bg="black")
        line.pack(side="top",fill="x", padx=0, pady=3)
        if data:
            i = 0
            for row in data:
                # main stage
                if i == 1:
                    result_frame = tk.Frame(contain_header_frame, bg="white", pady=5)
                    result_frame.pack(fill="x", padx=10, pady=1)

                    course_type_label = tk.Label(result_frame, text=row[4],  width=15)
                    course_type_label.pack(side="left", padx=(10, 0))

                    Date_label = tk.Label(result_frame, text=row[1], width=15)
                    Date_label.pack(side="left", padx=(0, 0))
                    Time_label = tk.Label(result_frame, text=row[2],  width=15)
                    Time_label.pack(side="left", padx=(0, 0))

                    StudentID_label = tk.Label(result_frame, text=row[0],  width=15)
                    StudentID_label.pack(side="left", padx=(0, 0))
                    i = 0
                else:
                    result_frame = tk.Frame(contain_header_frame, bg="white", pady=5)
                    result_frame.pack(fill="x", padx=10, pady=1)

                    course_type_label = tk.Label(result_frame, text=row[4],  width=15,bg="white")
                    course_type_label.pack(side="left", padx=(10, 0))

                    Date_label = tk.Label(result_frame, text=row[1], width=15,bg="white")
                    Date_label.pack(side="left", padx=(0, 0))
                    Time_label = tk.Label(result_frame, text=row[2],  width=15,bg="white")
                    Time_label.pack(side="left", padx=(0, 0))
                    StudentID_label = tk.Label(result_frame, text=row[0], width=15, bg="white")
                    StudentID_label.pack(side="left", padx=(0, 0))
                    i =+ 1

    def show_course_page(self, course_code,course_title,leader):
        self.course_code= course_code
        
        if self.main_stage.winfo_children():
            for widget in self.main_stage.winfo_children():
                widget.destroy()     
        def navigate_to_Student_page():
            
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10)
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10)
            course_title_label.pack(side="left")

            back_frame = tk.Frame(self.main_stage, bg="white")
            back_frame.pack(fill="x", padx=10, pady=5)
            
            back_button = tk.Button(back_frame, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=10)

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack(fill="x", padx=10, pady=5)
            
            
            # Teacher can view the student who student in this course??
            # add code here
            data = self.controller.db.course_student(self.course_code)


            contain_header_frame = tk.Frame(content_frame, bg="white")
            contain_header_frame.pack(side='top',fill="x", padx=10, pady=2)
            
            header_frame = tk.Frame(contain_header_frame, bg="white")
            header_frame.pack(fill="x", padx=10, pady=5)

            CourseCode_header = tk.Label(header_frame, text="CourseCode", width=15,bg="white")
            CourseCode_header.pack(side="left", padx=(10, 0))

            StudentID_header = tk.Label(header_frame, text="StudentID", width=15,bg="white")
            StudentID_header.pack(side="left", padx=(0, 0))

            add_image = Image.open("img/add_icon.png")
            add_image = add_image.resize((24, 24))
            self.add_icon = ImageTk.PhotoImage(add_image)
            
            create_course_button = tk.Button(header_frame, image=self.add_icon,command=self.addStudentToCourse)
            create_course_button.pack(side="right", padx=(0, 0))
            

            line = tk.Frame(contain_header_frame, height=2, width=240, bg="black")
            line.pack(side="top",fill="x", padx=0, pady=3)
            if data:
                for row in data:
                    # main stage
                    result_frame = tk.Frame(contain_header_frame, bg="white", pady=5)
                    result_frame.pack(fill="x", padx=10, pady=1)

                    CourseCode_label = tk.Label(result_frame, text=row[0],  width=15)
                    CourseCode_label.pack(side="left", padx=(10, 0))

                    StudentID_label = tk.Label(result_frame, text=row[1], width=15)
                    StudentID_label.pack(side="left", padx=(0, 0))

                    Delete_button = tk.Button(result_frame, text="Delete", font=("Helvetica", 12),command=lambda CourseCode=row[0], StudentID=row[1]: delete_message(CourseCode,StudentID))
                    Delete_button.pack(padx=(4, 10))

            def delete_message(CourseCode,StudentID):
                result = messagebox.askquestion("Warning", "Did you want to cancel the Class?")
                
                if result == "yes":
                    print("Runing...")
                    self.controller.db.delete_course_student(CourseCode,StudentID)
                    self.controller.show_frame(Course_TCH)

                    
                else:
                    print("Cancelled.")

            
        def navigate_to_Score_page():
            
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10)
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10)
            course_title_label.pack(side="left")

            back_frame = tk.Frame(self.main_stage, bg="white")
            back_frame.pack(fill="x", padx=10, pady=5)
            
            back_button = tk.Button(back_frame, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=10)

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack(fill="x", padx=10, pady=5)
            
            # Teacher can do the course score in this page. such as the student test score
            # add code here

            course_function_frame = tk.Frame(self.main_stage, bg="white")
            course_function_frame.pack(side='top' ,padx=40, pady=8)

            left_frame = tk.Frame(course_function_frame, bg="white")
            left_frame.pack(side='left', padx=45, pady=5)

            right_frame = tk.Frame(course_function_frame, bg="white")
            right_frame.pack( side='right', padx=45, pady=5)


            score_image = Image.open("img/score_icon2.png")
            score_image = score_image.resize((150, 150))
            self.score_icon = ImageTk.PhotoImage(score_image)
            
            Student_button = tk.Button(left_frame,image = self.score_icon, text="View",command=View_student_score)
            Student_button.pack(side="top", padx=10)
            Student_button_label = tk.Label(left_frame, text='View', font=("Helvetica", 16), pady=2,bg='white')
            Student_button_label.pack(side="top",pady=(0,25))

            update_image = Image.open("img/score_icon3.png")
            update_image = update_image.resize((150, 150))
            self.update_score_icon = ImageTk.PhotoImage(update_image)
            
            Score_button = tk.Button(right_frame,image = self.update_score_icon, text="Update",command=Update_student_score)
            Score_button.pack(side="top", padx=10)
            Score_button_label = tk.Label(right_frame, text='Update', font=("Helvetica", 16), pady=2,bg='white')
            Score_button_label.pack(side="top",pady=(0,25))

        def View_student_score ():
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
                    
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10,bg='white')
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,bg='white')
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")
            
            back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=(10,0))

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack()

            Title_label = tk.Label(topline, text='Student Score', font=("Helvetica", 16), pady=10,bg='white')
            Title_label.pack()

            tree_frame = tk.Frame(self.main_stage,bg='white')
            tree_frame.pack(pady=10)

            data = self.controller.db.get_Score(self.course_code)

            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
            scrollbar.pack(side="right", fill="y")
            tree = ttk.Treeview(tree_frame )

            columns = ["StudentID", "Type", "Score", "ScorePercent"]

            tree["columns"] = tuple(range(len(columns)))

            for i, column_name in enumerate(columns):
               tree.heading(i, text=column_name)

            for row in data:
                tree.insert("", "end", values=row)

            tree.pack()
            scrollbar.config(command=tree.yview)

            def search_student():
                student_id = self.search_entry.get()

                tree.delete(*tree.get_children())

                search_results = [row for row in data if row[0] == student_id]
                for row in search_results:
                    tree.insert("", "end", values=row)

                self.search_window.destroy()

            def open_search_window():
                self.search_window = tk.Toplevel(self.main_stage)

                search_label = tk.Label(self.search_window, text="Student ID : ", pady=10)
                search_label.pack(side="left", padx=(0, 1),pady=10)

                self.search_entry = tk.Entry(self.search_window)
                self.search_entry.pack(side="left",pady=20)

                search_button = tk.Button(self.search_window, text="Search", command=search_student)
                search_button.pack(side="left",padx = 10)

            def delete_rows():
                # Get the selected items from the treeview
                selected_items = tree.selection()

                # Remove the selected rows from the treeview and the data
                for item in selected_items:
                    values = tree.item(item, "values")
                    tree.delete(item)
                    self.controller.db.delete_student_score(self.course_code,values[0],values[1])
                    if values in data:
                        data.remove(values)
                        


            def sort_treeview(column):
                tree.delete(*tree.get_children())

                data = self.controller.db.get_Score(self.course_code)

                sorted_data = sorted(data, key=lambda row: row[column])

                for row in sorted_data:
                    tree.insert("", "end", values=row)

            def clear_treeview():
                # Clear the treeview
                tree.delete(*tree.get_children())

                # Insert the original data into the treeview
                original_data = self.controller.db.get_Score(self.course_code)
                for row in original_data:
                    tree.insert("", "end", values=row)

                    
            for i, column_name in enumerate(columns):
                tree.heading(i, text=column_name, command=lambda col=i: sort_treeview(col))

            search_button = tk.Button(topline, text="Search", command=open_search_window)
            search_button.pack(side="right", padx=(10, 60))

            clear_button = tk.Button(topline, text="Clear", command=clear_treeview)
            clear_button.pack(side="right", padx=(10, 5))

            delete_button = tk.Button(topline, text="Delete", command=delete_rows)
            delete_button.pack(side="right", padx=(10, 5))


        def Update_student_score ():
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
                    
            def validate_input_score(value):
                try:
                    # don't let the input be alphabet
                    if len(value) > 0:
                        self.calculate = 0
                        if int(value) <= 100:
                            self.calculate = int(value) * self.percentage/100
                            self.final_score_label.config(text=f"Calculation Score: {self.calculate}")
                        elif int(value) > 100:
                            self.final_score_label.config(text=f"Calculation Score: Error")
                    elif value == "":
                        self.final_score_label.config(text=f"Calculation Score: ")
                    # limit the age under 2 length
                    if len(value) <= 3:
                        return True
                    else:
                        return False
                    
                except ValueError:
                    return False
            
            def update_score():
                score = self.score_entry.get()
                Type = self.type_dropdown.get()
                Student = self.student_dropdown.get()
                
                self.controller.db.update_score( self.course_code,score,self.percentage,Student,Type,self.calculate)
                
                    
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10,bg='white')
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,bg='white')
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")
            
            back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=(10,0))

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack()

            Title_label = tk.Label(topline, text='Update Score', font=("Helvetica", 16), pady=10,bg='white')
            Title_label.pack()

            self.form_frame = tk.Frame(self.main_stage,bg="white",borderwidth=2, relief="solid",padx=30,pady=10)
            self.form_frame.pack(pady=10)

            layout_frame = tk.Frame(self.form_frame,bg="white", padx=30,pady=10)
            layout_frame.pack()

            left_side =tk.Frame(layout_frame,bg="white")
            left_side.pack(side='left',padx=8)

            right_side = tk.Frame(layout_frame,bg="white")
            right_side.pack(side='right',padx=8)

            type_label = tk.Label(left_side, text="Student",bg="white")
            type_label.pack()

            student_list = self.controller.db.get_studentID(self.course_code)
            self.selected_student = tk.StringVar()
            self.percentage = ''
            
            self.student_dropdown = ttk.Combobox(left_side,textvariable=self.selected_student)
            self.student_dropdown['values'] = student_list
            self.student_dropdown.pack(pady=5)

            self.student_dropdown.bind("<<ComboboxSelected>>", student_selection)

            space_label = tk.Label(right_side, text=" ",bg="white")
            space_label.pack(pady=16)

            type_label = tk.Label(left_side, text="Score Type",bg="white")
            type_label.pack()

            type_list = ["Homework","Test","Exam"]
            self.selected_type = tk.StringVar()
            self.percentage = ''
            
            self.type_dropdown = ttk.Combobox(left_side,textvariable=self.selected_type)
            self.type_dropdown['values'] = type_list
            self.type_dropdown.pack(pady=5)

            score_percentage_label = tk.Label(right_side, text="Score Percentage",bg="white")
            score_percentage_label.pack()

            self.percentage_label = tk.Label(right_side, text= "%",bg="white")
            self.percentage_label.pack(pady=5)

            self.type_dropdown.bind("<<ComboboxSelected>>", type_selection)

            score_label = tk.Label(left_side, text="Input Score:",bg="white")
            score_label.pack()

            self.score_entry = tk.Entry(left_side, state=tk.NORMAL)
            self.score_entry.pack(pady=(2,10))
            self.score_entry.configure(state=tk.DISABLED)

            validate_score = (self.form_frame.register(validate_input_score), '%P')
            self.score_entry.configure(validate='key', validatecommand=validate_score)

            space_label = tk.Label(right_side, text=" ",bg="white")
            space_label.pack(pady=16)

            
            right_corner= tk.Frame(self.form_frame,bg="white")
            right_corner.pack(side='right',padx=8)
            
            self.final_score_label = tk.Label(right_corner, text="Calculation Score: ",bg="white")
            self.final_score_label.pack(pady=5)
            
            self.submit_button = tk.Button(right_corner, text="Update", state=tk.DISABLED,command=update_score)
            self.submit_button.pack(pady=10)
                
        def student_selection(event):
            selected_item = self.student_dropdown.get()

        def type_selection(event):
            selected_item = self.type_dropdown.get()

            if selected_item == 'Homework':
                self.percentage = 20
            elif selected_item == 'Test':
                self.percentage = 30
            else:
                self.percentage = 50
            self.percentage_label.config(text=f"{self.percentage} %")
            self.score_entry.configure(state=tk.NORMAL)
            self.submit_button.configure(state=tk.NORMAL)

        def student_selection_GPA(event):
                selected_item = self.student_dropdown.get()
                student_score = self.controller.db.get_student_score(self.course_code,selected_item)

                self.Exam = student_score[0][5]
                self.Homework =  student_score[1][5]
                self.Test = student_score[2][5]
                self.selected_student = selected_item
                
                

                update_the_entry()

        
            
        def navigate_to_Attendance_page():
            
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10)
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10)
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")
            
            back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=(10,0))

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack()

            Title_label = tk.Label(topline, text='Course Attendance', font=("Helvetica", 16), pady=10,bg='white')
            Title_label.pack()

            # Teacher can check the course Attendance in this page
            # add code here
            teacher_id = self.controller.get_user().get_userID()
            data = self.controller.db.teaching_course_attendance(teacher_id,self.course_code)

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

            Venue_header = tk.Label(header_frame, text="Venue", width=15,bg="white")
            Venue_header.pack(side="left", padx=(0, 0))


            line = tk.Frame(contain_header_frame, height=2, width=240, bg="black")
            line.pack(side="top",fill="x", padx=0, pady=3)
            if data:
                for row in data:
                    # main stage
                    result_frame = tk.Frame(contain_header_frame, bg="white", pady=5)
                    result_frame.pack(fill="x", padx=10, pady=1)

                    course_type_label = tk.Label(result_frame, text=row[2],  width=15)
                    course_type_label.pack(side="left", padx=(10, 0))

                    Date_label = tk.Label(result_frame, text=row[3], width=15)
                    Date_label.pack(side="left", padx=(0, 0))
                    
                    Time_label = tk.Label(result_frame, text=str(row[4]) +' - '+ str(row[5]),  width=15)
                    Time_label.pack(side="left", padx=(0, 0))

                    Venue_label = tk.Label(result_frame, text=row[6],  width=15)
                    Venue_label.pack(side="left", padx=(0, 0))
                    view_button = tk.Button(result_frame, text="View", font=("Helvetica", 12),command=lambda code=row[0] , selected_Date = row[3]: self.Attendance_by_course(code,course_title,selected_Date))
                    view_button.pack(padx=(2, 10))


        def navigate_to_Arrangement_page():
            
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10,bg='white')
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,bg='white')
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")
            
            back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=10)

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack()

            # Teacher can manage the course lesson in this page
            # add code here
            Title_label = tk.Label(topline, text='Course Schedule', font=("Helvetica", 16), pady=10,bg='white')
            Title_label.pack()

            teacher_id = self.controller.get_user().get_userID()
            data = self.controller.db.teaching_course_attendance(teacher_id,self.course_code)

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

            Venue_header = tk.Label(header_frame, text="Venue", width=15,bg="white")
            Venue_header.pack(side="left", padx=(0, 0))

            add_image = Image.open("img/add_icon.png")
            add_image = add_image.resize((24, 24))
            self.add_icon = ImageTk.PhotoImage(add_image)
            
            create_course_button = tk.Button(header_frame, image=self.add_icon,command=self.create_course)
            create_course_button.pack(side="right", padx=(0, 0))

            
            

            line = tk.Frame(contain_header_frame, height=2, width=240, bg="black")
            line.pack(side="top",fill="x", padx=0, pady=3)
            if data:
                for row in data:
                    # main stage
                    result_frame = tk.Frame(contain_header_frame, bg="white", pady=5)
                    result_frame.pack(fill="x", padx=10, pady=1)

                    course_type_label = tk.Label(result_frame, text=row[2],  width=15)
                    course_type_label.pack(side="left", padx=(10, 0))

                    Date_label = tk.Label(result_frame, text=row[3], width=15)
                    Date_label.pack(side="left", padx=(0, 0))
                    
                    Time_label = tk.Label(result_frame, text=str(row[4]) +' - '+ str(row[5]),  width=15)
                    Time_label.pack(side="left", padx=(0, 0))

                    Venue_label = tk.Label(result_frame, text=row[6],  width=15)
                    Venue_label.pack(side="left", padx=(0, 0))

                    Delete_button = tk.Button(result_frame, text="Delete", font=("Helvetica", 12),command=lambda code=row[0], selected_Date=row[3],Time_Start=row[4]: self.display_message(code,selected_Date,Time_Start))
                    Delete_button.pack(padx=(4, 10))

            

            

        def navigate_to_GPA_page():
            
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10)
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10)
            course_title_label.pack(side="left")

            back_frame = tk.Frame(self.main_stage, bg="white")
            back_frame.pack(fill="x", padx=10, pady=5)
            
            back_button = tk.Button(back_frame, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=10)

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack(fill="x", padx=10, pady=5)

            # Teacher can manage the GPA in this page
            # add code here


            course_function_frame = tk.Frame(self.main_stage, bg="white")
            course_function_frame.pack(side='top' ,padx=40, pady=8)

            left_frame = tk.Frame(course_function_frame, bg="white")
            left_frame.pack(side='left', padx=45, pady=5)

            right_frame = tk.Frame(course_function_frame, bg="white")
            right_frame.pack( side='right', padx=45, pady=5)


            score_image = Image.open("img/GPA.png")
            score_image = score_image.resize((150, 150))
            self.score_icon = ImageTk.PhotoImage(score_image)
            
            view_score_button = tk.Button(left_frame,image = self.score_icon,command=view_student_GPA)
            view_score_button.pack(side="top", padx=10)
            view_score_button = tk.Label(left_frame, text='View', font=("Helvetica", 16), pady=2,bg='white')
            view_score_button.pack(side="top",pady=(0,25))

            update_image = Image.open("img/GPA.png")
            update_image = update_image.resize((150, 150))
            self.update_score_icon = ImageTk.PhotoImage(update_image)
            
            Score_button = tk.Button(right_frame,image = self.update_score_icon,command = Update_student_GPA)
            Score_button.pack(side="top", padx=10)
            Score_button_label = tk.Label(right_frame, text='Update', font=("Helvetica", 16), pady=2,bg='white')
            Score_button_label.pack(side="top",pady=(0,25))

        def view_student_GPA ():
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
                    
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10,bg='white')
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,bg='white')
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")
            
            back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=(10,0))

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack()

            Title_label = tk.Label(topline, text='View GPA', font=("Helvetica", 16), pady=10,bg='white')
            Title_label.pack()

            tree_frame = tk.Frame(self.main_stage)
            tree_frame.pack(pady=10)

            data = self.controller.db.get_all_student_GPA(self.course_code)
            
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
            scrollbar.pack(side="right", fill="y")
            tree = ttk.Treeview(tree_frame)

            columns = ["StudentID", "Student Name", "Grade"]

            tree["columns"] = tuple(range(len(columns)))

            for i, column_name in enumerate(columns):
               tree.heading(i, text=column_name)

            for row in data:
                tree.insert("", "end", values=row)

            tree.pack()
            scrollbar.config(command=tree.yview)

            def search_student():
                student_id = self.search_entry.get()

                tree.delete(*tree.get_children())

                search_results = [row for row in data if row[0] == student_id]
                for row in search_results:
                    tree.insert("", "end", values=row)
                    
                self.search_window.destroy()
                
            def open_search_window():
                self.search_window = tk.Toplevel(self.main_stage)

                search_label = tk.Label(self.search_window, text="Student ID : ", pady=10)
                search_label.pack(side="left", padx=(0, 1),pady=20)

                self.search_entry = tk.Entry(self.search_window)
                self.search_entry.pack(side="left",padx= 20)

                search_button = tk.Button(self.search_window, text="Search", command=search_student)
                search_button.pack(side="left",padx= 10)

            def delete_rows():
                # Get the selected items from the treeview
                selected_items = tree.selection()
                
                # Remove the selected rows from the treeview and the data
                for item in selected_items:
                    values = tree.item(item, "values")
                    tree.delete(item)
                    print(values)
                    self.controller.db.delete_student_GPA(self.course_code,values[0])
                    if values in data:
                        data.remove(values)

            def sort_treeview(column):
                tree.delete(*tree.get_children())

                data = self.controller.db.get_all_student_GPA(self.course_code)

                if tree.heading(column)["text"] == columns[column]:
                    sorted_data = sorted(data, key=lambda row: row[column], reverse=True)
                    tree.heading(column, text=columns[column] + " ↑")
                else:
                    sorted_data = sorted(data, key=lambda row: row[column])
                    tree.heading(column, text=columns[column] + " ↑")

                for row in sorted_data:
                    tree.insert("", "end", values=row)
            def clear_treeview():
                # Clear the treeview
                tree.delete(*tree.get_children())

                # Insert the original data into the treeview
                original_data = self.controller.db.get_all_student_GPA(self.course_code)
                for row in original_data:
                    tree.insert("", "end", values=row)

                    
            for i, column_name in enumerate(columns):
                tree.heading(i, text=column_name, command=lambda col=i: sort_treeview(col))
                
            search_button = tk.Button(topline, text="Search", command=open_search_window)
            search_button.pack(side="right", padx=(10, 60))

            clear_button = tk.Button(topline, text="Clear", command=clear_treeview)
            clear_button.pack(side="right", padx=(10, 5))

            delete_button = tk.Button(topline, text="Delete", command=delete_rows)
            delete_button.pack(side="right", padx=(10, 5))

        def Update_student_GPA ():
            if self.main_stage.winfo_children():
                for widget in self.main_stage.winfo_children():
                    widget.destroy()
                    
            courseheader_frame = tk.Frame(self.main_stage, bg="white")
            courseheader_frame.pack(fill="x", padx=10, pady=5)

            inner_frame = tk.Frame(courseheader_frame, bg="white")
            inner_frame.pack()

            course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10,bg='white')
            course_code_label.pack(side="left", padx=(0, 1),pady=20)

            course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,bg='white')
            course_title_label.pack(side="left")

            topline = tk.Frame(self.main_stage,bg="white")
            topline.pack(fill="x")
            
            back_button = tk.Button(topline, text="Back", command=self.go_back_to_course_page)
            back_button.pack(side="left", padx=(10,0))

            content_frame = tk.Frame(self.main_stage, bg="white")
            content_frame.pack()

            Title_label = tk.Label(topline, text='Update GPA', font=("Helvetica", 16), pady=10,bg='white')
            Title_label.pack()

            course_function_frame = tk.Frame(self.main_stage, bg="white")
            course_function_frame.pack(side='top' ,padx=40, pady=8)

            left_frame = tk.Frame(course_function_frame, bg="white")
            left_frame.pack(side='left', padx=5, pady=5)

            right_frame = tk.Frame(course_function_frame, bg="white")
            right_frame.pack( side='right', padx=5, pady=5)


            
            #======= GPA Update Form =========
            GPA_form_Frame = tk.Frame(left_frame,bg='white',borderwidth=1, relief="solid")
            GPA_form_Frame.pack(side = 'top',padx=10, pady=5)

            GPA_form_label = tk.Label(GPA_form_Frame, text='GPA Form', font=("Helvetica", 14), pady=10,bg='white')
            GPA_form_label.pack()

            form_left_side = tk.Frame(GPA_form_Frame, bg="white")
            form_left_side.pack(side='left', padx=35, pady=5)

            form_right_side = tk.Frame(GPA_form_Frame, bg="white")
            form_right_side.pack(side='right', padx=35, pady=5)
            

            Student_label = tk.Label(form_left_side, text='Student:',font=(10), pady=10,bg='white')
            Student_label.pack()

            student_list = self.controller.db.get_all_student(self.course_code)

            self.selected_student = tk.StringVar()
            self.student_dropdown = ttk.Combobox(form_left_side,textvariable=student_list,state=tk.NORMAL)
            self.student_dropdown['values'] = student_list
            self.student_dropdown.pack()
            self.student_dropdown.bind("<<ComboboxSelected>>", student_selection_GPA)

            

            label1_frame = tk.Frame(form_left_side, bg="white")
            label1_frame.pack(side='top', padx=20, pady=5)

            Homework_label = tk.Label(label1_frame, text='Homework:  ',font=(12), pady=10,bg='white')
            Homework_label.pack(side='left')

            self.homework_entry = tk.Entry(label1_frame, state=tk.NORMAL)
            self.homework_entry.pack(pady=10)

            label2_frame = tk.Frame(form_left_side, bg="white")
            label2_frame.pack(side='top', padx=20, pady=5)

            Test_label = tk.Label(label2_frame, text='Test:       ',font=(12), pady=10,bg='white')
            Test_label.pack(side='left')

            self.Test_entry = tk.Entry(label2_frame, state=tk.NORMAL)
            self.Test_entry.pack(pady=10)

            label3_frame = tk.Frame(form_left_side, bg="white")
            label3_frame.pack(side='top', padx=20, pady=5)

            Exam_label = tk.Label(label3_frame, text='Exam:     ',font=(12), pady=10,bg='white')
            Exam_label.pack(side='left')

            self.Exam_entry = tk.Entry(label3_frame, state=tk.NORMAL)
            self.Exam_entry.pack(pady=10)

            Total_label = tk.Label(form_right_side, text='Total Score:',font=(10), pady=10,bg='white')
            Total_label.pack(side='left')
            

            self.Total_score_label = tk.Label(form_right_side, text='',font=(10), pady=10,bg='white')
            self.Total_score_label.pack(side='left')


            right_corner_frame= tk.Frame(form_right_side,bg="white")
            right_corner_frame.pack(side='right',padx=8)
            
            self.final_Grade_label = tk.Label(right_corner_frame, text="Final Grade :",bg="white")
            self.final_Grade_label.pack(pady=5)
            
            self.submit_button = tk.Button(right_corner_frame, text="Update", state=tk.DISABLED,command=update_GPA_record)
            self.submit_button.pack(pady=10)



            #======GPA Standard Form=========

            GPA_standard_frame = tk.Frame(right_frame, bg="white",borderwidth=1, relief="solid")
            GPA_standard_frame.pack (padx=10, pady=5)

            GPA_standard_label = tk.Label(GPA_standard_frame, text='GPA Standard', font=("Helvetica", 14), pady=10,bg='white')
            GPA_standard_label.pack()

            left_side = tk.Frame(GPA_standard_frame, bg="white")
            left_side.pack(side='left', padx=35, pady=5)

            right_side = tk.Frame(GPA_standard_frame, bg="white")
            right_side.pack(side='right', padx=35, pady=5)

            GPA_Grade_label = tk.Label(left_side, text='GPA Grade', font=("Helvetica", 13), pady=10,bg='white')
            GPA_Grade_label.pack()
            
            Score_label = tk.Label(right_side, text='Score', font=("Helvetica", 13), pady=10,bg='white')
            Score_label.pack()

            A_label = tk.Label(left_side, text='A', pady=10,bg='white')
            A_label.pack()

            A_score_label = tk.Label(right_side, text='80 above', pady=10,bg='white')
            A_score_label.pack()

            Aminus_label = tk.Label(left_side, text='A-', pady=10,bg='white')
            Aminus_label.pack()

            Aminus_score_label = tk.Label(right_side, text='76 - 80', pady=10,bg='white')
            Aminus_score_label.pack()


            Bplus_label = tk.Label(left_side, text='B+', pady=10,bg='white')
            Bplus_label.pack()

            Bplus_score_label = tk.Label(right_side, text='71 - 75', pady=10,bg='white')
            Bplus_score_label.pack()

            B_label = tk.Label(left_side, text='B', pady=10,bg='white')
            B_label.pack()

            B_score_label = tk.Label(right_side, text='66 - 70', pady=10,bg='white')
            B_score_label.pack()

            Bminus_label = tk.Label(left_side, text='B-', pady=10,bg='white')
            Bminus_label.pack()

            Bminus_score_label = tk.Label(right_side, text='61 - 65', pady=10,bg='white')
            Bminus_score_label.pack()

            Cplus_label = tk.Label(left_side, text='C+', pady=10,bg='white')
            Cplus_label.pack()

            Cplus_score_label = tk.Label(right_side, text='56 - 60', pady=10,bg='white')
            Cplus_score_label.pack()

            C_label = tk.Label(left_side, text='C', pady=10,bg='white')
            C_label.pack()

            C_score_label = tk.Label(right_side, text='51 - 55', pady=10,bg='white')
            C_score_label.pack()

            pass_label = tk.Label(left_side, text='Pass', pady=10,bg='white')
            pass_label.pack()

            pass_score_label = tk.Label(right_side, text='40 - 50', pady=10,bg='white')
            pass_score_label.pack()

            Fail_label = tk.Label(left_side, text='Fail', pady=10,bg='white')
            Fail_label.pack()

            Fail_score_label = tk.Label(right_side, text='40 Below', pady=10,bg='white')
            Fail_score_label.pack()

        def update_the_entry():
            self.homework_entry.delete(0, tk.END)
            self.homework_entry.insert(0, self.Homework)

            self.Test_entry.delete(0, tk.END)
            self.Test_entry.insert(0, self.Test)

            self.Exam_entry.delete(0, tk.END)
            self.Exam_entry.insert(0, self.Exam)
            self.Total_score = self.Homework + self.Test + self.Exam

            self.Total_score_label.configure(text=f"{self.Total_score}")

            #===== assign the GPA Grade =====

            if float(self.Total_score) > 80:
                self.Final_Grade = 'A'
                
            elif 75 < float(self.Total_score) <= 80:
                self.Final_Grade = 'A-'
                
            elif 70 < float(self.Total_score) <= 75:
                self.Final_Grade = 'B+'
                
            elif 65 <=float(self.Total_score) <= 70:
                self.Final_Grade = 'B'
                
            elif 60 < float(self.Total_score) <= 65:
                self.Final_Grade = 'B-'
                
            elif 55 < float(self.Total_score) <= 60:
                self.Final_Grade = 'C+'
                
            elif 50 < float(self.Total_score) <= 55:
                self.Final_Grade = 'C'

            elif 40 <= float(self.Total_score) <= 50:
                self.Final_Grade = 'Pass'
                
            else:
                self.Final_Grade = 'Fail'

            self.final_Grade_label.configure(text=f" Final Grade : {self.Final_Grade}")
            self.submit_button.configure(state=tk.NORMAL)

        def update_GPA_record():
            #print(self.course_code,self.selected_student,self.Final_Grade)

            self.controller.db.update_GPA(self.course_code,self.selected_student,self.Final_Grade)


            


        courseheader_frame = tk.Frame(self.main_stage, bg="white")
        courseheader_frame.pack(fill="x", padx=10, pady=5)

        inner_frame = tk.Frame(courseheader_frame, bg="white")
        inner_frame.pack()

        course_code_label = tk.Label(inner_frame, text=course_code, font=("Helvetica", 16), pady=10 ,bg='white')
        course_code_label.pack(side="left", padx=(0, 1),pady=20)

        course_title_label = tk.Label(inner_frame, text=course_title, font=("Helvetica", 16), pady=10,bg='white')
        course_title_label.pack(side="left")

        line = tk.Frame(self.main_stage, height=2, bg="black")
        line.pack(side="top",fill="x", padx=0, pady=8)

        course_function_frame = tk.Frame(self.main_stage, bg="white")
        course_function_frame.pack(side='top' ,padx=40, pady=8)

        left_frame = tk.Frame(course_function_frame, bg="white")
        left_frame.pack(side='left', padx=45, pady=5)

        right_frame = tk.Frame(course_function_frame, bg="white")
        right_frame.pack( side='right', padx=45, pady=5)

        student_image = Image.open("img/student_icon.png")
        student_image = student_image.resize((150, 150))
        self.student_icon = ImageTk.PhotoImage(student_image)
        
        Student_button = tk.Button(left_frame,image = self.student_icon, text="Student",command=navigate_to_Student_page)
        Student_button.pack(side="top", padx=10)
        Student_button_label = tk.Label(left_frame, text='Student', font=("Helvetica", 16), pady=2,bg='white')
        Student_button_label.pack(side="top",pady=(0,25))
        

        score_image = Image.open("img/score_icon2.png")
        score_image = score_image.resize((150, 150))
        self.score_icon = ImageTk.PhotoImage(score_image)

        Score_button = tk.Button(right_frame,image = self.score_icon, text="Score",command=navigate_to_Score_page)
        Score_button.pack(side="top", padx=10)
        Score_button_label = tk.Label(right_frame, text='Score', font=("Helvetica", 16), pady=2,bg='white')
        Score_button_label.pack(side="top",pady=(0,25))
        
        
        class_schedule_image = Image.open("img/class_schedule.png")
        class_schedule_image = class_schedule_image.resize((150, 150))
        self.class_schedule_icon = ImageTk.PhotoImage(class_schedule_image)

        schedule_button = tk.Button(left_frame,image= self.class_schedule_icon,text="Schedule",command=navigate_to_Arrangement_page)
        schedule_button.pack(side="top", padx=10)
        schedule_button_label = tk.Label(left_frame, text='Schedule', font=("Helvetica", 16), pady=2,bg='white')
        schedule_button_label.pack(side="top",pady=(0,25))

        attendance_Course_image = Image.open("img/Attendance.png")
        attendance_Course_image = attendance_Course_image.resize((150, 150))
        self.attendance_icon = ImageTk.PhotoImage(attendance_Course_image)

        Attendance_button = tk.Button(right_frame,image=self.attendance_icon, text="Attendance",command=navigate_to_Attendance_page)
        Attendance_button.pack(side="top", padx=10)
        Attendance_button_label = tk.Label(right_frame, text='Attendance', font=("Helvetica", 16), pady=2,bg='white')
        Attendance_button_label.pack(side="top",pady=(0,25))

        GPA_image = Image.open("img/GPA.png")
        GPA_image = GPA_image.resize((150, 150))
        self.GPA_icon = ImageTk.PhotoImage(GPA_image)

        if leader == 1:
            GPA_button = tk.Button(left_frame,image=self.GPA_icon, text="GPA",command=navigate_to_GPA_page)
            GPA_button.pack(side="top", padx=10)
            GPA_button_label = tk.Label(left_frame, text='GPA', font=("Helvetica", 16), pady=2,bg='white')
            GPA_button_label.pack(side="top",pady=(0,25))
            
            Empty_label = tk.Label(right_frame, text='', font=("Helvetica", 16), pady=2,bg='white')
            Empty_label.pack(side="top",pady=(0,183))







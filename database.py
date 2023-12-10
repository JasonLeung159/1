import mysql.connector
from tkinter import messagebox
class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost", # don't need to change
            user="root", # username
            password="jaymysql",# your mysql password
            database="academic_system2" # database Name
        )
    def close(self):
        self.db.close()
     # ==================================================Student part============================================================
     
    def authenticate(self, username, password):
        cursor = self.db.cursor()
        query = "SELECT Email, login_password,StudentID,StudentName FROM student WHERE Email = %s AND login_password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        return result
    def time_table(self,ID):
        cursor = self.db.cursor()
        query = " SELECT Date, class_arrangements.CourseCode, Course_Group FROM class_arrangements , course_study WHERE class_arrangements.CourseCode = course_study.CourseCode and StudentID = %s"
        cursor.execute(query,[ID])
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result
    
    
    def student_course(self,ID):
        cursor = self.db.cursor()
        query = "select Course.CourseCode, Course.CourseTitle from Course, Course_study where Course.CourseCode = Course_study.CourseCode AND StudentID = %s";
        cursor.execute(query,[ID])
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result
    
    def get_courses_for_date(self,ID,Date):
        cursor = self.db.cursor()
        query = "select Class_arrangements.CourseCode , Course_Group , Date ,Time_Start,Time_End , Venue, Course.CourseTitle from Class_arrangements , Course_study, Course where Class_arrangements.CourseCode = Course_study.CourseCode and Class_arrangements.CourseCode = Course.CourseCode  and StudentID = %s and Date = %s order by Time_start;"
        cursor.execute(query, (ID, Date))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result
    def check_course_attend(self,ID,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT CourseCode,Group_Type,Date,Time FROM Attendance_Record WHERE StudentID = %s AND CourseCode  = %s"
        cursor.execute(query, (ID, CourseCode))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result


    def check_attend(self,ID,Date,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT COUNT(*) FROM Attendance_Record WHERE StudentID = %s AND CourseCode  = %s and Date = %s;"
        cursor.execute(query, (ID, CourseCode, Date))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        if result[0][0] == 1:
            return True
        else:
            return False

    def take_attendance(self,ID,Date,Time,CourseCode,Group_type):
        cursor = self.db.cursor()
        query = "INSERT INTO Attendance_Record (StudentID, Date, Time, CourseCode,Group_Type) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (ID, Date,Time,CourseCode,Group_type))
        self.db.commit()
        cursor.close()

    def get_pesonal_info(self,ID):
        cursor = self.db.cursor()
        query = "SELECT StudentID, StudentName, Year, Age, Gender, PhoneNum,SpLD FROM student WHERE StudentID = %s"
        cursor.execute(query, [ID])
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result

    def update_personal_info(self,ID,name,age,spld,PhoneNum):
        cursor = self.db.cursor()
        query = f"update student set StudentName = '{name}', Age = {age},SpLD = '{spld}', PhoneNum = '{PhoneNum}'  WHERE StudentID = '{ID}'"
        cursor.execute(query)
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result
        
    # ==================================================Teacher part============================================================
    def teacher_authenticate(self, username, password):
        cursor = self.db.cursor()
        query = "SELECT Email, Tlogin_password,TeacherID,TeacherName FROM teacher WHERE Email = %s AND Tlogin_password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        self.db.commit()
        cursor.close()
        return result

    def teacher_course(self,ID):
        cursor = self.db.cursor()
        query = "select Course.CourseCode, Course.CourseTitle,teaching.TeacherID,teaching.CourseLeader from Course , teaching where Course.CourseCode = teaching.CourseCode AND TeacherID = %s"
        cursor.execute(query,[ID])
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result

    def teaching_course_attendance(self, ID, CourseCode):
        cursor = self.db.cursor()
        query = "SELECT teaching.CourseCode,CourseTitle, Course_Group, Date, Time_Start, Time_End, Venue  FROM teaching , Course,class_arrangements where teaching.CourseCode = Course.CourseCode and teaching.CourseCode = class_arrangements.CourseCode and TeacherID = %s and teaching.CourseCode = %s"
        cursor.execute(query,(ID,CourseCode))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result
    
    def course_attendance_TCH(self, ID, CourseCode,Date):
        cursor = self.db.cursor()
        query = "SELECT * FROM Attendance_Record WHERE CourseCode = %s and Date = %s"
        cursor.execute(query,(CourseCode,Date))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result

    def create_course(self,venue, eventname, selected_date, time1, time2,CourseCode):
        cursor = self.db.cursor()
        query = "INSERT INTO class_arrangements (CourseCode, Course_Group, Date, Time_Start, Time_End, Venue) VALUES (%s, %s, %s, %s,%s,%s);"
        cursor.execute(query, (CourseCode, eventname, selected_date, time1, time2, venue))
        self.db.commit()
        cursor.close()
        

    def delete_course(self, CourseCode, Date,Time_Start):
        cursor = self.db.cursor()
        query = "Delete from class_arrangements where CourseCode = %s and Date = %sand Time_Start = %s"
        cursor.execute(query,(CourseCode,Date,Time_Start))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result

    def get_studentID(self,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT StudentID FROM course_study where CourseCode = %s"
        cursor.execute(query,[CourseCode])
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result

    def update_score(self, CourseCode, Score, Percentage, StudentID, Type, Final_score):
        try:
            cursor = self.db.cursor()
            query = "INSERT INTO coursescore (CourseCode, StudentID, Score, Type, ScorePercent, Final_score) VALUES (%s, %s, %s, %s, %s, %s);"
            cursor.execute(query, (CourseCode, StudentID, Score, Type, Percentage, Final_score))
            self.db.commit()
            messagebox.showinfo("Success", "Score updated successfully.")
            cursor.close()
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                messagebox.showinfo("Duplicate Entry", "The data is already in the database.")
            else:
                messagebox.showinfo("Integrity Error", "An integrity error occurred.")
                

    def get_Score(self,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT StudentID StudentID,Type,Score,ScorePercent FROM coursescore where CourseCode = %s"
        cursor.execute(query, [CourseCode])
        result = cursor.fetchall()
        #print(result)
        cursor.close()
        return result


    def get_GPA(self,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT StudentID StudentID,Type,Score,ScorePercent FROM CourseCode where CourseCode = %s"
        cursor.execute(query, [CourseCode])
        result = cursor.fetchall()
        #print(result)
        cursor.close()
        return result

    def count_score(self,CourseCode,StudentID):
        cursor = self.db.cursor()
        query = "SELECT COUNT(*) FROM coursescore WHERE CourseCode = %s and StudentID = %s"
        cursor.execute(query, (CourseCode,StudentID))
        result = cursor.fetchall()
        #print(result)
        cursor.close()
        return result

    def get_all_student(self,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT StudentID FROM coursescore WHERE CourseCode = %s GROUP BY StudentID HAVING COUNT(*)= 3"
        cursor.execute(query, [CourseCode])
        result = cursor.fetchall()
        #print(result)
        cursor.close()
        return result

    def get_student_score(self,CourseCode, StudentID):
        cursor = self.db.cursor()
        query = "SELECT * FROM coursescore WHERE CourseCode = %s and StudentID = %s order by Type"
        cursor.execute(query, (CourseCode,StudentID))
        result = cursor.fetchall()
        #print(result)
        cursor.close()
        return result
    def delete_student_score(self,CourseCode,StudentID,Type):
        cursor = self.db.cursor()
        query = "DELETE FROM coursescore WHERE CourseCode = %s and StudentID = %s and Type = %s;"
        cursor.execute(query,(CourseCode,StudentID,Type))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()


    def update_GPA(self,CourseCode,StudentID,Grade):
        try:
            cursor = self.db.cursor()
            query = "INSERT INTO gpa (CourseCode, StudentID, Grade) VALUES (%s, %s, %s);"
            cursor.execute(query, (CourseCode, StudentID, Grade))
            self.db.commit()
            messagebox.showinfo("Success", "Score updated successfully.")
            cursor.close()
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                messagebox.showinfo("Duplicate Entry", "The data is already in the database.")
            else:
                messagebox.showinfo("Integrity Error", "An integrity error occurred.")

    def get_all_student_GPA(self,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT gpa.StudentID, student.StudentName,Grade FROM gpa, student where gpa.StudentID = student.StudentID and CourseCode= %s"
        cursor.execute(query, [CourseCode])
        result = cursor.fetchall()
        cursor.close()
        return result

    def get_student_thier_GPA(self,StudentID,CourseCode):
        cursor = self.db.cursor()
        query = "SELECT gpa.StudentID, student.StudentName,Grade FROM gpa, student where gpa.StudentID = student.StudentID and CourseCode= %s and gpa.StudentID = %s"
        cursor.execute(query, (CourseCode,StudentID))
        result = cursor.fetchall()
        cursor.close()
        return result

    def delete_student_GPA(self,CourseCode,StudentID):
        cursor = self.db.cursor()
        query = "DELETE FROM gpa WHERE CourseCode = %s and StudentID = %s;"
        cursor.execute(query,(CourseCode,StudentID))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()


    def course_student(self, CourseCode):
        cursor = self.db.cursor(buffered=True)
        query = "SELECT * FROM course_study WHERE CourseCode = %s"
        cursor.execute(query, [CourseCode])
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result

    def delete_course_student(self, CourseCode, StudentID):
        cursor = self.db.cursor()
        query = "Delete from course_study where CourseCode = %s and StudentID = %s"
        cursor.execute(query,(CourseCode,StudentID))
        result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        return result
    
    def create_StudentToCourse(self, CourseCode, StudentID):
        try:
            cursor = self.db.cursor()
            query = "INSERT INTO course_study (CourseCode, StudentID) VALUES (%s, %s);"
            cursor.execute(query,(CourseCode,StudentID))
            self.db.commit()
            cursor.close()
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                messagebox.showinfo("Duplicate Entry", "The data is already study in this course.")
            else:
                messagebox.showinfo("Integrity Error", "An integrity error occurred.")

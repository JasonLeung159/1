import tkinter as tk


class User:
    def __init__(self, username, ID):
        self.username = username
        self.userID = ID

    def get_username(self):
        return self.username

    def get_userID(self):
        return self.userID

    def set_user(self,username,ID):
        self.username = username
        self.userID = ID
class Course:
    def __init__(self, course_code, course_title):
        self.course_code = course_code
        self.course_title = course_title
        

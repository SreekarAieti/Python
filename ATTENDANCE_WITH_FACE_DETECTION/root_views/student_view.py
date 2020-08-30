from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from root_controllers.AuthController import AuthController
from root_controllers.xlsx_controller import Create_attendance_sheet
from tkinter import messagebox
class Student():

    def load(self,av,id,name,role):
        av.master.destroy()
        self.id=str(id).upper()
        self.name=str(name).upper()
        self.role=str(role).upper()
        self.master = None              #main page code
        self.master = Tk()
        self.master.title("STUDENT")
        self.master.geometry("1200x600+175+50")
        self.master.resizable(False, False)       #fix the window size

        # ==bg image ====
        self.bg = ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image = Label(self.master, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        # frame for login
        self.Frame_Login = Frame(self.master, bg="white")
        self.Frame_Login.place(x=150, y=100, height=350, width=650)

        self.bg_f = ImageTk.PhotoImage(Image.open('profile_pic.jpeg'))
        self.bg_f_image = Label(self.Frame_Login, image=self.bg_f).place(x=3, y=3)

        self.l1_id = Label(self.Frame_Login, text="ID :", font=('Impact', 12), fg='#d77337',bg='white').place(x=170, y=15)
        self.l2_name = Label(self.Frame_Login, text="NAME :", font=('Impact', 12), fg='#d77337',bg='white').place(x=170, y=55)
        self.l3_rle = Label(self.Frame_Login, text="ROLE :", font=('Impact', 12), fg='#d77337',bg='white').place(x=170, y=95)
        self.txt_id = Label(self.Frame_Login, text=f"{self.id}", font=('Impact', 12),fg='#d77337',bg="white").place(x=225, y=15)
        self.txt_name = Label(self.Frame_Login, text=f"{self.name}", font=('Impact', 12),fg='#d77337',bg="white").place(x=225, y=55)
        self.txt_role = Label(self.Frame_Login, text=f"{self.role}",font=('Impact', 12),fg='#d77337',bg="white").place(x=225, y=95)
        # student_info button
        Student_info = Button(self.Frame_Login, command=lambda: self.open_info(self.id,self.role), text="View attendance", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=200, y=200, width=150)

        goback_btn=Button(self.Frame_Login,command=lambda :self.log_out(av),text="Log out",bg="#d77337",fg="white",font=("times new roman",10)).place(x=570,y=20,width=50)


        self.popup_student_info = None

        self.master.mainloop()




    def open_info(self,id,role):
        if self.popup_student_info is None or not self.popup_student_info.root_attendance_info.winfo_exists():
            self.popup_student_info = Attendance_info(id,role)
        else:
            self.popup_student_info.root_attendance_info.lift(self.master)

    def log_out(self,av):
        av.load(self)
class Attendance_info:
    def __init__(self,id,role):
        self.root_attendance_info=tk.Toplevel()
        self.root_attendance_info.title("Student_info page")
        self.root_attendance_info.geometry("1200x600+175+50")
        self.root_attendance_info.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_attendance_info,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #goback button
        goback_btn=Button(self.root_attendance_info,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)

        self.Frame_student_att = Frame(self.root_attendance_info, bg="white")
        self.Frame_student_att.place(x=150, y=100, height=350, width=650)
        #get xlsheet
        attandance_today = Button(self.Frame_student_att, command=lambda :self.get_xlsheet(id,role,"today"), text="get TODAY attendance sheet", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=200, y=100, width=200)
        attandance_all = Button(self.Frame_student_att, command=lambda :self.get_xlsheet(id,role,"total"), text="get TOTAL attendance sheet", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=200, y=250, width=200)
    def get_xlsheet(self,id,role,type):
        ac = AuthController()
        data=ac.get_all_students(id)
        if data:
            cas=Create_attendance_sheet()
            file_name= cas.load(id,role,type,data)
            if file_name:
                messagebox.showinfo('xlsx', f"{file_name}\nGenerated Successfully")
        else:
            messagebox.showinfo('Empty',"No records found")

    # window destroy function
    def back(self):
        self.root_attendance_info.destroy()

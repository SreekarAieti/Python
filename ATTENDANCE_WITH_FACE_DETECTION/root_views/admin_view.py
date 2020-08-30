from tkinter import *
import tkinter as tk
import os
import shutil
from tkinter import messagebox
from PIL import ImageTk,Image
from root_views.recongnitionView_OPENCV import Recognition
from root_controllers.face_training_controller_OPENCV import FTC
from root_controllers.AuthController import AuthController
from root_controllers.xlsx_controller import Create_attendance_sheet
class Admin():

    def load(self,av,id,name,role):
        av.master.destroy()
        self.id=str(id).upper()
        self.name=str(name).upper()
        self.role=str(role).upper()
        self.master = None              #main page code
        self.master = Tk()
        self.master.title("ADMIN")
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
        Student_info = Button(self.Frame_Login, command=lambda :self.open_info(self.id,self.role), text="View Attendance", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=50, y=200, width=150)
        #update button
        update = Button(self.Frame_Login, command=self.open_update, text="Update student", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=225, y=200, width=150)

        #delete button
        delete = Button(self.Frame_Login, command=self.open_delete, text="Delete student", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=400, y=200, width=150)
        w=150
        if str(id) == '1':
            add_admin = Button(self.Frame_Login, command=self.add_members, text='Add Members', bg="#d77337", fg="white",
                               font=("times new roman", 13)).place(x=325, y=270, width=150)
            w=0

        #attandance
        attandance = Button(self.Frame_Login, command=self.open_attendance, text="Attendance", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=150, y=270, width=150+w)
        goback_btn=Button(self.Frame_Login,command=lambda :self.log_out(av),text="Log out",bg="#d77337",fg="white",font=("times new roman",10)).place(x=570,y=20,width=50)

        self.popup_student_info = None
        self.popup_update = None
        self.popup_add_members=None
        self.popup_delete = None
        self.popup_attendance=None
        self.list_data=[]
        self.master.mainloop()

    def add_members(self):

        if self.popup_add_members is None or not self.popup_add_members.root_add_members.winfo_exists():
            self.popup_add_members = AddMembers()
        else:
            self.popup_add_members.root_add_members.lift(self.master)


    def open_info(self,id,role):
        if self.popup_student_info is None or not self.popup_student_info.root_attendance_info.winfo_exists():
            self.popup_student_info = Attendance_info(id,role)
        else:
            self.popup_student_info.root_attendance_info.lift(self.master)


    def open_update(self):
        if self.popup_update is None or not self.popup_update.root_update.winfo_exists():
            self.popup_register = Update_page()
        else:
            self.popup_update.root_update.lift(self.master)


    def open_delete(self):
        if self.popup_delete is None or not self.popup_delete.root_delete.winfo_exists():
            self.popup_delete = Delete_page()
        else:
            self.popup_delete.root_delete.lift(self.master)
    def open_attendance(self):
        fce=FTC()
        result=fce.load()
        if result:
            messagebox.showinfo('training','Trained Successfully')
        recog = Recognition()
        if self.popup_attendance is None or not self.popup_attendance.window.winfo_exists():
            self.popup_attendance = recog
            recog.load()
        else:
            self.popup_attendance.window.lift(self.master)


        # ac = AuthController()
        # ac.mark_attendance(self.list_data)
    def log_out(self,av):
        #self.master.destroy()
        av.load(self)

#adding memebers
class AddMembers:
    def __init__(self):
        self.root_add_members=tk.Toplevel()
        self.root_add_members.title("Add members")
        self.root_add_members.geometry("1200x600+175+50")
        self.root_add_members.resizable(False,False)


        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_add_members,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.Frame_add_members = Frame(self.root_add_members, bg="white")
        self.Frame_add_members.place(x=150, y=100, height=350, width=650)

        #widgets
        self.indicate = Label(self.Frame_add_members, text='Enter the Fileds to Add members', font=("times new roman", 18), fg='gray',
                             bg='white').place(
            x=75, y=50)
        self.ladd_id = Label(self.Frame_add_members, text='User_Id', font=("times new roman", 12), fg='gray', bg='white').place(
            x=60, y=100)
        self.eadd_id = Entry(self.Frame_add_members, font=("calibri light", 15), bg="white")
        self.eadd_id.place(x=160, y=100, width=250, height=35)

        self.ladd_role = Label(self.Frame_add_members, text='Role', font=("times new roman", 12), fg='gray', bg='white').place(x=60,
                                                                                                                  y=140)
        self.eadd_role = Entry(self.Frame_add_members, font=("calibri light", 15), bg="white")
        self.eadd_role.place(x=160, y=140, width=250, height=35)

        #button
        self.add_mem_button = Button(self.Frame_add_members, command=lambda: self.to_add(
            self.eadd_id.get(),
            self.eadd_role.get(),
           ), text="Update", bg="#d77337",
                               fg="white", font=("times new roman", 13)).place(x=160, y=200, width=250)

    def to_add(self,id,role):
        self.eadd_role.delete(0, END)
        self.eadd_id.delete(0, END)
        if len(id)!=0 and len(role)!=0:
            if role=='student' or role=='admin':
                ac=AuthController()
                result=ac.adding_members(id,role)
                if result:
                    messagebox.showinfo("Success","id and role are inserted in the database")
                else:
                    messagebox.showinfo("Alert","userid already exists or error in inserting record to the database")
            else:
                messagebox.showinfo('Alert','role must be "admin" or "student" only')
        else:
            messagebox.showinfo("Alert",'Fields cannot be empty')



#student info class
class Attendance_info:
    def __init__(self,id,role):
        self.root_attendance_info=tk.Toplevel()
        self.root_attendance_info.title("Attendance Information page")
        self.root_attendance_info.geometry("1200x600+175+50")
        self.root_attendance_info.resizable(False,False)


        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_attendance_info,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.Frame_att = Frame(self.root_attendance_info, bg="white")
        self.Frame_att.place(x=150, y=100, height=350, width=650)

        #goback button
        goback_btn=Button(self.root_attendance_info,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)

        #get xlsheet
        attandance_today = Button(self.Frame_att, command=lambda :self.get_xlsheet(id,role,"today"), text="get TODAY attendance sheet", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=200, y=100, width=200)
        attandance_all = Button(self.Frame_att, command=lambda :self.get_xlsheet(id,role,"total"), text="get TOTAL attendance sheet", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=200, y=250, width=200)


    def get_xlsheet(self,id,role,type):
        ac = AuthController()
        data=ac.get_all_students()
        if data:
            cas=Create_attendance_sheet()
            file_name= cas.load(id,role,type,data)
            if file_name:
                messagebox.showinfo('xlsx', f"{file_name}\nGenerated Successfully")
        else:
            messagebox.showinfo('Empty',"No records found")

    def back(self):
        self.root_attendance_info.destroy()

#update class
class Update_page:
    def __init__(self):
        self.root_update = tk.Toplevel()
        self.root_update.title("Update page")
        self.root_update.geometry("1200x600+175+50")
        self.root_update.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_update,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #goback button
        goback_btn=Button(self.root_update,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)
        update_frame=Frame(self.root_update,bg="white")
        update_frame.place(x=150, y=50, height=500, width=550)
        search_btn = Button(update_frame, command=lambda: self.search_for_id(self.txt_userid.get()), text="search",
                                 bg="#d77337", fg="white", font=("times new roman", 10)).place(x=425, y=100, width=70)

        self.lbl_name = Label(update_frame, text='User_Id', font=("times new roman", 12), fg='gray', bg='white').place(
            x=60, y=100)
        self.txt_userid = Entry(update_frame, font=("calibri light", 15), bg="white")
        self.txt_userid.place(x=160, y=100, width=250, height=35)
        self.lbl_Id = Label(update_frame, text='Name', font=("times new roman", 12), fg='gray', bg='white').place(x=35,
                                                                                                                 y=140)
        self.txt_name = Entry(update_frame, font=("calibri light", 15), bg="white")
        self.txt_name.place(x=160, y=140, width=250, height=35)

        self.lbl_mail = Label(update_frame, text='Gmail', font=("times new roman", 12), fg='gray', bg='white').place(
            x=35, y=180)
        self.txt_gmail = Entry(update_frame, font=("calibri light", 15), bg="white")
        self.txt_gmail.place(x=160, y=180, width=250, height=35)

        self.lbl_no = Label(update_frame, text='Ph.Number', font=("times new roman", 12), fg='gray', bg='white').place(
            x=35, y=220)
        self.txt_phno = Entry(update_frame, font=("calibri light", 15), bg="white")
        self.txt_phno.place(x=160, y=220, width=250, height=35)
        self.snap_btn = Button(update_frame, command=lambda: self.update_student_data(
                                                                                   self.txt_userid.get(),
                                                                                   self.txt_name.get(),
                                                                                   self.txt_gmail.get(),
                                                                                   self.txt_phno.get(),
                                                                                   ), text="Update", bg="#d77337",
                               fg="white", font=("times new roman", 13)).place(x=160, y=400, width=250)

    def search_for_id(self, id):
        ac = AuthController()
        result = ac.searching_id(id)
        if result:
            self.txt_name.delete(0, END)
            self.txt_gmail.delete(0, END)
            self.txt_phno.delete(0, END)
            self.txt_name.insert(0, result[1])
            self.txt_gmail.insert(0, result[2])
            self.txt_phno.insert(0, result[3])
        else:
            messagebox.showinfo("Alert", "User id not exists")

    def update_student_data(self,id,name,gmail,phone):
        if True in map(lambda item: len(str(item))==0,[id,name,gmail,phone]):
            messagebox.showinfo("Empty Fields", 'Fields cannot be empty')
        else:
            ac=AuthController()
            result=ac.update_student(id,name,gmail,phone)
            if result:
                messagebox.showinfo('Updated','Users data updated')
                # self.root_update.destroy()
            else:
                messagebox.showinfo('some error in inserting')
                self.root_update.destroy()
    #window destroy function
    def back(self):
        self.root_update.destroy()

#delete class
class Delete_page:
    def __init__(self):
        self.root_delete = tk.Toplevel()
        self.root_delete.title("Delete page")
        self.root_delete.geometry("1200x600+175+50")
        self.root_delete.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_delete,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #goback botton
        goback_btn=Button(self.root_delete,command=self.back,text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)
        #frame
        self.delet_frame = Frame(self.root_delete, bg="white")
        self.delet_frame.place(x=150, y=100, height=350, width=650)
        #btn
        #prompt label
        self.label_prompt=Label(self.delet_frame,text='Enter the correct userId  to  delete', font=("times new roman", 15), fg='gray', bg='white').place(x=80,y=80)
        self.txt_userid = Entry(self.delet_frame, font=("calibri light", 15), bg="white")
        self.txt_userid.place(x=80, y=130, width=330, height=35)

        delete = Button(self.delet_frame, command=lambda :self.delete_student(self.txt_userid.get()), text="Delete student", bg="#d77337", fg="white",font=("times new roman", 13)).place(x=400, y=200, width=150)


    #delete_student fun
    def delete_student(self,id):
        if len(str(id))!=0:
            ac = AuthController()
            result = ac.searching_id(id)
            if result:
                result=ac.User_to_delete(id)
                if result!=None:
                    sub_dir=os.path.join('faceDataset/',id)
                    if os.path.exists(sub_dir):
                        shutil.rmtree(sub_dir)
                    messagebox.showinfo('deleted',f'deleted all data of user with id {id} ')
            else:
                messagebox.showinfo("Alert","userid doesnot exists")
        else:
            messagebox.showinfo('Alert',"userid cannot be empty")

    #window destroy function
    def back(self):
        self.root_delete.destroy()


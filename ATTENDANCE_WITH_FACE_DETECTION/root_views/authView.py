from tkinter import *
from tkinter import messagebox
from root_controllers.AuthController import AuthController
from root_views.detectionView import DetectionView
from root_views.admin_view import Admin
from root_views.student_view import Student
from PIL import ImageTk,Image
import os
class AuthView():

    def load(self,ad=None):
        if ad:
            ad.master.destroy()
        self.master=None
        self.master = Tk()
        self.master.title("ATTANDANCE WITH FACIAL RECOGNITION")
        self.master.geometry("1199x600+100+50")
        self.master.resizable(False, False)
        # ==bg image ====
        self.bg = ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image = Label(self.master, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.back_btn = Label(self.master, text="Developed By:", anchor="w", fg="#f05c02",
                              font=("times new roman", 13, "bold")).place(x=30, y=470, width=120, height=20)
        self.back_btn = Label(self.master, text="E Kiran Kumar", anchor="w", fg="#f05c02",
                              font=("times new roman", 13, "bold")).place(x=50, y=500, width=120, height=20)
        self.back_btn = Label(self.master, text="A Sreekar", anchor="w", fg="#f05c02",
                              font=("times new roman", 13, "bold")).place(x=50, y=520, width=100, height=20)
        self.back_btn = Label(self.master, text="C Veeresh", anchor="w", fg="#f05c02",
                              font=("times new roman", 13, "bold")).place(x=50, y=540, width=100, height=20)

        # frame directs to login or register page
        self.Frame_Login = Frame(self.master, bg="white")
        self.Frame_Login.place(x=200, y=100, height=340, width=600)
        title = Label(self.Frame_Login, text="ATTENDACE WITH FACE DETECTION", font=("Impact", 25, "bold"), fg='#d77337',
                      bg='white').place(x=90, y=30)
        self.sub_title = Label(self.Frame_Login, text='Attendance In Modern Way', font=("times new roman", 13),
                               fg='gray', bg='white').place(x=90, y=70)

        #login btn to login page
        login_btn = Button(self.Frame_Login, command=lambda :self.open_login(self), text="LOGIN", bg="#d77337", fg="white",font=("times new roman", 15)).place(x=150, y=200, width=150)

        #register btn to register page
        register_btn = Button(self.Frame_Login, command=lambda :self.open_register(self), text="REGESTER", bg="#d77337", fg="white",font=("times new roman", 15)).place(x=350, y=200, width=150)

        self.popup_login = None
        self.popup_register = None
        self.master.mainloop()



    def open_login(self,av):
        if self.popup_login is None or not self.popup_login.root_login.winfo_exists():
            l=Login_page()
            self.popup_login = l
            l.load(av)
        else:
            self.popup_login.root_login.lift(self.master)
    def open_register(self,av):
        if self.popup_register is None or not self.popup_register.root_register.winfo_exists():
            rp=Register_page()
            self.popup_register = rp
            rp.load(av)
        else:
            self.popup_register.root_register.lift(self.master)


class Login_page:
    def load(self,av):
        self.root_login=av.master
        self.root_login.title("Login page")
        self.root_login.geometry("1199x600+100+50")
        self.root_login.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_login,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #btn destroys courrent login page toplevel window
        self.back_btn=Button(self.root_login,command=lambda :self.back(av),text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)

        # frame for login
        self.Frame_Login = Frame(self.root_login, bg="white")
        self.Frame_Login.place(x=150, y=150, height=340, width=480)

        #lable
        self.title=Label(self.Frame_Login,text="Login Here",font=("Impact",35,"bold"),fg='#d77337',bg='white').place(x=90,y=30)

        #input user id
        self.label_userid=Label(self.Frame_Login,text='User_Id', font=("Goudy old style",15), fg='gray',bg='white').place(x=80,y=100)
        self.txt_userid=Entry(self.Frame_Login,font=("calibri light",15),bg="white")
        self.txt_userid.place(x=80,y=130,width=330,height=35)
        #inut password
        self.label_password = Label(self.Frame_Login,text='Password', font=("Goudy old style", 15), fg='gray',bg='white').place(x=80, y=180)
        self.txt_password = Entry(self.Frame_Login, font=("calibri light", 15),show="*", bg="white")
        self.txt_password.place(x=80, y=210, width=330, height=35)
        #butn to login control
        self.login_btn=Button(self.Frame_Login,command=lambda :self.login_control(av,self.txt_userid.get(),self.txt_password.get()),text="Login",bg="#d77337",fg="white",font=("times new roman",15)).place(x=190,y=300,width=100)
    def back(self,av):
        self.root_login.destroy()
        av.load()
    def login_control(self,av, id, password):
        ac = AuthController()
        message = ac.login(id, password)
        if message:
            self.set_pro_pic(id)
            data_row=message
            if data_row[5]=='student':
                st=Student()
                st.load(av,data_row[0],data_row[1],data_row[5])
            if data_row[5]=='admin':
                ad=Admin()
                ad.load(av,data_row[0],data_row[1],data_row[5])

    def set_pro_pic(self,id):
        image_names = []
        main_dir='faceDataset'
        sub_dir=id
        image=None
        for (_, _, file) in os.walk('faceDataset', topdown=False):

            image_names.extend(file)
        for image_name in image_names:
            _, _id, _ = image_name.split('.', 2)
            if id == _id:
                image=f"{main_dir}/{sub_dir}/{image_name}"
                break

        img = Image.open(image)
        img = img.resize((120, 130), Image.ANTIALIAS)
        img.save('profile_pic.jpeg')
class Register_page:
    def load(self,av):
        self.root_register = av.master
        self.root_register.title("Register page")
        self.root_register.geometry("1199x600+100+50")
        self.root_register.resizable(False,False)

        #==bg image ====
        self.bg=ImageTk.PhotoImage(Image.open("back_ground.jpeg"))
        self.bg_image=Label(self.root_register,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        Login_btn=Button(self.root_register,command=lambda :self.back(av),text="Go back",bg="#d77337",fg="white",font=("times new roman",10)).place(x=10,y=20,width=50)


        Frame_Login = Frame(self.root_register, bg="white")
        Frame_Login.place(x=150, y=50, height=500, width=550)

        self.title=Label(Frame_Login,text="Register Here",font=("Impact",35,"bold"),fg='#d77337',bg='white').place(x=35,y=20)

        self.search_btn = Button(Frame_Login,command=lambda :self.load_label(av,self.txt_userid.get()), text="search",bg="#d77337",fg="white",font=("times new roman", 10)).place(x=425, y=100, width=70)


        self.lbl_name=Label(Frame_Login,text='User_Id',font=("times new roman", 12), fg='gray',bg='white').place(x=60,y=100)
        self.txt_userid=Entry(Frame_Login,font=("calibri light",15),bg="white")
        self.txt_userid.place(x=160,y=100,width=250,height=35)

        self.lbl_Id = Label(Frame_Login, text='Name', font=("times new roman", 12), fg='gray', bg='white').place(x=35,y=140)
        self.txt_name = Entry(Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_name.place(x=160, y=140, width=250, height=35)


        self.lbl_mail = Label(Frame_Login, text='Gmail', font=("times new roman", 12), fg='gray', bg='white').place(x=35,y=180)
        self.txt_gmail = Entry(Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_gmail.place(x=160, y=180, width=250, height=35)


        self.lbl_no = Label(Frame_Login, text='Ph.Number', font=("times new roman", 12), fg='gray', bg='white').place(x=35,y=220)
        self.txt_phno = Entry(Frame_Login, font=("calibri light", 15), bg="white")
        self.txt_phno.place(x=160, y=220, width=250, height=35)


        self.lbl_password = Label(Frame_Login, text='Password', font=("times new roman", 12), fg='gray', bg='white').place(x=35,y=260)
        self.txt_password= Entry(Frame_Login, font=("calibri light", 15),show='*',bg="white")
        self.txt_password.place(x=160, y=260, width=250, height=35)


        self.lbl_confor_password = Label(Frame_Login, text="Conform Password", font=("times new roman", 12), fg='gray',bg='white').place(x=35, y=300)
        self.txt_cpassword = Entry(Frame_Login, font=("calibri light", 15), show="*",bg="white")
        self.txt_cpassword.place(x=160, y=300, width=250, height=35)

        self.lbl_role = Label(Frame_Login, text="Role", font=("times new roman", 12), fg='gray',bg='white').place(x=35, y=340)
        self.txt_role = Label(Frame_Login,text='None', borderwidth=2, relief="groove" ,font=("calibri light", 15), bg="white")
        self.txt_role.place(x=160, y=345, width=250, height=35)

        self.snap_btn = Button(Frame_Login,command=lambda:self.take_snap_control(av,self.txt_userid.get(),
                                                  self.txt_name.get(),
                                                  self.txt_gmail.get(),
                                                  self.txt_phno.get(),
                                                  self.txt_password.get(),
                                                  self.txt_cpassword.get(),
                                                  self.txt_role['text']
                                                  ),text="Take a snap",bg="#d77337",fg="white", font=("times new roman", 13)).place(x=160, y=400, width=250)

        self.Register_btn = Button(Frame_Login,
        command=lambda :self.register_control(av,self.txt_userid.get(),
                                                  self.txt_name.get(),
                                                  self.txt_gmail.get(),
                                                  self.txt_phno.get(),
                                                  self.txt_password.get(),
                                                  self.txt_cpassword.get(),
                                                  self.txt_role['text']
                                                  ),text="Register",bg="#d77337",fg="white",font=("times new roman", 13)).place(x=160, y=450, width=250)


    def back(self,av):
        self.root_register.destroy()
        av.load()
    def load_label(self,av,userid):
      if len(str(userid))==0:
          messagebox.showinfo('Empty Fields','Fields cannot be empty')
      else:
        ac=AuthController()
        #return is list [role in authentic_users,if id exist in users]
        data=ac.check_role(userid)
        if data[0]!=None:
            if data[1]==None:
                self.txt_role['text']=data[0][0]
            else:
                messagebox.showinfo('DB Error','user already exist')
        else:
            messagebox.showinfo('Authentication Error','not authorised users')
    def register_control(self,av,id,name,email,phone, password, conform_password,role):

        if True in map(lambda item: len(str(item)) == 0, [id,name,email,phone, password, conform_password,role]):
            messagebox.showinfo('Empty Feilds', 'fields cannot be empty')
        else:
            if role=='None':

                messagebox.showinfo('Empty Feilds', 'role cannot be None')
            else:
                ac = AuthController()
                id=int(id)
                phone=int(phone)
                message = ac.register(id,name, email, phone, password, conform_password, role)
                if message==True:
                    messagebox.showinfo('Alert Registeration', 'Registered sucessfully')
                    self.root_register.destroy()
                    av.load()
                # else:
                #     messagebox.showinfo(message, "a user with same id already exists\n Try you own id")
    def take_snap_control(self,av, id,name,email,phone, password, conform_password,role):
        if True in map(lambda item: len(str(item)) == 0,[id,name,email,phone, password, conform_password,role]):
            messagebox.showinfo('Empty Feilds take a shanp', 'fields cannot be empty')
            print(list(map(lambda item: len(str(item)) == 0, [id, name, email, phone, password, conform_password, role])))
        else:
            if role == 'None':
                messagebox.showinfo('Empty Feilds', 'role cannot be None')
            else:
                ad = DetectionView(id, name)
                ad.load()



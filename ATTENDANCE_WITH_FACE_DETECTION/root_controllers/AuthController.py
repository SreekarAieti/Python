from root_models.AuthModel import AuthModel
from tkinter import messagebox
from passlib.context import CryptContext
import re

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)


class AuthController:

    def login(self,id,password):

        if len(id) == 0 or len(password) == 0:
            messagebox.showinfo("alert", "fields cannot be empty")
            message = False
            return message

        am = AuthModel()
        result = am.getUser(id,password)

        if result:
            result1 = pwd_context.verify(password, result[4])
            if result1:
                message = result
            else:
                messagebox.showinfo("Alert",'Wrong password')
                message=False

        else:
            messagebox.showinfo("alert", 'User not found')
            message = False

        return message

    def register(self,id,name,email,phone,password,conform_password,role):
        result = re.findall(r"^[A-Za-z\sA-Za-z]*$", name)
        if result and len(str(phone))==10:
            if password==conform_password:
                password=pwd_context.encrypt(password)
                am = AuthModel()
                result = am.createUser(id,name,email,phone,password,role)
                if result==True:
                    return True
                else:
                    return result
            else:
                messagebox.showinfo('password conformation','password conformation failed')
        else:
            messagebox.showinfo("ALERT","Invalid formats of Entry Fields,once check name and phone number field")
    def check_role(self,id):
        am=AuthModel()
        result=am.getUserrole(id)
        if result:
            message=result
        else:
            message=False
        return  message

    def User_to_delete(self,id):
        am=AuthModel()
        result=am.User_delete(id)
        return result

    def mark_attendance(self,list_data):
        if list_data:
            am=AuthModel()
            for i in list_data:
                result=am.update_attendance(i)
                return result
        else:
            print('nothing to update')

    def get_all_students(self,id=None):
        am=AuthModel()
        data=am.get_all(id)
        if data:
            return data
        else:
            return False

    def update_student(self,id,name,email,phone):
        result = re.findall(r"^[A-Za-z\sA-Za-z]*$", name)
        #phno=str(phone)
        if result and len(str(phone))==10:
            am=AuthModel()
            result=am.updating(id,name,email,phone)
            return result
        else:
            messagebox.showinfo("Alert","Invalid filed formats,check user name and phone number field")

    def searching_id(self,id):
        am=AuthModel()
        result=am.get_id(id)
        if result:
            return result
        else:
            return False

    def adding_members(self,id,role):
        am=AuthModel()
        result=am.add_to_table(id,role)
        if result:
            return True
        else:
            return False
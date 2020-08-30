from openpyxl import Workbook, load_workbook
from tkinter import messagebox
import os
import datetime
import pickle
class Create_attendance_sheet():
    def __init__(self):
        self.main_attendance_dir='attendance/'
        self.sub_dir=None
        self.date_today=None
        self.ids_names={}
        self.file_name=None

    def load(self,id,role,type,data):
            #make dir if not exist
            #get the current date
            date_today=str(datetime.datetime.now()).split(" ")[0]
            #collect the names correnponding to ids to project inside xls
            f_handle = open("faces_ids_names.pkl", 'rb')
            self.ids_names = pickle.load(f_handle)
            f_handle.close()
            #get a workbook handler
            attendance_workBook = Workbook()
            # creating worksheet and giving names to column
            attendance_worksheet = attendance_workBook.active
            attendance_worksheet.title = "Total_Attendance"
            #set each column width
            attendance_worksheet.column_dimensions['A'].width=14
            attendance_worksheet.column_dimensions['B'].width=14
            attendance_worksheet.column_dimensions['C'].width=14
            attendance_worksheet.column_dimensions['D'].width=14
            attendance_worksheet.column_dimensions['E'].width=14
            #append the column names
            attendance_worksheet.append(('attendance_Id','student_Id','student_name','date','time','status'))
            count=0
            #entering the data where the date is date_today
            if type=="today":
               if role=='STUDENT':
                     for a in data:
                        if a[2] == date_today and str(a[1])==str(id):
                            count+=1
                            attendance_worksheet.append((a[0], a[1],self.ids_names[a[1]], a[2], a[3], a[4],))

               if role=='ADMIN':
                    for a in data:
                      if a[2] == date_today:
                          count+=1
                          attendance_worksheet.append((a[0], a[1],self.ids_names[a[1]], a[2], a[3], a[4],))


            #entering the entire data to worksheet
            else:
                if role == 'STUDENT':
                     for a in data:
                        if str(a[1]) == str(id):
                            count += 1
                            date = str(a[2])
                            attendance_worksheet.append((a[0], a[1], self.ids_names[a[1]],date, a[3], a[4],))
                if role=='ADMIN':
                     for a in data:
                        count += 1
                        date=str(a[2])
                        attendance_worksheet.append((a[0], a[1], self.ids_names[a[1]],date, a[3], a[4]))

            if count==0:
                messagebox.showinfo("Not Found","No records today")
            else:
                self.mak_dir(self.main_attendance_dir, role)
                if type=='today':
                    self.file_name = f"{self.main_attendance_dir}/{role}/{date_today}_attendance.xlsx"
                else:
                    self.file_name = f"{self.main_attendance_dir}/{role}/Total_attendance.xlsx"
                attendance_workBook.save(filename=self.file_name)
                return self.file_name

            #return the generated file name to show in message box in student_info class
            return False
    def mak_dir(self,attendance_dir,role_dir):
        dir = os.path.dirname(attendance_dir)
        if not os.path.exists(dir):
            os.makedirs(dir)
        sub_dir = os.path.join(attendance_dir, role_dir)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)

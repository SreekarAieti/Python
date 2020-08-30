from tkinter import *
import tkinter as tk
from cv2 import cv2
from PIL import Image           # pip install pillow
from PIL import ImageTk
import threading
from tkinter import messagebox
import datetime,time
import os

class DetectionView:
    def __init__(self,id,name):
        self.t=None
        self.stop = False
        self.capture = False
        self.camera_port = 0
        self.image_dir = "faceDataset/"
        self.user_folder=None
        self.current_datetime = datetime.datetime.now()
        self.face_id = id#input('enter your id')
        self.user_name = name#input("enter you name")
        self.vid_cam = cv2.VideoCapture(self.camera_port, cv2.CAP_DSHOW)
        self.face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.count = 1
        self.path_exists(self.image_dir)
        self.path_exists(self.image_dir, self.face_id)


    def path_exists(self, main_dir, sub_dir=""):
        dir = os.path.dirname(main_dir)
        if not os.path.exists(dir):
            os.makedirs(dir)
            return
        sub_dir = os.path.join(main_dir, sub_dir)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
            return
    def load(self):
        self.window = tk.Toplevel()
        self.window.title("Capture photos")
        frame = Frame(self.window,bg="#d77337",padx=10,pady=10)
        frame.grid(row=0,column=0,padx=10,pady=10)

        self.l1 = Label(frame)
        self.l1.grid(row=0,column=0,columns=3,pady=5)

        b2 = Button(frame, text="close", command=self.stopCamera,pady=5)
        b2.grid(row=1, column=0 ,stick='nesw',pady=5)

        b2 = Button(frame, text="capture", command=self.captureCamera, pady=5)
        b2.grid(row=1, column=2, stick='nesw', pady=5)

        self.l2 = Label(frame,text="capture exactly 5 photos",font=('Courier',10),pady=10)
        self.l2.grid(row=2,column=0,columns=3,stick='nesw',pady=5)

        self.startCamera()
        self.window.mainloop()

    def startCamera(self):
        self.t = threading.Thread(target=self.webcam,args=())
        self.t.start()

    def webcam(self):

        self.user_folder = os.path.join(self.image_dir, self.face_id)
        while (True):
            _, image_fram = self.vid_cam.read()
            image_frame = cv2.cvtColor(image_fram, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:

                if self.capture and self.count<6:
                    cv2.imwrite(f"{self.user_folder}/{self.user_name}.{self.face_id}.{self.count}.jpg",
                                image_fram)  # [y+5:y + h+5, x+5:x + w+5]
                    cv2.rectangle(image_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    time.sleep(0.05)
                    self.count += 1
                    self.capture = False
                if self.count>=6:
                    cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255,0,0), 3)
                    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                    cv2.putText(image_frame,f'cannot capture more than {self.count-1}',(x - 100, y - 60),font, 0.8, (0, 255, 0), 1)
                    self.capture = False
                else:
                    cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
                    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                    cv2.putText(image_frame,
                                f"{self.user_name}/{self.face_id}\n-count{self.count-1}--{self.current_datetime}",
                                (x - 100, y - 60),
                                font, 0.8, (0, 255, 0), 1)
                self.path_exists(self.image_dir, self.face_id)

            self.img = Image.fromarray(image_frame)
            imgtk = ImageTk.PhotoImage(self.img)

            # push the image into the tkinter label
            self.l1.config(image=imgtk)
            if self.stop!=True:
               self.l1.image = imgtk
            else:
              self.l1.image = None
              self.stop = False
              self.vid_cam.release()
              cv2.destroyAllWindows()
              self.window.destroy()
              break


    def stopCamera(self):
        self.stop = True



    def captureCamera(self):
        self.capture=True

# dd=DetectionView('1','a')
# t2=threading.Thread(target=dd.load(),args=())
# dd=DetectionView('1','a')
# dd.load()





from tkinter import *
import tkinter as tk
from cv2 import cv2 #if this line doen't work go for the below one
from PIL import Image  # pip install pillow
from PIL import ImageTk
from root_controllers.AuthController import AuthController
import threading
import pickle
from tkinter import messagebox


class Recognition:

    def __init__(self):
        self.stop = False
        self.close=False

        self.known_ids_names = {}

        self.present_ids=[]
        self.process_this_frame = True
        self.camera_port=0
        self.vid_cam = cv2.VideoCapture(self.camera_port,cv2.CAP_DSHOW)
        self.face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trained_dataset.yml')
        self.load_pkl_file()
    def load_pkl_file(self):

        f_handle = open("faces_ids_names.pkl", 'rb')
        self.known_ids_names= pickle.load(f_handle)
        f_handle.close()
    def load(self):
        self.window = tk.Toplevel()
        self.window.title("Auto attendance ap")
        frame = Frame(self.window, bg="#d77337", padx=10, pady=10)
        frame.grid(row=0, column=0, padx=10, pady=10)

        self.l1 = Label(frame)
        self.l1.grid(row=0, column=0, columns=3, pady=5)

        b1 = Button(frame, text="start", command=self.startCamera, pady=5)
        b1.grid(row=1, column=0, stick='nesw', pady=5)

        b2 = Button(frame, text="stop", command=self.stopCamera, pady=5)
        b2.grid(row=1, column=1, stick='nesw', pady=5)

        b2 = Button(frame, text="close", command=self.closeCamera,pady=5)
        b2.grid(row=1, column=2, stick='nesw', pady=5)

        self.l2 = Label(frame, text="Camera started", font=('Courier', 10), pady=20)
        self.l2.grid(row=2, column=0, columns=3, stick='nesw', pady=5)

        self.startCamera()
        self.window.mainloop()

    def startCamera(self):
        t = threading.Thread(target=self.webcam, args=())
        try:
            t.start()
        except:
            pass

    def webcam(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        while True:
            ret, fram = self.vid_cam.read()
            frame=cv2.cvtColor(fram, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
            faces = self.face_cas.detectMultiScale(gray, 1.3, 7)
            for (x, y, w, h) in faces:
                img = gray[y:y + h, x:x + w]
                id, conf = self.recognizer.predict(img)
                if conf < 50:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, str(id) + self.known_ids_names[id] + "%.2f"%(conf), (x, y - 10), font, 0.55, (120, 255, 120), 1)
                    if id not in self.present_ids:
                        self.present_ids.append(id)
            self.img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(self.img)

            # push the image into the tkinter label
            try:
                self.l1.config(image=imgtk)
            except:
                pass
            if self.stop != True:
                self.l1.image = imgtk
            else:
                self.l1.image=None
                self.stop=False
                return

    def stopCamera(self):

        self.stop = True

    def closeCamera(self):
        self.vid_cam.release()
        cv2.destroyAllWindows()
        self.window.destroy()
        if self.present_ids:
            ac = AuthController()
            result=ac.mark_attendance(self.present_ids)
            if result:
                messagebox.showinfo("attendance","marked successfully")
            else:
                messagebox.showinfo("alert"," error")




# r=Recognition()
# print(r.load())







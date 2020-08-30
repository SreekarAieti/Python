import cv2
import os
import numpy as np
import pickle
from PIL import Image


class FTC:
    def load(self):
        self.faces_ids_names={}
        self.image_names = []
        self.existing_faces=[]
        self.existing_ids=[]
        self.main_image_dir = 'faceDataset/'
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.make_training_yml()
        self.dict_pkl_file()
        return self.faces_ids_names


    def make_training_yml(self):
        for (_, _, file) in os.walk('faceDataset', topdown=False):
            self.image_names.extend(file)
        for image_name in self.image_names:
            user_name, id, _ = image_name.split('.', 2)
            image_path = f"{self.main_image_dir}{id}/{image_name}"
            Id = int(image_path.split('.', 2)[1])
            # loading the image and converting it to gray scale
            pilImage = Image.open(f"{image_path}").convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            # extract the face from the training image sample
            faces = self.detector.detectMultiScale(imageNp)
            # If a face is there then append that in the list as well as Id of it
            for (x, y, w, h) in faces:
                self.existing_faces.append(imageNp[y:y + h, x:x + w])
                self.existing_ids.append(Id)
                self.faces_ids_names[Id] = image_name.split('.')[0]
        s = self.recognizer.train(self.existing_faces, np.array(self.existing_ids))
        self.recognizer.write('trained_dataset.yml')
    def dict_pkl_file(self):
        my_path="faces_ids_names.pkl"
        f_handle=open(my_path,'wb')
        pickle.dump(self.faces_ids_names,f_handle)
        f_handle.close()



# fce=FTC()
# d=fce.load()
# print(d)
# print(fce.existing_ids)
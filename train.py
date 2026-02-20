from tkinter import*
from tkinter import ttk
from tkinter import Entry
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import threading 



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="Red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"collage_images\1_FwgSuwjS8YP9UTYsr8SQ4Q.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)  
        self.photoimg_top= ImageTk.PhotoImage(img_top)     
        
        label2 = Label(self.root, image=self.photoimg_top)  
        label2.place(x=0, y=55, width=1530, height=325)

        #=====button====
        b1_text = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_text.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open(r"collage_images\360_F_799320929_gFM0CXd3dfJ2brnXzcUAfBVpo9RtogJq.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)  
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)     
        
        label2 = Label(self.root, image=self.photoimg_bottom)  
        label2.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        t = threading.Thread(target=self._train)
        t.start()

    def _train(self):
       data_dir=("data")
       path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

       faces=[]
       ids=[]

       for image_path in path:
            img=Image.open(image_path).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image_path)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)

       ids=np.array(ids)

       clf=cv2.face.LBPHFaceRecognizer_create()
       clf.train(faces,ids)
       clf.write("classifier.xml")
       cv2.destroyAllWindows()
       messagebox.showinfo("Result","Training datasets completed!!")      

    








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()        

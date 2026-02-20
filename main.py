from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student
import os



class Face_Recoginition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x790+0+0")
        self.root.title("face Recognition System")
        
        # First image
        img = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\faceimage.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        
        label = Label(self.root, image=self.photoimage)
        label.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\1_FwgSuwjS8YP9UTYsr8SQ4Q.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)   
        self.photoimage1 = ImageTk.PhotoImage(img1)     
        
        label1 = Label(self.root, image=self.photoimage1)   
        label1.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\a-collage-displaying-diverse-faces-with-facial-recognition-technology-overlays-each-person-shows-a-unique-expression-highlighting-the-advancement-in-identification-tec.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)  
        self.photoimage2 = ImageTk.PhotoImage(img2)     
        
        label2 = Label(self.root, image=self.photoimage2)  
        label2.place(x=1000, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\pngtree-abstract-technology-big-data-background-concept-generate-ai-image_15686420.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)  
        self.photoimage3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimage3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #Student button
        img4 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\student.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimage4, command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_text = Button(bg_img, text="Student Details", command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_text.place(x=200, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\face detector.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)  

        b2 = Button(bg_img, image=self.photoimage5, cursor="hand2")   
        b2.place(x=500, y=100, width=220, height=220)

        b2_text = Label(bg_img, text="Face Detector", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_text.place(x=500, y=300, width=220, height=40)


       # Attendance face button
        img6 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\attendance.webp")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimage6 = ImageTk.PhotoImage(img6)  

        b3 = Button(bg_img, image=self.photoimage6, cursor="hand2")   
        b3.place(x=800, y=100, width=220, height=220)

        b3_text = Label(bg_img, text="Attendance", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_text.place(x=800, y=300, width=220, height=40)


        #Help face button
        img7 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\images.png")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimage7 = ImageTk.PhotoImage(img7)  

        b4 = Button(bg_img, image=self.photoimage7, cursor="hand2")   
        b4.place(x=1100, y=100, width=220, height=220)

        b4_text = Label(bg_img, text="Help Desk", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_text.place(x=1100, y=300, width=220, height=40)


        #Train face button
        img8 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\traindata.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimage8 = ImageTk.PhotoImage(img8)  

        b5 = Button(bg_img, image=self.photoimage8, cursor="hand2")   
        b5.place(x=200, y=380, width=220, height=220)

        b5_text = Label(bg_img, text="Train Data", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_text.place(x=200, y=580, width=220, height=40)


        #Photos face button
        img9 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\photos.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimage9 = ImageTk.PhotoImage(img9)  

        b6 = Button(bg_img, image=self.photoimage9, cursor="hand2",command=self.open_img)   
        b6.place(x=500, y=380, width=220, height=220)

        b6_text = Label(bg_img, text="Photos",cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_text.place(x=500, y=580, width=220, height=40)


        #Developer face button
        img10 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\images (2).jpeg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimage10 = ImageTk.PhotoImage(img10)  

        b7 = Button(bg_img, image=self.photoimage10, cursor="hand2")   
        b7.place(x=800, y=380, width=220, height=220)

        b7_text = Label(bg_img, text="Developer", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_text.place(x=800, y=580, width=220, height=40)


        #Exit face button
        img11 = Image.open(r"C:\Users\rajes\OneDrive\Desktop\Face_recoginition system\collage_images\images (4).jpeg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimage11 = ImageTk.PhotoImage(img11)  

        b8 = Button(bg_img, image=self.photoimage11, cursor="hand2")   
        b8.place(x=1100, y=380, width=220, height=220)

        b8_text = Label(bg_img, text="Exit", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_text.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
              os.startfile("data")
              
            

        #================Functions Button==============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
         
                  
 
 
 
 


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition_System(root)
    root.mainloop()

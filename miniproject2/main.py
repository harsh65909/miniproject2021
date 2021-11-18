from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class miniproject:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face recognition system")

        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\miniproject2\images\download.png")
        img=img.resize((415,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=415,height=130)

        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\miniproject2\images\download.png")
        img1=img1.resize((415,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=415,y=0,width=415,height=130)

        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\miniproject2\images\download.png")
        img2=img2.resize((415,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=830,y=0,width=415,height=130)


        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\miniproject2\images\download.png")
        img3=img3.resize((415,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1245,y=0,width=415,height=130)

        #bg image
        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\miniproject2\images\bg1.jpeg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="face recognition attendence system",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student Button
        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\miniproject2\images\studentbutton.png")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)



 




if __name__ == "__main__":
    root=Tk()
    obj=miniproject(root)
    root.mainloop()

 
from deepface import DeepFace
import cv2
from PIL import ImageTk, Image
import PIL.Image
from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Face Recognition")
frame1=Frame(window)
frame1.pack()
frame5=Frame(window)
frame5.pack()
frame4=Frame(window)
frame4.pack()
frame2=Frame(window)
frame2.pack()
frame3=Frame(window)
frame3.pack()

photo1=ImageTk.PhotoImage(PIL.Image.open("./d1.jpg"))

photo2=ImageTk.PhotoImage(PIL.Image.open("./d2.jpg"))

lb0=Label(frame1, text="Face Recognition" , font=("Arial", 25))
lb0.pack(side="top")

lb0=Label(frame1, image=photo1)
lb0.pack(side="left")

lb1=Label(frame1, image=photo2)
lb1.pack()


image1=cv2.imread('F:\\UOC Physical\\d1.jpg')
image2=cv2.imread('F:\\UOC Physical\\d2.jpg')
result = DeepFace.verify(image1,image2)
print("Is same face = ",result["verified"])
accuracy=round(((1-result["distance"])*100), 2)
strMatching =str(accuracy)+"%  Matching" 
print("Out put = {")
for key, value in result.items():
    print(key, ' : ', value)
print("}")
var = StringVar()
var1 = StringVar()
var2 = StringVar()
res="YES" if result["verified"] else "No"
strLbl="Same person ? " + res

strNotLined=str(result)
strLined=strNotLined.replace(',', " \n")
var.set(strLined)
var1.set(strLbl)
var2.set(strMatching)
lb1=Label(frame5, textvariable = var2,font=("Arial", 18))
lb1.pack()
lb1=Label(frame2, text="Output =",font=("Arial", 18))
lb1.pack()
lb1=Label(frame3, textvariable = var,font=("Arial", 15))
lb1.pack()
lb1=Label(frame4, textvariable = var1,font=("Arial", 18))
lb1.pack()
window.mainloop()

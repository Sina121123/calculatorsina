from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import *
root = Tk()
img = None
label1 = None
root.geometry('1920x1080')
cimage = "flower1.jpg"
# Functions
def rightpic() :
    global cimage
    if cimage == "flower1.jpg" :
        label1.grid_forget()
        label2.grid()
        cimage = "flower2.jpg"
        print("flower1skip")
    elif cimage == "flower2.jpg" :
        label2.grid_forget()
        label3.grid()
        cimage = "flower3.jpg"
        print("flower2skip")
    elif cimage == "flower3.jpg" :
        label3.grid_forget()
        label4.grid()
        cimage = "flower4.jpg"
        print("flower3skip")
    elif cimage == "flower4.jpg" :
        label4.grid_forget()
        label1.grid()
        cimage = "flower1.jpg"
        print("flower4skip")
def start() :
    global cimage
    label1.grid(row=0)
    buttonright.place(x=900, y=950)
    buttonclose.place(x=700, y=950)
def close() :
    global cimage
    if cimage == "flower1.jpg" :
        label1.grid_forget()
        buttonclose.place_forget()
        buttonright.place_forget()
        print("closed1")
    elif cimage == "flower2.jpg" :
        label2.grid_forget()
        buttonclose.place_forget()
        buttonright.place_forget()
        print("closed2")
    elif cimage == "flower3.jpg" :
        label3.grid_forget()
        buttonclose.place_forget()
        buttonright.place_forget()
        print("closed3")
    elif cimage == "flower4.jpg" :
        label4.grid_forget()
        buttonclose.place_forget()
        buttonright.place_forget()
        print("closed4")

buttons = Button(root,text = "Start!",command=start , bg = "#29a8ab",fg="#cccccc" , padx = 50 ,font=('Helvetica 19 bold'))
buttons.place(x=960,y=540)

buttonright= Button(root,text = "Next!",command=rightpic , bg = "#0e9aa7",fg="#f6cd61" , padx = 50 ,font=('Helvetica 19 bold'))
# buttonright.place(x=900, y=950)
buttonclose= Button(root,text = "Close!",command=close , bg = "#0e9aa7",fg="#f6cd61" , padx = 50 ,font=('Helvetica 19 bold'))





image1 = Image.open("flower1.jpg")
image1 = image1.resize((1920,950) , Image.ANTIALIAS)
image12 = ImageTk.PhotoImage(image1)
label1 = Label(root,image=image12)

image2 = Image.open("flower2.jpg")
image2 = image2.resize((1920,950) , Image.ANTIALIAS)
image13 = ImageTk.PhotoImage(image2)
label2 = Label(root,image=image13)

image3 = Image.open("flower3.jpg")
image3 = image3.resize((1920,950) , Image.ANTIALIAS)
image14 = ImageTk.PhotoImage(image3)
label3 = Label(root,image=image14)

image4 = Image.open("flower4.jpg")
image4 = image4.resize((1920,950) , Image.ANTIALIAS)
image15 = ImageTk.PhotoImage(image4)
label4 = Label(root,image=image15)

# label1.grid(row = 0)

mainloop()

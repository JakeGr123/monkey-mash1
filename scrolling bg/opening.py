from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

root = Tk()


root.title("Monkey Mash")
root.geometry('1200x800')
bg = PhotoImage(file = "beach1.png")
image = Image.open("beach1.png")

resize_image = image.resize((1200, 800))
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img)
label1.image = img
label1.pack()

root.config(bg='green')
scoop = Button(text='Play', command=root.destroy)
scoop.config(bg='dark green')
scoop.place(x=510, y=400)
myFont = font.Font(family='Helvetica')


scoop1 = Button(text='In this game you are trying to keep the monkey safe!\nControl the monkey using W, A, S, D to keep him alive!', )
scoop1.config(bg='dark green')
scoop1['font'] = myFont
scoop1.place(x=350, y=350)
root.mainloop()



from main1 import *
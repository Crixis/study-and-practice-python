from tkinter import *
from PIL import Image, ImageTk

ventana=Tk()
ventana.geometry("700x500")

Label(ventana, text="soy cris").pack(anchor=W)

imagen=Image.open("./21-tkinter/husky.jpg")
render=ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack

ventana.mainloop()
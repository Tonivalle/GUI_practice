
#importamos tkinter
from tkinter import *

#abrir la ventana y titulo

window = Tk()
window.title("GUI")
#configurando el color de fondo
window.configure(background='black')
#imagen

photo = PhotoImage(file='Allmight.png')
Label (window, image = photo, bg='black') .grid(row=0, column=0, sticky=W)
#loop principal

window.mainloop()

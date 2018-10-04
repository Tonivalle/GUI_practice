
#importamos tkinter
from tkinter import *

#funciones(teclas,etc)(se crea despues de la entrada de texto para admitirlo)
def click():
    entered_text = textentry.get()#coge el texto de textentry
    Label (window, text = 'Everything will be OK, '+ entered_text
        + '\n PLUS ULTRA', bg = 'black', fg = 'white',
        font= 'Arial 12 bold') .grid(row =1, column = 0, sticky = S )
#abrir la ventana y titulo

window = Tk()
window.title("GUI")
#configurando el color de fondo
window.configure(background='black')
#imagen

photo = PhotoImage(file='Allmight.png')
Label (window, image = photo, bg='black') .grid(row=0, column=0, sticky=W)

#etiqueta con texto

Label (window, text = 'Enter name', bg = 'black', fg = 'white',
    font= 'Arial 12 bold') .grid(row =1, column = 0, sticky = S )

#texto de entrada

textentry = Entry(window, width = 20, bg='white')
textentry.grid(row = 2, column=0, sticky=S)

#boton width puede ser lo que mida la palabra del boton

Button(window, text='CHEER', width = 6, command=click).grid(row = 3,
    column=0, sticky=S)

#loop principal

window.mainloop()

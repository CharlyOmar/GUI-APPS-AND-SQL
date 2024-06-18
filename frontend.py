"""Un prograama que almacene la siguiente información de los libros:
titulo, autor, año, isbn
"""
from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list.curselection()[0]
        selected_tuple=list.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list.delete(0, END)
    for row in backend.view():
        list.insert(END, row)

def search_command():
    list.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list.insert(END, row)

def insert_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list.delete(0, END)
    list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window=Tk()
window.wm_title("Tienda de libros")

l1=Label(window, text="Titulo")
l1.grid(row=0, column=0)

l2=Label(window, text="Autor")
l2.grid(row=0, column=2)

l3=Label(window, text="Año")
l3.grid(row=1, column=0)

l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)
 
title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list = Listbox(window, height=6, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="Ver todo", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Buscar", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Añadir datos", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Actualizar", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Borrar", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Cerrar", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
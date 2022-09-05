from tkinter import ttk, Tk, Label, LEFT, RIGHT, Y, X, Scrollbar, Button, END, Entry, Frame, Listbox

import pickle
from modules.IslaiduIrasas import Irasas, IslaiduIrasas
from modules.PajamuIrasas import Irasas, PajamuIrasas
from modules.Biudzetas import Biudzetas

def addincome():
    income = float(entry1.get())
    entry1.delete(0,END)
    biudzetas.prideti_pajamu_irasa(income)
    atnaujinti()

def addexpense():
    expense = float(entry2.get())
    biudzetas.prideti_islaidu_irasa(expense)
    atnaujinti()


def atnaujinti():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    listbox.delete(0,END)
    listbox.insert(END, *biudzetas.zurnalas)
    label3['text'] = f"Balansas: {biudzetas.gauti_balansa()}"

def istrinti():
    biudzetas.zurnalas.pop(listbox.curselection()[0])
    biudzetas.irasyti_ataskaita()
    atnaujinti()

def update_item():
    biudzetas.zurnalas[listbox.curselection()[0]].suma = float(entry3.get())
    biudzetas.irasyti_ataskaita()
    atnaujinti()


biudzetas = Biudzetas()

langas = Tk()
langas.geometry("600x750")
langas.title("Biudzetas")
frame1 = Frame(langas)
label1 = Label(langas, text="Iveskite pajamas")
entry1 = Entry(langas, width= 35)
mygtukas1 = Button(langas, text="Patvirtinti", command=addincome)

frame1.pack(pady=3)
label1.pack(pady=3)
entry1.pack(pady=3)
mygtukas1.pack(pady=3)

frame2 = Frame(langas)
label2 = Label(langas, text="Iveskite islaidas")
entry2 = Entry(langas,width= 35)
mygtukas2 = Button(langas, text="Patvirtinti", command=addexpense)

frame2.pack(pady=3)
label2.pack(pady=3)
entry2.pack(pady=3)
mygtukas2.pack(pady=3)

frame3 = Frame(langas)
label3 = Label(langas, text=f"Balansas: {biudzetas.gauti_balansa()}")

frame3.pack()
label3.pack( pady=30)

frame4 = Frame(langas)
label4 = Label(langas, text="Ataskaita: ")
scrollbar = Scrollbar(frame4)
listbox = Listbox(frame4, yscrollcommand=scrollbar.set, width=90, height=20)
scrollbar.config(command=listbox.yview())
listbox.insert(END, *biudzetas.zurnalas)
mygtukas3 = Button(langas, text="Atnaujinti", command=update_item)
label5 = Label(langas, text="Iveskite atnaujinta suma:")
entry3 = Entry(langas)
mygtukas4 = Button(langas, text="Istrinti", command=istrinti)


label4.pack()
frame4.pack()


scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT)
label5.pack()
entry3.pack()
mygtukas3.pack()

mygtukas4.pack()

langas.mainloop()

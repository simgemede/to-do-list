import tkinter
from tkinter import *

PenceereArkaPlani = "#e2e2e2"
WidgetRengi = "#7c7578"
ListboxRengi = "#ffffff"

Font1 = ("Cambria", 10)
Font2 = ("Times New Roman", 12)

pencere = tkinter.Tk()
pencere.title("To Do List")
pencere.iconbitmap("Webalys-Kameleon.pics-Checklist.ico")
pencere.resizable(False,False)
pencere.geometry("400x450")
pencere.config(bg=PenceereArkaPlani)

def add():
    if listEntry.get() == "":
        pass
    else:
        listBox.insert(END, listEntry.get())
    listEntry.delete(0, END)

def remove():
    listBox.delete(0,END)

def clear():
    listEntry.delete(0,END)

def save():
    with open("checklist.txt","w") as f:
        listBoxTuple = listBox.get(0,END)
        for item in listBoxTuple:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item+"\n")

Frame1 = tkinter.Frame(pencere, bg=PenceereArkaPlani)
Frame2 = tkinter.Frame(pencere, bg=PenceereArkaPlani)
Frame3 = tkinter.Frame(pencere, bg=PenceereArkaPlani)
Frame1.pack()
Frame2.pack()
Frame3.pack()

removeImage = tkinter.PhotoImage(file="Delete-icon.png")
clearImage = tkinter.PhotoImage(file="Clear-icon.png")
saveImage = tkinter.PhotoImage(file="Save-icon.png")
quitImage = tkinter.PhotoImage(file="delete-1-icon.png")
addImage = tkinter.PhotoImage(file="add-1-icon.png")

listEntry = tkinter.Entry(Frame1, width=40,
                          borderwidth=3, font=Font2, bg=WidgetRengi)
addtoList = tkinter.Button(Frame1, text="Ekle", image=addImage,
                           bg=PenceereArkaPlani,command=add)
listEntry.grid(row=0, column=0, padx=5, pady=(10, 0))
addtoList.grid(row=0, column=1, padx=5, pady=(7, 0))

scrollBar = tkinter.Scrollbar(Frame2,bg=ListboxRengi)
listBox = tkinter.Listbox(Frame2, height=18,
                          width=53, font=Font1,borderwidth=3,bg=ListboxRengi,
                          yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)
listBox.grid(row=1,column=0)
scrollBar.grid(row=1,column=1,sticky="NS")

removeButton = tkinter.Button(Frame3, image=removeImage,
                              bg=PenceereArkaPlani, command=remove)
clearButton = tkinter.Button(Frame3, image=clearImage,
                             bg=PenceereArkaPlani, command=clear)
saveButton = tkinter.Button(Frame3, image=saveImage,
                             bg=PenceereArkaPlani, command=save)
quitButton = tkinter.Button(Frame3, image=quitImage,
                             bg=PenceereArkaPlani, command=exit)

removeButton.grid(row=0,column=0)
clearButton.grid(row=0,column=1)
saveButton.grid(row=0,column=2)
quitButton.grid(row=0,column=3)

pencere.mainloop()

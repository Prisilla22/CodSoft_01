from tkinter import*
from tkinter.font import Font

top = Tk()
top.title('To-Do List Application')
top.geometry("500x500")

#Define the font
font = Font(
    family="Footlight MT Light",
    size = 30,
    weight="bold")
#Create Frame
frame = Frame(top)
frame.pack(pady=10)

#Create listbox
_list = Listbox(frame,font=font,width=25,height=5,bg="#29A2D3",bd=0,fg="#FFFFFF" )

_list.pack(side=LEFT, fill=BOTH)

things = ["Do Exercise","Drink Water","Water plants","Wash the Car","Buy Groceries"]

for item in things:
    _list.insert(END, item)

# Add scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=_list.yview)

#create an entry box
entry = Entry(top, font=("Helvetica, 24"))
entry.pack(pady=20)

#create a button frame
button_frame = Frame(top)
button_frame.pack(pady=20)

#Functions
def delete_item():
    _list.delete(ANCHOR)

def add_item():
    _list.insert(END, entry.get())
    entry.delete(0, END)

def complete_item():
    _list.itemconfig(
        _list.curselection(),
        fg="#050505")
    _list.selection_clear(0, END)

def uncomplete_item():
    _list.itemconfig(
        _list.curselection(),
        fg="#464646")
    _list.selection_clear(0, END)



#buttons
Delete_button = Button(button_frame, text="Delete Item", command=delete_item)
Add_button = Button(button_frame, text="Add Item", command=add_item)
Cross_Off_button = Button(button_frame, text="Complete", command=complete_item)
Uncross_button = Button(button_frame, text="Uncomplete", command=uncomplete_item)


Delete_button.grid(row=0, column=0)
Add_button.grid(row=0, column=1, padx=20)
Cross_Off_button.grid(row=0, column=2)
Uncross_button.grid(row=0, column=3, padx=20)


top.mainloop()
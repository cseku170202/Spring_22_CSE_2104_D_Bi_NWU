from tkinter import *
import tkinter.messagebox as messagebox

def reset_program():
    my_list.delete(0, END)  # Clear the listbox
    search_entry1.delete(0, END)  # Clear the search entry
    value_entry.delete(0, END)  # Clear the value entry
    start_page.tkraise()

def search_data():
    data = search_entry1.get()
    if data in my_list.get(0, END):
        messagebox.showinfo("Congratulations", "Search data found")
    elif data not in my_list.get(0,END):
        messagebox.showerror("Sorry", "Data not found")

#code for update value start
def update_data(value):
    my_list.delete(ANCHOR)
    my_list.insert(ANCHOR,value)
#code for update value end

#code for remove value start
def remove_data():
    my_list.delete(ANCHOR)
#code for remove value end

#code for insert value start
def insert_data(data):

    selected_item = my_list.get(my_list.curselection())
    if selected_item in list:
       my_list.delete(ANCHOR)

    #list.append(data)
    my_list.insert(ANCHOR,data)

#code for insert value end

def show_options(event):
    selected_item = my_list.get(my_list.curselection())
    if selected_item in list:
        context_menu1.delete(0, END)  # Clear previous options
        context_menu1.add_command(label="Insert", command= lambda : insert_data(value_entry.get()))
        context_menu1.add_command(label="Update", command=lambda : update_data(value_entry.get()))
        context_menu1.add_command(label="Remove", command=remove_data)
        context_menu1.post(event.x_root, event.y_root)
    else:
        context_menu1.delete(0, END)  # Clear previous options
        context_menu1.add_command(label="Insert", command=lambda: insert_data(value_entry.get()))
        context_menu1.add_command(label="Update", command=lambda :update_data(value_entry.get()))
        context_menu1.add_command(label="Remove", command=remove_data)
        context_menu1.post(event.x_root, event.y_root)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)


def listpage():
    my_list.insert(0,list[0])
    list_page.tkraise()

root = Tk()
root.geometry("1500x700")
list = ["Click here"]

#create page start
start_page = Frame(root, width="1600", height="800",bg="#9EF2FF")
start_page.grid(column=0, row=0)
list_page = Frame(root, width="1600", height="800",bg="#9EF2FF")
list_page.grid(column=0, row=0)
#create page end

#search
search_entry1 = Entry(list_page,bg="#D4D4D4",width=23,highlightthickness=5)
search_entry1.place(x=790, y=485)
search_button1 = Button(list_page, text="Search",bg="#4FF545",bd=0,padx=12,font="25", command= search_data)
search_button1.place(x=955,y=480)
#search

# Create the reset button
reset_button = Button(list_page, text="Reset", bg="#FF0000", bd=0, padx=12, font="25", command=reset_program)
reset_button.place(x=500, y=480)

my_frame=Frame(list_page,)
my_frame.place(x=500,y=150)
my_list=Listbox(my_frame,width=50,height=12,cursor="hand2",font="30")
my_list.pack()

#for x in list:
   # my_list.insert(END,x)


context_menu = Menu(root,tearoff=0)
context_menu1 = Menu(list_page,tearoff=0)
context_menu.add_command(label="New node",command=listpage)

label = Label(list_page,text="Enter value",font="15")
label.place(x=500,y=100)
value_entry = Entry(list_page,bg="#D4D4D4",width=23,highlightthickness=5)
value_entry.place(x=620,y=100)


my_list.bind("<<ListboxSelect>>", show_options)
my_list.pack()

start_page.tkraise()
root.bind("<Button-3>",show_context_menu)
root.mainloop()
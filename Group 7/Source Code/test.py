from tkinter import *
import tkinter.messagebox as messagebox


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        linked_list_listbox.delete(0, END)
        while current:
            linked_list_listbox.insert(END, current.data)
            current = current.next


def save_value():
    try:
        value = int(linked_list_entry.get())
        linked_list.append(value)
        linked_list_entry.delete(0, END)
        linked_list.display()
    except ValueError:
        messagebox.showerror("Error", "Invalid input")


def remove_value():
    try:
        value = int(linked_list_entry.get())
        linked_list.remove(value)
        linked_list_entry.delete(0, END)
        linked_list.display()
    except ValueError:
        messagebox.showerror("Error", "Invalid input")


def switch_program():
    if program_var.get() == "Array Program":
        linked_list_frame.pack_forget()
        array_frame.pack()
    elif program_var.get() == "Linked List Program":
        array_frame.pack_forget()
        linked_list_frame.pack()


root = Tk()
root.geometry("400x350")
root.title("Data Structure Programs")

# Program selection
program_var = StringVar()
program_var.set("Array Program")

program_selection = OptionMenu(root, program_var, "Array Program", "Linked List Program")
program_selection.pack(pady=10)

# Array program
array_frame = Frame(root)

array_label = Label(array_frame, text="Array Program", font=("Arial", 16, "bold"))
array_label.pack(pady=10)

# TODO: Add array program elements

# Linked List program
linked_list_frame = Frame(root)

linked_list = LinkedList()

linked_list_label = Label(linked_list_frame, text="Linked List Program", font=("Arial", 16, "bold"))
linked_list_label.pack(pady=10)

linked_list_entry = Entry(linked_list_frame, width=10)
linked_list_entry.pack(pady=5)

save_button = Button(linked_list_frame, text="Save Value", command=save_value)
save_button.pack(pady=5)

remove_button = Button(linked_list_frame, text="Remove Value", command=remove_value)
remove_button.pack(pady=5)

linked_list_listbox = Listbox(linked_list_frame, width=20, height=8)
linked_list_listbox.pack(side=LEFT)

scrollbar = Scrollbar(linked_list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

linked_list_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=linked_list_listbox.yview)

# Switch program button
switch_button = Button(root, text="Switch Program", command=switch_program)
switch_button.pack(pady=10)

# Initial display
linked_list_frame.pack()

root.mainloop()

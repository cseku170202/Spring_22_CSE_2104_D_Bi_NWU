import tkinter as tk
from tkinter import simpledialog, messagebox

# Node class for LinkedList
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def insert_after(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def insert_before(self, old_data, new_data):
        if self.head is None:
            return
        if self.head.data == old_data:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.data == old_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete(self, data):
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

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

    def linked_list_to_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

    def list_to_linked_list(self, arr):
        self.head = None
        for data in arr:
            self.insert(data)

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x600")
        self.show_main_menu()

    def show_main_menu(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Button(self.master, text="Array", command=self.open_array_window, height=2, width=20).pack(pady=30)
        tk.Button(self.master, text="Linked List", command=self.open_ll_window, height=2, width=20).pack(pady=30)

    def open_array_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.geometry("600x600")
        OperationWindow(new_window, [], 'array', self.show_main_menu)

    def open_ll_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.geometry("600x600")
        OperationWindow(new_window, LinkedList(), 'linked_list', self.show_main_menu)

class OperationWindow:
    def __init__(self, master, container, container_type='array', return_to_main_menu=None):
        self.master = master
        self.container = container
        self.container_type = container_type
        self.return_to_main_menu = return_to_main_menu
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        tk.Button(self.master, text="Insert", command=self.insert_element).pack(side=tk.LEFT)
        tk.Button(self.master, text="Sort Ascending", command=self.sort_asc).pack(side=tk.LEFT)
        tk.Button(self.master, text="Sort Descending", command=self.sort_desc).pack(side=tk.LEFT)
        tk.Button(self.master, text="Reset", command=self.reset_elements).pack(side=tk.LEFT)
        self.update_buttons()

    def insert_element(self):
        num = simpledialog.askinteger("Insert", "Enter number")
        if self.container_type == 'array':
            self.container.append(num)
        elif self.container_type == 'linked_list':
            self.container.insert(num)
        self.update_buttons()

    def sort_asc(self):
        if self.container_type == 'array':
            self.container.sort()
        elif self.container_type == 'linked_list':
            list_representation = self.container.linked_list_to_list()
            list_representation.sort()
            self.container.list_to_linked_list(list_representation)
        self.update_buttons()

    def sort_desc(self):
        if self.container_type == 'array':
            self.container.sort(reverse=True)
        elif self.container_type == 'linked_list':
            list_representation = self.container.linked_list_to_list()
            list_representation.sort(reverse=True)
            self.container.list_to_linked_list(list_representation)
        self.update_buttons()

    def reset_elements(self):
        if self.container_type == 'array':
            self.container.clear()
        elif self.container_type == 'linked_list':
            self.container.head = None
        if self.return_to_main_menu:
            self.return_to_main_menu()
        self.master.destroy()

    def update_buttons(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        if self.container_type == 'array':
            for num in self.container:
                tk.Button(self.frame, text=str(num), command=lambda num=num: self.open_item_window(num)).pack(side=tk.LEFT)
        elif self.container_type == 'linked_list':
            current = self.container.head
            while current:
                tk.Button(self.frame, text=str(current.data), command=lambda num=current.data: self.open_item_window(num)).pack(side=tk.LEFT)
                current = current.next

    def open_item_window(self, num):
        new_window = tk.Toplevel(self.master)
        tk.Label(new_window, text=str(num)).pack()
        tk.Button(new_window, text="Delete", command=lambda: self.delete_and_close(num, new_window)).pack()
        tk.Button(new_window, text="Replace", command=lambda: self.replace_and_close(num, new_window)).pack()
        tk.Button(new_window, text="Insert After", command=lambda: self.insert_after_and_close(num, new_window)).pack()
        tk.Button(new_window, text="Insert Before", command=lambda: self.insert_before_and_close(num, new_window)).pack()

    def delete_and_close(self, num, window):
        if self.container_type == 'array':
            self.container.remove(num)
        elif self.container_type == 'linked_list':
            self.container.delete(num)
        window.destroy()
        self.update_buttons()

    def replace_and_close(self, num, window):
        new_num = simpledialog.askinteger("Replace", "Enter new number")
        if self.container_type == 'array':
            index = self.container.index(num)
            self.container[index] = new_num
        elif self.container_type == 'linked_list':
            self.container.replace(num, new_num)
        window.destroy()
        self.update_buttons()

    def insert_after_and_close(self, num, window):
        new_num = simpledialog.askinteger("Insert After", "Enter new number")
        if self.container_type == 'array':
            index = self.container.index(num)
            self.container.insert(index+1, new_num)
        elif self.container_type == 'linked_list':
            self.container.insert_after(num, new_num)
        window.destroy()
        self.update_buttons()

    def insert_before_and_close(self, num, window):
        new_num = simpledialog.askinteger("Insert Before", "Enter new number")
        if self.container_type == 'array':
            index = self.container.index(num)
            self.container.insert(index, new_num)
        elif self.container_type == 'linked_list':
            self.container.insert_before(num, new_num)
        window.destroy()
        self.update_buttons()

root = tk.Tk()
MainApplication(root)
root.mainloop()

from tkinter import *
import tkinter as tk


class Jabunnesa:
    def __init__(self, eva):
        self.eva = eva
        self.current_interface = 0
        self.array_size = 0
        self.array = []
        self.home_interface()


    def home_interface(self):
        self.current_interface = 0
        self.eva.title("Basic Data Structures")
        Label(self.eva, text="\u2744 Choose a Data Structure \u2744", relief="groove", font=("Times New Roman", 40, "bold"), bg="#AACCCC").pack(pady=30)

        Button(self.eva, text="Array", bg="skyblue", fg="black", relief="ridge", font=("Times New Roman", 15, "bold"), bd=5,
                  activeforeground="white", activebackground="green", command=self.array_interface).place(x=725, y=200)

        Button(self.eva, text="Linked List", font=("Times New Roman", 15, "bold"), bg="skyblue", fg="black", relief="ridge", bd=5,
                  activeforeground="white", activebackground="green", command=self.llnew).place(x=700, y=250)

        Button(self.eva, text="EXIT", bg="red", fg="black",font=("Times New Roman", 15, "bold"), relief=RIDGE,
                           bd=5, state=NORMAL,activeforeground="white", activebackground="grey",
                  command=self.eva.destroy).place(x=725, y=400)

    def array_interface(self):
        self.ary = tk.Toplevel(bg="#AACCCC")
        self.ary.title("Array")
        self.ary.geometry("1520x792+0+0")
        tk.Label(self.ary, text="Enter the size of array:", font="Sans-serif, 20 bold", bg="#AACCCC").place(x=400, y=40)
        self.array_size_entry = tk.Entry(self.ary, width="3", font="Arial 25")
        self.array_size_entry.place(x=490, y=83)
        self.array_size_entry.focus()
        Button(self.ary, text="Enter", font="Sans-serif, 15", bg="green", fg="white", relief="ridge", bd=5,
                  activeforeground="white", activebackground="grey", command=self.new).place(x=550, y=80)




    def new(self):

        tk.Label(self.ary, text="Enter array elements: ", font="Sans-serif, 20 bold", bg="#AACCCC").place(x=800, y=40)
        self.array_elements = tk.Entry(self.ary, width="15", font="Arial 25")
        self.array_elements.place(x=805, y=83)
        self.array_elements.focus()
        tk.Button(self.ary, text="Create", font="Sans-serif, 15", bg="#65D560", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.show_array).place(x=910, y=130)

        tk.Button(self.ary, text="\u21E6", width=3, font="Sans-serif, 18", bg="#412AB4", fg="white", bd=5,
                  relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.ary.destroy).place(x=200, y=400)

        tk.Button(self.ary, text="\u21E8", width=3, font="Sans-serif, 18", bg="#65D560", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.show_array).place(x=1280, y=400)




    def show_array(self):
        self.out = tk.Toplevel(bg="#AACCCC")
        self.out.title("Arrays: Operations")
        self.out.geometry("1520x792+0+0")

        global array
        array = Label(self.out, text="", font=("Times New Roman", 40, "bold"), bg="#AACCCC")
        array.pack()


        self.size = int(self.array_size_entry.get())

        array_str = self.array_elements.get()
        self.array = [int(num) for num in array_str.split()[:self.size]]


        array.config(text="Array: " + str(self.array))

        self.refreshbtn = Button(self.out, text="\u27F3Refresh", font="Sans-serif, 15", bg="#0CEC94", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.refresh).place(x=720, y=80)


        tk.Button(self.out, text="Search", font="Sans-serif, 15", bg="black", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.array_search).place(x=580, y=190)
        tk.Button(self.out, text="Insert", font="Sans-serif, 15", bg="black", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.array_insert).place(x=690, y=190)
        tk.Button(self.out, text="Delete", font="Sans-serif, 15", bg="black", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.array_delete).place(x=790, y=190)
        tk.Button(self.out, text="Update", font="Sans-serif, 15", bg="black", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.update).place(x=890, y=190)

        tk.Button(self.out, text="EXIT", bg="red", fg="black",font=("Times New Roman", 15, "bold"), relief=RIDGE,
                           bd=5, state=NORMAL, activeforeground="white",
                  activebackground="grey", command=self.eva.destroy).place(x=740, y=300)

        tk.Button(self.out, text="\u21E8", width=3, font="Sans-serif, 18", bg="#75DF62", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.array_search).place(x=1300, y=600)
        tk.Button(self.out, text="\u21E6", width=3, font="Sans-serif, 18", bg="purple", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.out.destroy).place(x=150, y=600)





    def array_search(self):

        self.src = tk.Toplevel(bg="#AACCCC")
        self.src.title("Search Operation")
        self.src.geometry("1520x792+0+0")

        tk.Label(self.src, text="\u2666 Search Operation \u2666", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#AACCCC").pack(pady=30)

        tk.Label(self.src, text="Enter the element you want to search: " + str(self.array), font="Sans-serif, 20 bold",
                 bg="#AACCCC").pack(pady=10)
        self.array_search_element = tk.Entry(self.src, width="3", font="Arial 25")
        self.array_search_element.pack(pady=5)
        self.array_search_element.focus()
        tk.Button(self.src, text="Search", font="Sans-serif, 15", bg="#F0E16D", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.V_search_result).pack(pady=5)

        tk.Button(self.src, text="\u21E8", font="Sans-serif, 15", bg="#75DF62", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.array_insert).place(x=1300, y=600)
        tk.Button(self.src, text="\u21E6", font="Sans-serif, 15", bg="purple", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.src.destroy).place(x=150, y=600)



    def V_search_result(self):

        global lblSearch
        global SearchElement
        global pos
        SearchElement = int(self.array_search_element.get())

        if SearchElement in self.array:
            pos = self.array.index(SearchElement)

            lblSearch = Label(self.src, text=str(SearchElement) + " Found at Position " + str(pos), font="Sans-serif, 20 bold", bg="#AACCCC")
            lblSearch.pack(pady=10)

        else:

            lblSearch.config(text=str(SearchElement) + " Not Found in the Array")
            lblSearch.pack(pady=10)

    def array_insert(self):
        self.insrt = tk.Toplevel(bg="#AACCCC")
        self.insrt.title("Insert Operation: By Value")
        self.insrt.geometry("1520x792+0+0")

        Label(self.insrt, text="\u2666 Insert Operation \u2666", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#AACCCC").pack(pady=30)


        self.value= tk.Button(self.insrt, text="Insert By Value", font="Sans-serif, 15", bg="#EB96EB", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.insert_with_value).place(x=100, y=150)

        self.index= tk.Button(self.insrt, text="Insert By Index No.", font="Sans-serif, 15", bg="#EB96EB", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.insert_with_index).place(x=100, y=200)

        tk.Button(self.insrt, text="\u21E8", font="Sans-serif, 15", bg="#75DF62", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.array_delete).place(x=1300,
                                                                                                      y=600)
        tk.Button(self.insrt, text="\u21E6", font="Sans-serif, 15", bg="purple", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.insrt.destroy).place(x=150, y=600)






    def insert_with_value(self):

        tk.Label(self.insrt, text="Enter the element you want to insert: " + str(self.array),font="Sans-serif, 20 bold",
                 bg="#AACCCC").pack(pady=10)

        self.array_insert_entry = tk.Entry(self.insrt, width="3", font="Arial 25")
        self.array_insert_entry.pack(pady=5)
        self.array_insert_entry.focus()

        tk.Button(self.insrt, text="Insert", font="Sans-serif, 15", bg="#F0E16D", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.insert_with_value2).pack(pady=10)




    def insert_with_value2(self):

        self.array.append(int(self.array_insert_entry.get()))
        tk.Label(self.insrt,
                 text="\nAfter inserting " + self.array_insert_entry.get() + "\n\n Updated array: " + str(self.array),
                 font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=20)



    def insert_with_index(self):
        self.insrt_indx = tk.Toplevel(bg="#AACCCC")
        self.insrt_indx.title("Insert Operation: By Index")
        self.insrt_indx.geometry("1520x792+0+0")

        tk.Label(self.insrt_indx, text="Array: " + str(self.array), font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)

        tk.Label(self.insrt_indx, text="Enter the Index No.", font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)
        self.index_entry = tk.Entry(self.insrt_indx, width="3", font="Arial 25")
        self.index_entry.pack(pady=5)
        self.index_entry.focus()

        tk.Label(self.insrt_indx, text="Enter the Value", font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)
        self.index_value = tk.Entry(self.insrt_indx, width="3", font="Arial 25")
        self.index_value.pack(pady=5)

        tk.Button(self.insrt_indx, text="Enter", font="Sans-serif, 15", bg="#412AB4", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.insert_with_index2).pack()

        tk.Button(self.insrt_indx, text="\u21E8", font="Sans-serif, 15", bg="#75DF62", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.array_delete).place(x=1300,
                                                                                                      y=600)
        tk.Button(self.insrt_indx, text="\u21E6", font="Sans-serif, 15", bg="purple", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.insrt_indx.destroy).place(x=150, y=600)





    def insert_with_index2(self):
        self.array.insert(int(self.index_entry.get()), int(self.index_value.get()))

        tk.Label(self.insrt_indx, text="\nAfter inserting " + str(self.index_value.get()) + " at Position: "
                                       + str(self.index_entry.get()) + " \n\nUpdated array: "
                                       + str(self.array), font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)





    def array_delete(self):
        self.dlt = tk.Toplevel(bg="#AACCCC")
        self.dlt.title("Delete Operation")
        self.dlt.geometry("1520x792+0+0")

        Label(self.dlt, text="\u2666 Delete Operation \u2666", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#AACCCC").pack(pady=30)

        Button(self.dlt, text="Delete by Value", font="Sans-serif, 15", bg="#EB96EB", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.delete_by_value).place(x=100, y=150)

        Button(self.dlt, text="Delete by Index No.", font="Sans-serif, 15", bg="#EB96EB", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.delete_by_index).place(x=100, y=200)




        Button(self.dlt, text="\u21E8", font="Sans-serif, 15", bg="#75DF62", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.update).place(x=1300, y=600)
        Button(self.dlt, text="\u21E6", font="Sans-serif, 15", bg="purple", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.dlt.destroy).place(x=150, y=600)

    def delete_by_value(self):

        tk.Label(self.dlt, text="Enter the value you want to delete from the Array: " + str(self.array), font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)
        self.delete_value = tk.Entry(self.dlt, width="3", font="Arial 25")
        self.delete_value.pack(pady=5)
        self.delete_value.focus()

        tk.Button(self.dlt, text="Delete", font="Sans-serif, 15", bg="#F0E16D", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.delete_interface0).pack(pady=5)



    def delete_interface0(self):
        global array_label
        global value
        global dlt_value
        dlt_value = None

        value = int(self.delete_value.get())
        try:
            if value in self.array:
                self.array.remove(value)
                array_label = Label(self.dlt, text="After deleting: " + str(value)+ "\n Updated array: " +
                                                            str(self.array), font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)
                # tk.Button(self.dlt, text="Go to Array Home", font="Sans-serif, 15", bg="Lightsteelblue2",
                #           fg="black", bd=5, relief="raised", activeforeground="white", activebackground="grey", command=self.out.destroy).pack()
            else:
                Label(self.dlt, text="Value not found.", font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)
        except ValueError:
            Label(self.dlt, text="Invalid Value.", font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)





    def delete_by_index(self):

        self.dlt_by_index = tk.Toplevel(bg="#AACCCC")
        self.dlt_by_index.title("Delete Operation: By Index")
        self.dlt_by_index.geometry("1520x792+0+0")

        tk.Label(self.dlt_by_index, text="Enter the index number you want to delete from the\nArray: " + str(self.array),
                 font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=10)
        self.array_delete_entry = tk.Entry(self.dlt_by_index, width="3", font="Arial 25")
        self.array_delete_entry.pack(pady=5)
        self.array_delete_entry.focus()

        Button(self.dlt_by_index, text="Delete", font="Sans-serif, 15", bg="#F0E16D", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.delete_interface).pack()

        Button(self.dlt_by_index, text="\u21E8", font="Sans-serif, 15", bg="#75DF62", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.update).place(x=1300, y=600)
        Button(self.dlt_by_index, text="\u21E6", font="Sans-serif, 15", bg="purple", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.dlt_by_index.destroy).place(x=150, y=600)




    def delete_interface(self):
        self.x = int(self.array_delete_entry.get())
        self.array.__delitem__(self.x)
        tk.Label(self.dlt_by_index,
                 text="\nAfter deleting index No: " + self.array_delete_entry.get() +
                      "\n\n Updated array: " + str(self.array), font="Sans-serif, 20 bold", bg="#AACCCC").pack(pady=20)



    def update(self):

        global old_value
        global new_value
        self.up = Toplevel(bg="#AACCCC")
        self.up.title("Update Operation")
        self.up.geometry("1520x792+0+0")

        Label(self.up, text="\u2666 Update Operation \u2666", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#AACCCC").pack(pady=30)

        tk.Label(self.up, text="Array: " + str(self.array), font="Sans-serif, 30 bold", bg="#AACCCC").pack(pady=10)

        self.old_value_label = Label(self.up, text="Enter Existing Value:", font="Sans-serif, 20 bold", bg="#AACCCC")
        self.old_value_label.pack(pady=5)
        self.old_value_entry = Entry(self.up, width="3", font="Arial 20")
        self.old_value_entry.place(x=900, y=200)
        self.old_value_entry.focus()

        self.new_value_label = Label(self.up, text="Enter New Value:", font="Sans-serif, 20 bold", bg="#AACCCC")
        self.new_value_label.pack()
        self.new_value_entry = Entry(self.up, width="3", font="Arial 20")
        self.new_value_entry.place(x=900, y=245)

        Button(self.up, text="Update", font="Sans-serif, 15", bg="#F0E16D", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.update_fn).pack(pady=5)


        tk.Button(self.up, text="\u21E8", font="Sans-serif, 15", bg="red", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.llnew).place(x=1300, y=600)
        tk.Button(self.up, text="\u21E6", font="Sans-serif, 15", bg="purple", fg="white", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.up.destroy).place(x=150, y=600)





    def update_fn(self):

        self.uplbl = Label(self.up, text="", font="Sans-serif, 20 bold", bg="#AACCCC")
        self.uplbl.pack(pady=10)

        old_value = int(self.old_value_entry.get())
        new_value = int(self.new_value_entry.get())

        if old_value in self.array:
            index = self.array.index(old_value)
            self.array[index] = new_value

            self.uplbl.config(text="After Updating " + self.old_value_entry.get() + " by " + self.new_value_entry.get()+
                                   "\nUpdated array: " + str(self.array))
        else:
            self.uplbl.config(text=str(self.old_value_entry.get()) + " not found in the array")



    def refresh(self):
        array.config(text="Array: " + str(self.array))





########################################################################################################################
#                                                                                                                      #
#                                (E V A)      L I N K E D     L I S T                                                  #
#                                                                                                                      #
########################################################################################################################

    def llnew (self):
        LinkedListGUI()




class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, prev, data, insert_after=True):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        elif not prev:
            new_node.next = self.head
            self.head = new_node
        else:
            if insert_after:
                new_node.next = prev.next
                prev.next = new_node
            else:
                new_node.next = prev
                if prev == self.head:
                    self.head = new_node
                else:
                    current = self.head
                    while current.next != prev:
                        current = current.next
                    current.next = new_node

    def delete(self, prev, current):
        if current == self.head:
            self.head = current.next
        elif prev:
            prev.next = current.next

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return ' -> '.join(values)

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1


class LinkedListGUI:
    def __init__(self):
        self.lwind = Toplevel(bg="#AACCCC")
        self.lwind.title("Linked List GUI")
        self.lwind.geometry("1520x792+0+0")

        self.lbl = Label(self.lwind, text=" Right Click to Create a Linked List ", font=("Times New Roman", 20, "bold"), bg="#AACCCC", relief=SUNKEN, bd=2)
        self.lbl.place(x=550, y=10)
        self.lwind.bind("<Button-3>", self.show_entry_frame)
        self.exit_button = Button(self.lwind, text="HOME", bg="dark green", fg="white", font="Sans-serif, 15",bd=5, relief="ridge",
                                activeforeground="white", activebackground="grey", command=self.lwind.destroy)
        self.exit_button.place(x=720, y=710)

        self.values = LinkedList()
        self.entry_frame = None
        self.operation_frame = None

        self.canvas = tk.Canvas(self.lwind, width=800, height=300)
        self.canvas.place(x=350, y=200)

        self.lwind.mainloop()

    def show_entry_frame(self, event):
        if self.entry_frame is not None:
            return

        self.entry_frame = tk.Frame(self.lwind, relief=tk.SOLID, borderwidth=2)
        self.entry_frame.place(x=760, y=120, anchor=tk.CENTER)

        self.entry_field = tk.Entry(self.entry_frame, width=20, font=("Times New Roman", 20))
        self.entry_field.pack(padx=5, pady=5)
        self.entry_field.focus()

        ok_button = tk.Button(self.entry_frame, text="OK", bg="skyblue", fg="black", font="Sans-serif, 15", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=self.process_entry)
        ok_button.pack(pady=5)



    def hide_entry_frame(self):
        if self.entry_frame is not None:
            self.entry_frame.destroy()
            self.entry_frame = None

    def process_entry(self):
        if self.entry_field is not None:
            data = self.entry_field.get()
            values = data.split()
            for value in reversed(values):  # Iterate in reverse order
                self.values.insert(None, value)  # Insert at the head
            self.entry_field.delete(0, tk.END)
            self.hide_entry_frame()
            self.display_list()

    def display_list(self):
        self.canvas.delete("all")

        node_radius = 30
        node_spacing = 100

        current = self.values.head
        x = node_spacing
        while current:
            self.canvas.create_oval(x - node_radius, 150 - node_radius,
                                    x + node_radius, 150 + node_radius,
                                    fill="lightblue")
            self.canvas.create_text(x, 150, text=str(current.data), font=("Sans-serif, 15"))

            x += node_spacing
            current = current.next

        current = self.values.head  # Start again from the head
        while current.next:
            self.canvas.create_text(x, 150, text="")
            x += node_spacing
            current = current.next

        self.canvas.bind("<Button-1>", self.show_operations)

    def show_operations(self, event):
        if self.entry_frame is not None:
            return

        self.operation_frame = tk.Frame(self.lwind, relief=tk.SOLID, borderwidth=2)
        self.operation_frame.place(x=760, y=550, anchor=tk.CENTER)

        selected_index = (event.x - 50) // 100
        current = self.values.head
        for _ in range(selected_index):
            if current:
                current = current.next

        if current:
            search_button = tk.Button(self.operation_frame, text="Search", bg="skyblue", fg="black", font="Sans-serif, 15", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=lambda: self.show_search_frame())
            search_button.pack(side=tk.LEFT, padx=5)

            insert_button = tk.Button(self.operation_frame, text="Insert", bg="skyblue", fg="black", font="Sans-serif, 15", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=lambda: self.show_insert_frame(current))
            insert_button.pack(side=tk.LEFT, padx=5)

            delete_button = tk.Button(self.operation_frame, text="Delete", bg="skyblue", fg="black", font="Sans-serif, 15", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=lambda: self.delete_value(current))
            delete_button.pack(side=tk.LEFT, padx=5)

            update_button = tk.Button(self.operation_frame, text="Update", bg="skyblue", fg="black", font="Sans-serif, 15", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=lambda: self.show_update_frame(current))
            update_button.pack(side=tk.LEFT, padx=5)




    def hide_opFrame(self):
        if self.operation_frame is not None:
            self.operation_frame.destroy()
            self.operation_frame = None


    def show_insert_frame(self, selected_node):
        if self.entry_frame is not None:
            self.entry_frame.destroy()
            self.entry_frame = None

        self.selected_node = selected_node

        self.entry_frame = tk.Frame(self.lwind, bg="#AACCCC", relief=tk.SOLID, borderwidth=2)
        self.entry_frame.place(x=760, y=650, anchor=tk.CENTER)

        self.insert_field = tk.Entry(self.entry_frame, width=10, font=("Times New Roman", 20))
        self.insert_field.pack(padx=5, pady=5)
        self.insert_field.focus()

        insert_before_button = tk.Button(self.entry_frame, text="Insert Before", bg="skyblue", fg="black", font="Sans-serif, 12", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey",
                                         command=lambda: self.insert_value(self.selected_node, False))
        insert_before_button.pack(side=tk.LEFT, padx=5)

        insert_after_button = tk.Button(self.entry_frame, text="Insert After", bg="skyblue", fg="black", font="Sans-serif, 12", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey",
                                        command=lambda: self.insert_value(self.selected_node, True))
        insert_after_button.pack(side=tk.LEFT, padx=5)

    def insert_value(self, selected_node, insert_after=True):
        if self.insert_field is not None:
            new_value = self.insert_field.get()
            self.values.insert(selected_node, new_value, insert_after)
            self.insert_field.delete(0, tk.END)
            self.hide_entry_frame()
            self.hide_opFrame()
            self.display_list()

    def delete_value(self, selected_node):
        prev = None
        current = self.values.head
        while current:
            if current == selected_node:
                self.values.delete(prev, current)
                self.hide_opFrame()
                self.display_list()
                return
            prev = current
            current = current.next


    def show_update_frame(self, selected_node):
        if self.entry_frame is not None:
            self.entry_frame.destroy()
            self.entry_frame = None

        self.selected_node = selected_node

        self.entry_frame = tk.Frame(self.lwind, bg="#AACCCC", relief=tk.SOLID, borderwidth=2)
        self.entry_frame.place(x=760, y=650, anchor=tk.CENTER)

        self.update_field = tk.Entry(self.entry_frame, width=10, font=("Times New Roman", 20))
        self.update_field.pack(padx=5, pady=5)
        self.update_field.focus()

        update_button = tk.Button(self.entry_frame, text="Update", font="Sans-serif, 12",  bg="skyblue", fg="black", bd=5, relief="ridge",
                  activeforeground="white", activebackground="grey", command=lambda: self.update_value(self.selected_node))
        update_button.pack(pady=5)

    def update_value(self, selected_node):
        if self.update_field is not None:
            new_value = self.update_field.get()
            selected_node.data = new_value
            self.update_field.delete(0, tk.END)
            self.hide_entry_frame()
            self.hide_opFrame()
            self.display_list()

    def show_search_frame(self):
        if self.operation_frame is not None:
            self.operation_frame.destroy()
            self.operation_frame = None
        self.window = Toplevel()

        self.window.title("Search Operations")
        self.window.config(bg="#AACCCC")
        self.window.geometry("365x273+1155+230")

        self.slbl = Label(self.window, text="Enter a value to Search in the List", bg="#AACCCC",
                          font=("Times New Roman", 18))
        self.slbl.pack(pady=10)

        self.result_label = Label(self.window, text="", bg="#AACCCC", font=("Times New Roman", 20, "bold"))
        self.result_label.place(x=90, y=180)

        self.sentry_frame = tk.Frame(self.window, relief=tk.SOLID, borderwidth=2)
        self.sentry_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.search_field = tk.Entry(self.window, width=10, font=("Times New Roman", 20))
        self.search_field.pack(padx=5, pady=5)
        self.search_field.focus()

        search_button = tk.Button(self.window, text="Search", bg="green", fg="white", font="Sans-serif, 10", bd=5,
                                  relief="ridge",
                                  activeforeground="white", activebackground="grey",
                                  command=lambda: self.search_value())
        search_button.pack(pady=5)

    def search_value(self):
        if self.search_field is not None:
            search_value = self.search_field.get()
            index = self.values.search(search_value)
            if index != -1:
                self.result_label.config(text=f"Found at index {index}")
            else:
                self.result_label.config(text="Not found in the List")
            self.search_field.delete(0, tk.END)


root = tk.Tk()
root.geometry("1520x792+0+0")
root.config(bg="#AACCCC")
app = Jabunnesa(root)
root.mainloop()

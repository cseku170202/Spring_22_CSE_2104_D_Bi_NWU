import tkinter as tk
from tkinter import simpledialog,messagebox

array = []

def create_array():
    global array
    values = simpledialog.askstring("Create Array", "Enter values separated by comma")
    if values is not None:
        values_list = values.split(",")
        try:
            array = [int(value.strip()) for value in values_list if value.strip()]
            label.config(text="Array: " + str(array))
        except ValueError:
            messagebox.showerror("Error", "Enter integers only!")


def insert_array():

    try:
        value = simpledialog.askinteger("Insert", "Enter a value:")
        if value is not None:
            array.append(value)
            label.config(text="Array: " + str(array))
    except ValueError:
        messagebox.showerror("Error", "Enter an integer value!")


def delete_array():

    try:
        index = simpledialog.askinteger("Delete", "Enter an index:")
        if index is not None and index >= 0 and index < len(array):
            del array[index]
            label.config(text="Array: " + str(array))
        else:
            messagebox.showerror("Error", "Invalid index!")
    except ValueError:
        messagebox.showerror("Error", "Enter an integer index!")


def open_array():
    global label

    array_window = tk.Toplevel()
    array_window.geometry("700x500")
    array_window.title("Array Operation")

    frame = tk.Frame(array_window)
    frame.pack()
    label = tk.Label(frame, text="Array: ", font=("Arial", 24))
    label.pack(pady=20)
    create_button = tk.Button(frame, text="Create",padx=20,pady=10,command=create_array, bg="black", fg="white",
                              font=("Arial", 14))
    create_button.pack(side=tk.LEFT, padx=30,pady=60)
    insert_button = tk.Button(frame, text="Insert", padx=20,pady=10,command=insert_array, bg="green", fg="black",
                              font=("Arial", 14))
    insert_button.pack(side=tk.LEFT, padx=30)
    delete_button = tk.Button(frame, text="Delete", padx=20,pady=10,command=delete_array, bg="red", fg="black",
                              font=("Arial", 14))
    delete_button.pack(side=tk.LEFT, padx=30)




def destroy_linked_list_window():
    linked_list_window.destroy()

def open_linked_list():
    global value_entry,linked_list_window
    linked_list_window = tk.Toplevel()
    linked_list_window.geometry("600x500")
    linked_list_window.title("Linked List")
    linked_list_window.columnconfigure([0, 1], weight=1, minsize=250)
    linked_list_window.rowconfigure([0, 1,2], weight=1, minsize=100)
    linked_list_window.bind("<Button-1>", create_linked_list)




def create_linked_list(event):
    global linked_list
    values = simpledialog.askstring("Create", "Enter values separated by comma :")
    if values is None:
        return
    values = values.split(",")
    linked_list = [int(value.strip()) for value in values]
    display_linked_list()



def display_linked_list():
    destroy_linked_list_window()
    list_window = tk.Toplevel()
    list_window.title("Linked List Display Screen")
    canvas = tk.Canvas(list_window, width=800, height=500)
    canvas.pack()

    node_positions = []
    arrow_coords = []
    x = 100
    y = 100
    node_width = 80
    node_height = 50
    arrow_length = 50

    for value in linked_list:
        canvas.create_rectangle(x, y, x + node_width, y + node_height, fill="lightblue")
        canvas.create_text(x + node_width // 2, y + node_height // 2, text=str(value))
        node_positions.append((x + node_width // 2, y + node_height))
        x += node_width + arrow_length
        arrow_coords.append((x - arrow_length, y + node_height // 2))

    arrows = []
    for i in range(len(linked_list) - 1):
        x1, y1 = arrow_coords[i]
        x2, y2 = node_positions[i + 1]
        arrow = canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
        arrows.append(arrow)

    canvas.bind("<Button-1>", lambda event: perform_linked_list_operation(event, canvas, node_positions, arrows))


def perform_linked_list_operation(event, canvas, node_positions, arrows):
    global linked_list

    clicked_node = None
    for i, position in enumerate(node_positions):
        x, y = position
        if x - 40 <= event.x <= x + 40 and y - 25 <= event.y <= y + 25:
            clicked_node = i
            break

    if clicked_node is not None:
        choice = simpledialog.askstring("Linked List Operation",
        "Select an operation:\n1. Insert at the end\n2. Insert at the beginning\n3. Update\n4. Insert at index\n5. Delete the first node\n6. Delete the last node\n7. Delete this node\n8. Delete at index"
        )
        if choice is None:
            return

        if choice == "1":  # Insert at the end
            value = simpledialog.askinteger("Insert at the End", "Enter the value:")
            if value is None:
                return
            linked_list.append(value)
        elif choice == "2":  # Insert at the beginning
            value = simpledialog.askinteger("Insert at the Beginning", "Enter the value:")
            if value is None:
                return
            linked_list.insert(0, value)
        elif choice == "3":  # Update
            new_value = simpledialog.askinteger("Update", "Enter the new value:")
            if new_value is None:
                return
            linked_list[clicked_node] = new_value
        elif choice == "4":  # Insert at index
            index = simpledialog.askinteger("Insert at Index", "Enter the index:")
            if index is None or index < 0 or index > len(linked_list):
                messagebox.showerror("Error", "Invalid index!")
                return
            value = simpledialog.askinteger("Insert at Index", "Enter the value:")
            if value is None:
                return
            linked_list.insert(index, value)
        elif choice == "5":  # Delete the first node
            if len(linked_list) > 0:
                linked_list.pop(0)
        elif choice == "6":  # Delete the last node
            if len(linked_list) > 0:
                linked_list.pop()
        elif choice == "7":  # Delete this node
            linked_list.pop(clicked_node)
        elif choice == "8":  # Delete at index
            index = simpledialog.askinteger("Delete at Index", "Enter the index:")
            if index is None or index < 0 or index >= len(linked_list):
                messagebox.showerror("Error", "Invalid index!")
                return
            linked_list.pop(index)

        canvas.delete("all")
        node_positions = []
        arrow_coords = []
        x = 100
        y = 100
        node_width = 80
        node_height = 50
        arrow_length = 50

        for value in linked_list:
            canvas.create_rectangle(x, y, x + node_width, y + node_height, fill="lightblue")
            canvas.create_text(x + node_width // 2, y + node_height // 2, text=str(value))
            node_positions.append((x + node_width // 2, y + node_height))
            x += node_width + arrow_length
            arrow_coords.append((x - arrow_length, y + node_height // 2))

        arrows = []
        for i in range(len(linked_list) - 1):
            x1, y1 = arrow_coords[i]
            x2, y2 = node_positions[i + 1]
            arrow = canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
            arrows.append(arrow)


root = tk.Tk()
root.geometry("800x600")
root.title("Project")
root.config(background="#81849f")
root.columnconfigure([0,1,2], weight=1, minsize=250)
root.rowconfigure([0,1,2,3], weight=1, minsize=100)

array_button = tk.Button(root, text="Array", padx=50, pady=25, fg="white", bg="black", font="Times 20 bold" ,
                         command=open_array)
array_button.grid(row=1,column=1,pady=10)
linkedlist_button = tk.Button(root, text="LinkedList", padx=50, pady=25,fg="white", bg="black", font="Times 20 bold",
                              command=open_linked_list)
linkedlist_button.grid(row=2, column=1,pady=30)

root.mainloop()


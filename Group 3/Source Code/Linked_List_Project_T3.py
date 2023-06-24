import tkinter as tk
import tkinter.messagebox as messagebox
import os
from tkinter import simpledialog


def exit1():
    exit()


def about():
    messagebox.showinfo("Members", "Made with <3 by Asif Iqbal, Fariha Akter Prova & Tanmay Ghosh.")


def about1():
    messagebox.showinfo("About",
                        "A Linked List based Python Tkinter Project with functionalities like Create, Update, Add, Remove & Export Data.")


def on_right_click(event):
    new_menu.tk_popup(event.x_root, event.y_root)


def on_new():
    # Create a new window for input
    input_window = tk.Toplevel(root)
    input_window.geometry("300x100+500+300")

    # Create a Label widget for user input text
    label = tk.Label(input_window, text="Enter your Data:")
    label.grid(row=0, column=8, sticky='w')

    # Create an Entry widget for user input
    entry = tk.Entry(input_window)
    entry.grid(row=0, column=10, padx=5, pady=5)

    def on_ok():
        # Get the input from the Entry widget
        input_string = entry.get()

        # Create a clickable label for the input data
        clickable_label = tk.Label(output_frame, text=input_string,relief="solid",padx="25",font=("Baskerville Old Face","15"),bg="#D6EAF8", fg="black", cursor="hand2")
        clickable_label.grid(row=len(data_labels), column=10, padx=0,pady=0)

        clickable_label.bind("<Button-1>", lambda event, label=clickable_label: on_label_click(event, label))

        def on_label_click(event, label):
            # Create a menu when the label is clicked
            label_menu = tk.Menu(root, tearoff=0,bg="#D6EAF8")
            label_menu.add_command(label="Add Left", command=lambda: add_node("left", label.cget("text")))
            label_menu.add_command(label="Add Right", command=lambda: add_node("right", label.cget("text")))
            label_menu.add_command(label="Update", command=lambda: edit_node(label))
            label_menu.add_command(label="Remove", command=lambda: remove_node(label))

            # Display the menu at the clicked location
            label_menu.tk_popup(event.x_root, event.y_root)

        clickable_label.bind("<Button-1>", lambda event, l=clickable_label: on_label_click(event, l))

        # Add the label to the list of data labels
        data_labels.append(clickable_label)

        # Close the input window
        input_window.destroy()

    # Create a button to submit the input
    ok_button = tk.Button(input_window, text="Enter", command=on_ok)
    ok_button.grid(row=2, column=10, padx=5, pady=5)


def add_node(position, label):
    new_data = simpledialog.askstring("Add Value to Node", "Enter the new data:")
    if new_data:
        new_label = tk.Label(output_frame, text=new_data,relief="solid",padx="25",font=("Baskerville Old Face","15"),bg="#D6EAF8", fg="black", cursor="hand2")
        new_label.grid(row=0, column=10, padx=0,pady=0)

        if position == "left":
            try:
                index = data_labels.index(label)
            except ValueError:
                index = 0

            data_labels.insert(index, new_label)

            for i, lbl in enumerate(data_labels):
                lbl.grid(row=0, column=i,padx=10, pady=0)

        elif position == "right":
            try:
                index = data_labels.index(label) + 1
            except ValueError:
                index = len(data_labels)

            data_labels.insert(index, new_label)

            for i, lbl in enumerate(data_labels):
                lbl.grid(row=0, column=i, padx=10, pady=10)

        new_label.bind("<Button-1>", lambda event, lbl=new_label: on_label_click(event, lbl))


def on_label_click(event, data):
    # Create a menu when the label is clicked
    label_menu = tk.Menu(root, tearoff=0,bg="#D6EAF8")
    label_menu.add_command(label="Add Left", command=lambda: add_node("left", data))
    label_menu.add_command(label="Add Right", command=lambda: add_node("right", data))
    label_menu.add_command(label="Update", command=lambda: edit_node(data))
    label_menu.add_command(label="Remove", command=lambda: remove_node(data))

    # Display the menu at the clicked location
    label_menu.tk_popup(event.x_root, event.y_root)


def edit_node(label):
    # Create a new window for editing
    edit_window = tk.Toplevel(root)
    edit_window.geometry("300x100+500+300")

    # Create a Label widget for edit text
    edit_label = tk.Label(edit_window, text="Update your Data:")
    edit_label.grid(row=0, column=8, sticky='w')

    # Create an Entry widget with the current data
    entry = tk.Entry(edit_window)
    entry.insert(0, label.cget("text"))
    entry.grid(row=0, column=10, padx=5, pady=5)

    def on_update():
        # Get the updated data from the Entry widget
        updated_data = entry.get()

        # Update the label text with the updated data
        label.config(text=updated_data)

        # Close the edit window
        edit_window.destroy()

    # Create a button to update the data
    update_button = tk.Button(edit_window, text="Update", command=on_update)
    update_button.grid(row=2, column=10, padx=5, pady=5)


def remove_node(label):
    # Remove the label from the list and destroy the label widget
    data_labels.remove(label)
    label.destroy()


def clear_output():
    for label in data_labels:
        label.destroy()

    data_labels.clear()


def export_data():
    data = '\n'.join(label.cget("text") for label in data_labels)
    file_path = os.path.join(os.getcwd(), "output_linked_list.txt")  # Create a file path in the program's location
    try:
        with open(file_path, "w") as file:
            file.write(data)
        messagebox.showinfo("Export", "Data exported successfully.")
    except Exception as e:
        messagebox.showerror("Export Error", str(e))


def search_data():
    search_query = simpledialog.askstring("Search Data", "Enter the data to search:")
    found = False
    for label in data_labels:
        if label.cget("text") == search_query:
            found = True
            break
    if found:
        messagebox.showinfo("Search Result", f"YES, Data '{search_query}' is found!")
    else:
        messagebox.showinfo("Search Result", f"NO, Data '{search_query}' is NOT found!")


root = tk.Tk()
root.geometry("700x400+300+100")
root.title("Linked List Operations")

# Create a frame for the output labels
output_frame = tk.Frame(root)
output_frame.pack(pady=20)

# Create a list to store the data labels
data_labels = []

# Create a right-click menu
new_menu = tk.Menu(root, tearoff=0,bg="#D6EAF8")
new_menu.add_command(label="New", command=on_new)
new_menu.add_command(label="Search", command=search_data)
new_menu.add_command(label="Export", command=export_data)
new_menu.add_command(label="Reset", command=clear_output)
new_menu.add_separator()
new_menu.add_command(label="About", command=about1)
new_menu.add_command(label="Authors", command=about)
new_menu.add_command(label="Exit", command=exit1)

root.config(menu=new_menu)

root.bind("<Button-3>", on_right_click)

root.mainloop()
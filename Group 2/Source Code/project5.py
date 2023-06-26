import tkinter as tk
from tkinter import messagebox, simpledialog

# List to store the data
data_list = []

def open_data_page():
    # Hide the initial page
    initial_page.pack_forget()

    # Show the linked list operation
    data_page.pack()

def insert_data():
    # Open a dialog box to get input from the user
    data = simpledialog.askstring("Insert Data", "Enter the data:")
    if data:
        data_list.append(data)
        show_data()

def update_data():
    selected_index = data_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]  # Extract the index from the tuple
        selected_data = data_listbox.get(selected_index)
        updated_data = simpledialog.askstring("Update Data", "Enter the updated data:", initialvalue=selected_data)
        if updated_data:
            data_list[selected_index] = updated_data
            messagebox.showinfo("Success", "Data updated successfully.")
            show_data()

def remove_data():
    selected_index = data_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]  # Extract the index from the tuple
        data_list.pop(selected_index)
        messagebox.showinfo("Success", "Data removed successfully.")
        show_data()

def search_data():
    search_query = simpledialog.askstring("Search Data", "Enter the data to search:")
    if search_query:
        results = [data for data in data_list if search_query in data]
        if results:
            messagebox.showinfo("Search Results", f"Found {len(results)} result(s):\n\n{', '.join(results)}")
        else:
            messagebox.showinfo("Search Results", "No results found.")

def show_data():
    # Clear the listbox
    data_listbox.delete(0, tk.END)

    # Insert the data into the listbox
    for data in data_list:
        data_listbox.insert(tk.END, data)

def on_right_click(event):
    new_menu.tk_popup(event.x_root, event.y_root)

def on_new():
    input_data = simpledialog.askstring("New Node", "Enter the data for the new node:")
    if input_data:
        data_list.append(input_data)
        show_data()

# Create the main window
root = tk.Tk()
root.title("linked list operation")
root.geometry("300x400")

# Create the initial page
initial_page = tk.Frame(root)

# Create a button on the initial page
button = tk.Button(initial_page, text="Linked list", command=open_data_page)
button.pack(pady=50)
# Create the data management page
data_page = tk.Frame(root)

# Create a frame to hold the listbox
list_frame = tk.Frame(data_page)
list_frame.pack(pady=10)

# Create a listbox to display the data
data_listbox = tk.Listbox(list_frame, width=30)
data_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Configure the listbox and scrollbar
data_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=data_listbox.yview)

# Create a right-click menu
new_menu = tk.Menu(root, tearoff=0)
new_menu.add_command(label="New Node", command=on_new)
new_menu.add_command(label=" Add", command=on_new)
new_menu.add_command(label="Update", command=update_data)
new_menu.add_command(label="Search", command=search_data)
new_menu.add_command(label="Remove", command=remove_data)

root.bind("<Button-3>", on_right_click)

# Show the initial page
initial_page.pack()

# Start the main event loop
root.mainloop()
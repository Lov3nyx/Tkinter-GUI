import tkinter as tk  # Import the Tkinter library for GUI

# Function to add a task to the listbox
def add_task():
    task = task_entry.get()  # Get the text from entry
    if task:
        task_listbox.insert(tk.END, task)  # Add the task to the listbox
        task_entry.delete(0, tk.END)

# Removes the selected task
def remove_task():
    selected_task = task_listbox.curselection()  
    if selected_task:  
        task_listbox.delete(selected_task)  

# Creates main application window
root = tk.Tk()
root.title("To-Do List")  # Set window title
root.geometry("600x400")  # Set window size (w x h)

# Create an entry field where users can type tasks
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.grid(row=0, column=0, columnspan=2) 

# Create a button to add tasks to the listbox
tk.Button(root, text="Add", command=add_task).grid(row=1, column=0) 

# Create a button to remove the selected task from the listbox
tk.Button(root, text="Remove", command=remove_task).grid(row=1, column=1) 

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, font=("Arial", 14), height=15)
task_listbox.grid(row=2, column=0, columnspan=2)


root.mainloop()

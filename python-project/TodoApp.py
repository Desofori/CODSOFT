import tkinter as tk
from tkinter import messagebox

# Initialize the main window
window = tk.Tk()
window.title("To-Do List Application")
window.geometry("400x450")

# Global list to store tasks
tasks = []

# Function to update the listbox with tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        del tasks[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to clear all tasks
def clear_tasks():
    global tasks
    tasks = []
    update_listbox()

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = tasks[selected_task_index]
        tasks[selected_task_index] = " (✓) " + task
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully.")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        update_listbox()
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found.")

# Create UI components
frame = tk.Frame(window)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

task_entry = tk.Entry(window, width=50)
task_entry.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
save_button.pack(side=tk.LEFT, padx=5)

load_button = tk.Button(button_frame, text="Load Tasks", command=load_tasks)
load_button.pack(side=tk.LEFT, padx=5)

# Load tasks if any
load_tasks()

# Start the main event loop
window.mainloop()

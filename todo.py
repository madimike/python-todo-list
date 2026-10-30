import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("Python To-Do List App")
root.geometry("400x450")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Entry Box for typing tasks
task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", font=("Arial", 12), bg="#4CAF50", fg="white", width=15, command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, font=("Arial", 12), width=30, height=12, selectbackground="#a6a6a6")
task_listbox.pack(pady=10)

# Delete Task Button
delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), bg="#f44336", fg="white", width=15, command=delete_task)
delete_button.pack(pady=5)

# Run the app window
root.mainloop()
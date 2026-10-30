import tkinter as tk
from tkinter import ttk, messagebox

# Global counter for task numbering
task_counter = 1
selected_item_to_edit = None

def add_task():
    global task_counter, selected_item_to_edit
    task_text = task_entry.get().strip()
    
    if not task_text:
        messagebox.showwarning("Warning", "You must enter a task.")
        return

    # Determine font formatting based on checkboxes
    weight = "bold" if bold_var.get() else "normal"
    slant = "italic" if italic_var.get() else "roman"
    underline = 1 if underline_var.get() else 0

    if selected_item_to_edit:
        # If we were editing an existing task, update it
        current_values = tree.item(selected_item_to_edit, "values")
        tree.item(selected_item_to_edit, values=(current_values[0], task_text, current_values[2]))
        
        # Reset state back to adding
        selected_item_to_edit = None
        add_button.config(text="Add Task", bg="#a6e3a1")
    else:
        # Otherwise, insert a brand new task
        tag_name = f"style_{task_counter}"
        tree.insert(
            "", 
            tk.END, 
            values=(task_counter, task_text, "Not Done"), 
            tags=(tag_name,)
        )
        tree.tag_configure(tag_name, font=("Arial", 11, weight, slant), underline=underline)
        task_counter += 1

    task_entry.delete(0, tk.END)

def load_task_into_box(event=None):
    global selected_item_to_edit
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "You must select a task to edit.")
        return
    
    selected_item_to_edit = selected_items[0]
    current_values = tree.item(selected_item_to_edit, "values")
    
    # Put the task text into the entry box
    task_entry.delete(0, tk.END)
    task_entry.insert(0, current_values[1])
    task_entry.focus()
    
    # Change Add button to Update button to indicate editing mode
    add_button.config(text="Update Task", bg="#f9e2af")

def mark_complete():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")
        return
    
    for item in selected_items:
        current_values = tree.item(item, "values")
        tree.item(item, values=(current_values[0], current_values[1], "Done"))

def mark_not_done():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "You must select a task to mark as not done.")
        return
    
    for item in selected_items:
        current_values = tree.item(item, "values")
        tree.item(item, values=(current_values[0], current_values[1], "Not Done"))

def delete_task():
    global selected_item_to_edit
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "You must select a task to delete.")
        return
    
    for item in selected_items:
        if item == selected_item_to_edit:
            selected_item_to_edit = None
            add_button.config(text="Add Task", bg="#a6e3a1")
        tree.delete(item)

# Create main window
root = tk.Tk()
root.title("TaskCraft — Precision Task Manager")
root.geometry("520x650")
root.config(bg="#1e1e2e")

# Style configuration for a modern look
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#313244", foreground="white")
style.configure("Treeview", font=("Arial", 11), rowheight=28, background="#24273a", fieldbackground="#24273a", foreground="white")

# Title Header & Logo Branding
title_label = tk.Label(root, text="🛠️ TaskCraft", font=("Arial", 20, "bold"), bg="#1e1e2e", fg="#89b4fa")
title_label.pack(pady=10)

subtitle_label = tk.Label(root, text="Build your productivity, one task at a time.", font=("Arial", 10, "italic"), bg="#1e1e2e", fg="#a6adc8")
subtitle_label.pack(pady=(0, 10))

# Entry Frame
entry_frame = tk.Frame(root, bg="#1e1e2e")
entry_frame.pack(pady=5)

task_entry = tk.Entry(entry_frame, font=("Arial", 13), width=26, bg="#313244", fg="white", insertbackground="white")
task_entry.pack(side=tk.LEFT, padx=5, ipady=4)
task_entry.bind("<Return>", lambda e: add_task())

add_button = tk.Button(entry_frame, text="Add Task", font=("Arial", 11, "bold"), bg="#a6e3a1", fg="#1e1e2e", activebackground="#94e2d5", command=add_task, relief="flat", padx=10)
add_button.pack(side=tk.LEFT, padx=5)

# Formatting Options Frame (Bold, Italic, Underline checkboxes)
format_frame = tk.Frame(root, bg="#1e1e2e")
format_frame.pack(pady=8)

bold_var = tk.BooleanVar()
italic_var = tk.BooleanVar()
underline_var = tk.BooleanVar()

bold_chk = tk.Checkbutton(format_frame, text="Bold", variable=bold_var, bg="#1e1e2e", fg="#cdd6f4", selectcolor="#313244", activebackground="#1e1e2e", activeforeground="white", font=("Arial", 10))
bold_chk.pack(side=tk.LEFT, padx=10)

italic_chk = tk.Checkbutton(format_frame, text="Italic", variable=italic_var, bg="#1e1e2e", fg="#cdd6f4", selectcolor="#313244", activebackground="#1e1e2e", activeforeground="white", font=("Arial", 10))
italic_chk.pack(side=tk.LEFT, padx=10)

underline_chk = tk.Checkbutton(format_frame, text="Underline", variable=underline_var, bg="#1e1e2e", fg="#cdd6f4", selectcolor="#313244", activebackground="#1e1e2e", activeforeground="white", font=("Arial", 10))
underline_chk.pack(side=tk.LEFT, padx=10)

# Table / Treeview with Columns (Number, Task, Status)
columns = ("No.", "Task Description", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings", height=11)

tree.heading("No.", text="No.")
tree.heading("Task Description", text="Task Description (Double-click to edit)")
tree.heading("Status", text="Status")

tree.column("No.", width=50, anchor=tk.CENTER)
tree.column("Task Description", width=290, anchor=tk.W)
tree.column("Status", width=120, anchor=tk.CENTER)

tree.pack(pady=10, padx=20)

# Bind double-click to load task into the main entry box for editing
tree.bind("<Double-1>", load_task_into_box)

# Action Buttons Frame 1 (Status & Edit in Box)
btn_frame_1 = tk.Frame(root, bg="#1e1e2e")
btn_frame_1.pack(pady=5)

edit_box_btn = tk.Button(btn_frame_1, text="✏️ Edit in Box", font=("Arial", 10, "bold"), bg="#f9e2af", fg="#1e1e2e", command=load_task_into_box, relief="flat", width=14, pady=4)
edit_box_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame_1, text="✔ Mark as Done", font=("Arial", 10, "bold"), bg="#89b4fa", fg="#1e1e2e", command=mark_complete, relief="flat", width=14, pady=4)
done_btn.grid(row=0, column=1, padx=5)

not_done_btn = tk.Button(btn_frame_1, text="✘ Mark Not Done", font=("Arial", 10, "bold"), bg="#fab387", fg="#1e1e2e", command=mark_not_done, relief="flat", width=14, pady=4)
not_done_btn.grid(row=0, column=2, padx=5)

# Action Buttons Frame 2 (Delete)
btn_frame_2 = tk.Frame(root, bg="#1e1e2e")
btn_frame_2.pack(pady=5)

delete_btn = tk.Button(btn_frame_2, text="🗑 Delete Task", font=("Arial", 10, "bold"), bg="#f38ba8", fg="#1e1e2e", command=delete_task, relief="flat", width=22, pady=4)
delete_btn.grid(row=0, column=0, padx=5)

root.mainloop()
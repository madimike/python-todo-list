import tkinter as tk
from tkinter import ttk, messagebox

# Global counter for task numbering
task_counter = 1

def add_task():
    global task_counter
    task_text = task_entry.get().strip()
    
    if not task_text:
        messagebox.showwarning("Warning", "You must enter a task.")
        return

    # Determine font formatting based on checkboxes
    weight = "bold" if bold_var.get() else "normal"
    slant = "italic" if italic_var.get() else "roman"
    underline = 1 if underline_var.get() else 0

    # Create a unique tag name for this style combination
    tag_name = f"style_{task_counter}"
    
    # Insert into the Treeview table
    tree.insert(
        "", 
        tk.END, 
        values=(task_counter, task_text, "Not Done"), 
        tags=(tag_name,)
    )
    
    # Configure the font style dynamically for this specific tag
    tree.tag_configure(tag_name, font=("Arial", 11, weight, slant), underline=underline)
    
    task_counter += 1
    task_entry.delete(0, tk.END)

def mark_complete():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")
        return
    
    for item in selected_items:
        current_values = tree.item(item, "values")
        # Update status column to "Done"
        tree.item(item, values=(current_values[0], current_values[1], "Done"))

def mark_not_done():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "You must select a task to mark as not done.")
        return
    
    for item in selected_items:
        current_values = tree.item(item, "values")
        # Update status column back to "Not Done"
        tree.item(item, values=(current_values[0], current_values[1], "Not Done"))

def delete_task():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "You must select a task to delete.")
        return
    
    for item in selected_items:
        tree.delete(item)

# Create main window
root = tk.Tk()
root.title("Glow Theory - Pro To-Do List")
root.geometry("520x620")
root.config(bg="#1e1e2e")

# Style configuration for a modern look
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#313244", foreground="white")
style.configure("Treeview", font=("Arial", 11), rowheight=28, background="#24273a", fieldbackground="#24273a", foreground="white")

# Title Label
title_label = tk.Label(root, text="✨ Pro Task Manager", font=("Arial", 18, "bold"), bg="#1e1e2e", fg="#cba6f7")
title_label.pack(pady=10)

# Entry Frame
entry_frame = tk.Frame(root, bg="#1e1e2e")
entry_frame.pack(pady=5)

task_entry = tk.Entry(entry_frame, font=("Arial", 13), width=32, bg="#313244", fg="white", insertbackground="white")
task_entry.pack(side=tk.LEFT, padx=5, ipady=4)

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
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

tree.heading("No.", text="No.")
tree.heading("Task Description", text="Task Description")
tree.heading("Status", text="Status")

tree.column("No.", width=50, anchor=tk.CENTER)
tree.column("Task Description", width=290, anchor=tk.W)
tree.column("Status", width=120, anchor=tk.CENTER)

tree.pack(pady=10, padx=20)

# Action Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

done_btn = tk.Button(btn_frame, text="✔ Mark as Done", font=("Arial", 10, "bold"), bg="#89b4fa", fg="#1e1e2e", command=mark_complete, relief="flat", width=14, pady=4)
done_btn.grid(row=0, column=0, padx=5)

not_done_btn = tk.Button(btn_frame, text="✘ Mark Not Done", font=("Arial", 10, "bold"), bg="#f9e2af", fg="#1e1e2e", command=mark_not_done, relief="flat", width=14, pady=4)
not_done_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="🗑 Delete Task", font=("Arial", 10, "bold"), bg="#f38ba8", fg="#1e1e2e", command=delete_task, relief="flat", width=14, pady=4)
delete_btn.grid(row=0, column=2, padx=5)

root.mainloop()
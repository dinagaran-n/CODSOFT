import tkinter as tk
from tkinter import messagebox, simpledialog

# Add new task
def add_task():
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    selected = listbox_tasks.curselection()
    if selected:
        listbox_tasks.delete(selected[0])
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Clear all tasks
def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Mark task as Done
def mark_done():
    selected = listbox_tasks.curselection()
    if selected:
        task = listbox_tasks.get(selected[0])
        if "✓" not in task:
            listbox_tasks.delete(selected[0])
            listbox_tasks.insert(selected[0], f"{task} ✓")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Update/Edit selected task
def update_task():
    selected = listbox_tasks.curselection()
    if selected:
        old_task = listbox_tasks.get(selected[0])
        new_task = simpledialog.askstring("Update Task", "Edit the task:", initialvalue=old_task.replace(" ✓", ""))
        if new_task:
            if "✓" in old_task:
                new_task += " ✓"
            listbox_tasks.delete(selected[0])
            listbox_tasks.insert(selected[0], new_task)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

# Setup the main window
root = tk.Tk()
root.title("To-Do List")
root.iconbitmap("icon.ico")
root.geometry("400x450")
root.configure(bg="lightblue")
root.resizable(False, False)

# Title label
tk.Label(root, text="📝 To-Do List", font=("Helvetica", 16)).pack(pady=10)

# Entry
entry_task = tk.Entry(root, width=35, font=("Helvetica", 12))
entry_task.pack(pady=5)

# Buttons frame
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Task", width=12, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update Task", width=12, command=update_task).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Mark as Done", width=12, command=mark_done).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Delete Task", width=12, command=delete_task).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Clear All Tasks", width=30, command=clear_tasks).pack(pady=5)

# Listbox
listbox_tasks = tk.Listbox(root, width=45, height=12, font=("Courier", 11))
listbox_tasks.pack(pady=10)

# Run the app
root.mainloop()

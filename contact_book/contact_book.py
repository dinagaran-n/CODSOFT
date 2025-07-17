import tkinter as tk
from tkinter import messagebox
import json
import os

contacts = []
DATA_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    global contacts
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            contacts = json.load(file)

# Save contacts to file
def save_contacts():
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Functions
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        save_contacts()
        messagebox.showinfo("Success", "Contact added successfully.")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def view_contacts():
    listbox_contacts.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        listbox_contacts.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

def on_contact_select(event):
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact['name'])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact['phone'])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact['email'])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact['address'])
        btn_update.grid()
        btn_delete.grid()
    else:
        btn_update.grid_remove()
        btn_delete.grid_remove()

def update_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contacts[index] = {
            'name': entry_name.get().strip(),
            'phone': entry_phone.get().strip(),
            'email': entry_email.get().strip(),
            'address': entry_address.get().strip()
        }
        save_contacts()
        messagebox.showinfo("Updated", "Contact updated successfully.")
        view_contacts()
        clear_fields()

def delete_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        confirm = messagebox.askyesno("Confirm", "Delete this contact?")
        if confirm:
            contacts.pop(index)
            save_contacts()
            view_contacts()
            clear_fields()
            messagebox.showinfo("Deleted", "Contact deleted.")

def search_contact():
    query = entry_search.get().strip().lower()
    listbox_contacts.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        if query in contact['name'].lower() or query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")
    if listbox_contacts.size() == 0:
        messagebox.showinfo("No Match", "No contact found.")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    btn_update.grid_remove()
    btn_delete.grid_remove()

def focus_next(event, widget):
    widget.focus_set()
    return "break"

# GUI Setup
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("600x600")
root.config(bg="#f5f5f5")

font_label = ("Segoe UI", 11)
font_entry = ("Segoe UI", 11)
font_button = ("Segoe UI", 10, "bold")

# --- Entry Frame ---
frame_entry = tk.LabelFrame(root, text="Add / Edit Contact", bg="#ffffff", font=("Segoe UI", 12, "bold"))
frame_entry.pack(fill="x", padx=20, pady=10)

tk.Label(frame_entry, text="Name:", font=font_label, bg="#ffffff").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_entry, width=40, font=font_entry)
entry_name.grid(row=0, column=1, pady=5)
entry_name.bind("<Return>", lambda e: focus_next(e, entry_phone))

tk.Label(frame_entry, text="Phone:", font=font_label, bg="#ffffff").grid(row=1, column=0, sticky="w")
entry_phone = tk.Entry(frame_entry, width=40, font=font_entry)
entry_phone.grid(row=1, column=1, pady=5)
entry_phone.bind("<Return>", lambda e: focus_next(e, entry_email))

tk.Label(frame_entry, text="Email:", font=font_label, bg="#ffffff").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame_entry, width=40, font=font_entry)
entry_email.grid(row=2, column=1, pady=5)
entry_email.bind("<Return>", lambda e: focus_next(e, entry_address))

tk.Label(frame_entry, text="Address:", font=font_label, bg="#ffffff").grid(row=3, column=0, sticky="w")
entry_address = tk.Entry(frame_entry, width=40, font=font_entry)
entry_address.grid(row=3, column=1, pady=5)
entry_address.bind("<Return>", lambda e: focus_next(e, btn_add))

# --- Buttons ---
btn_add = tk.Button(frame_entry, text="Add Contact", font=font_button, bg="#4CAF50", fg="white", width=15, command=add_contact)
btn_add.grid(row=4, column=0, pady=10)

btn_update = tk.Button(frame_entry, text="Update", font=font_button, bg="#2196F3", fg="white", width=15, command=update_contact)
btn_update.grid(row=4, column=1, sticky="w", pady=10)
btn_update.grid_remove()

btn_delete = tk.Button(frame_entry, text="Delete", font=font_button, bg="#f44336", fg="white", width=15, command=delete_contact)
btn_delete.grid(row=5, column=0, pady=5)
btn_delete.grid_remove()

# --- Search & Contact List ---
frame_list = tk.LabelFrame(root, text="Search Contact", font=("Segoe UI", 12, "bold"), bg="#ffffff")
frame_list.pack(fill="x", padx=20, pady=5)

entry_search = tk.Entry(frame_list, width=30, font=font_entry)
entry_search.pack(side="left", padx=10, pady=10)

tk.Button(frame_list, text="Search", font=font_button, command=search_contact).pack(side="left")

listbox_contacts = tk.Listbox(root, width=65, height=10, font=("Segoe UI", 11))
listbox_contacts.pack(padx=20, pady=10)
listbox_contacts.bind("<<ListboxSelect>>", on_contact_select)

# --- Extra Buttons ---
frame_actions = tk.Frame(root, bg="#f5f5f5")
frame_actions.pack(pady=5)

tk.Button(frame_actions, text="View All", font=font_button, width=15, bg="#9C27B0", fg="white", command=view_contacts).grid(row=0, column=0, padx=10)
tk.Button(frame_actions, text="Clear Fields", font=font_button, width=15, bg="#FF9800", fg="white", command=clear_fields).grid(row=0, column=1, padx=10)

# Load and show contacts
load_contacts()
view_contacts()

root.mainloop()

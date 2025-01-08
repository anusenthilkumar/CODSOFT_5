import tkinter as tk
from tkinter import messagebox

# Initialize the contact dictionary
contacts = {}

# Functions for contact book actions
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
    else:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()

def view_contacts():
    contact_list.delete(0, tk.END)
    if not contacts:
        contact_list.insert(tk.END, "No contacts found.")
    else:
        for name, details in contacts.items():
            contact_list.insert(tk.END, f"{name} - {details['Phone']}")

def search_contact():
    search_term = search_entry.get()
    for name, details in contacts.items():
        if name == search_term or details["Phone"] == search_term:
            messagebox.showinfo("Contact Found", 
                                f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            return
    messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Contact not found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Main GUI window
root = tk.Tk()
root.title("Contact Book")

# Labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons for actions
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="View Contacts", command=view_contacts).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=5, column=1, padx=10, pady=10)

# Search entry
tk.Label(root, text="Search by Name/Phone:").grid(row=6, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1, padx=10, pady=5)

# Contact list display
tk.Label(root, text="Contact List:").grid(row=7, column=0, columnspan=2, padx=10, pady=5)
contact_list = tk.Listbox(root, width=40, height=10)
contact_list.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Run the main loop
root.mainloop()

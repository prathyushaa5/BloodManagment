import tkinter as tk
from tkinter import messagebox

from blood import *
from login import*
#Insert data into Blood_Bank table
def insert_blood_bank():
    name = name_entry.get()
    capacity = capacity_entry.get()

    query = "INSERT INTO Blood_Bank (Name, Capacity) VALUES (%s, %s)"
    values = (name, capacity)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Blood bank inserted successfully")

# Update data in Blood_Bank table
def update_blood_bank():
    bank_id = bank_id_entry.get()
    new_name = new_name_entry.get()
    new_capacity = new_capacity_entry.get()

    query = "UPDATE Blood_Bank SET Name = %s, Capacity = %s WHERE Bank_ID = %s"
    values = (new_name, new_capacity, bank_id)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Blood bank updated successfully")

# Delete data from Blood_Bank table
def delete_blood_bank():
    bank_id = bank_id_entry.get()

    query = "DELETE FROM Blood_Bank WHERE Bank_ID = %s"
    values = (bank_id,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Blood bank deleted successfully")

# Create the GUI window
root = tk.Tk()
root.title("Blood Bank Management")

# Labels and Entry fields for Blood_Bank
bank_id_label = tk.Label(root, text="Bank ID:")
name_label = tk.Label(root, text="Name:")
capacity_label = tk.Label(root, text="Capacity:")
bank_id_entry = tk.Entry(root)
name_entry = tk.Entry(root)
capacity_entry = tk.Entry(root)
new_name_label = tk.Label(root, text="New Name:")
new_capacity_label = tk.Label(root, text="New Capacity:")
new_name_entry = tk.Entry(root)
new_capacity_entry = tk.Entry(root)

# Buttons for Blood_Bank
insert_button = tk.Button(root, text="Insert Blood Bank", command=insert_blood_bank)
update_button = tk.Button(root, text="Update Blood Bank", command=update_blood_bank)
delete_button = tk.Button(root, text="Delete Blood Bank", command=delete_blood_bank)

# Grid layout for Blood_Bank
bank_id_label.grid(row=0, column=0)
bank_id_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
capacity_label.grid(row=2, column=0)
capacity_entry.grid(row=2, column=1)
insert_button.grid(row=3, columnspan=2)
new_name_label.grid(row=4, column=0)
new_name_entry.grid(row=4, column=1)
new_capacity_label.grid(row=5, column=0)
new_capacity_entry.grid(row=5, column=1)
update_button.grid(row=6, columnspan=2)
delete_button.grid(row=7, columnspan=2)

# Main loop
root.mainloop()
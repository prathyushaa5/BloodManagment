import mysql.connector
import tkinter as tk
import sqlite3
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="blood")
# Function to insert values into the database
def insert_data():
    donor_name = name_entry.get()
    blood_type = blood_type_var.get()

    query = "INSERT INTO donors (name, blood_type) VALUES (%s, %s)"
    cursor.execute(query, (donor_name, blood_type))
    conn.commit()

def delete_data():
    donor_id = id_entry.get()

    query = "DELETE FROM donors WHERE id = %s"
    cursor.execute(query, (donor_id,))
    conn.commit()

def update_data():
    donor_id = id_entry.get()
    new_blood_type = new_blood_type_var.get()

    query = "UPDATE donors SET blood_type = %s WHERE id = %s"
    cursor.execute(query, (new_blood_type, donor_id))
    conn.commit()

# GUI setup
root = tk.Tk()
root.title("Blood Donation System")

name_label = tk.Label(root, text="Donor Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

blood_type_label = tk.Label(root, text="Blood Type:")
blood_type_label.pack()

blood_type_var = tk.StringVar(root)
blood_type_var.set("A+")

blood_type_dropdown = tk.OptionMenu(root, blood_type_var, "A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-")
blood_type_dropdown.pack()

insert_button = tk.Button(root, text="Insert", command=insert_data)
insert_button.pack()

id_label = tk.Label(root, text="Donor ID:")
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

new_blood_type_label = tk.Label(root, text="New Blood Type:")
new_blood_type_label.pack()

new_blood_type_var = tk.StringVar(root)
new_blood_type_var.set("A+")

new_blood_type_dropdown = tk.OptionMenu(root, new_blood_type_var, "A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-")
new_blood_type_dropdown.pack()

update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete_data)
delete_button.pack()

root.mainloop()

# Close the database connection when GUI is closed
conn.close()
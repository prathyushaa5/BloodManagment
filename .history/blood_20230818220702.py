import mysql.connector
import tkinter as tk
from tkinter import messagebox
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database



# Database connection



cursor = db.cursor()

# Insert data into User table
def insert_user():
    username = username_entry.get()
    password = password_entry.get()

    query = "INSERT INTO User (Username, Password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "User inserted successfully")

# Delete data from User table
def delete_user():
    username = username_entry.get()

    query = "DELETE FROM User WHERE Username = %s"
    values = (username,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "User deleted successfully")

# Update data in User table
def update_user():
    username = username_entry.get()
    new_password = new_password_entry.get()

    query = "UPDATE User SET Password = %s WHERE Username = %s"
    values = (new_password, username)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "User updated successfully")

# Create the GUI window
root = tk.Tk()
root.title("User Management")

# Labels and Entry fields for User
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")
new_password_label = tk.Label(root, text="New Password:")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
new_password_entry = tk.Entry(root, show="*")

# Buttons for User
insert_button = tk.Button(root, text="Insert User", command=insert_user)
delete_button = tk.Button(root, text="Delete User", command=delete_user)
update_button = tk.Button(root, text="Update User Password", command=update_user)

# Grid layout for User
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
insert_button.grid(row=2, columnspan=2)
delete_button.grid(row=3, columnspan=2)
new_password_label.grid(row=4, column=0)
new_password_entry.grid(row=4, column=1)
update_button.grid(row=5, columnspan=2)

# Main loop
root.mainloop()

# Close the database connection
db.close()
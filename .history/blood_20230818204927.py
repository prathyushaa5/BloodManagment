import mysql.connector
import tkinter as tk
import sqlite3
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database

from tkinter import messagebox
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)
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

# Insert data into Address table
def insert_address():
    city = city_entry.get()
    neighborhood = neighborhood_entry.get()

    query = "INSERT INTO Address (City, Neighborhood) VALUES (%s, %s)"
    values = (city, neighborhood)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Address inserted successfully")

# Create the GUI window
root = tk.Tk()
root.title("Database Insertion")

# Labels and Entry fields for User
user_label = tk.Label(root, text="User")
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
insert_user_button = tk.Button(root, text="Insert User", command=insert_user)

# Labels and Entry fields for Address
address_label = tk.Label(root, text="Address")
city_label = tk.Label(root, text="City:")
neighborhood_label = tk.Label(root, text="Neighborhood:")
city_entry = tk.Entry(root)
neighborhood_entry = tk.Entry(root)
insert_address_button = tk.Button(root, text="Insert Address", command=insert_address)

# Grid layout for User
user_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
insert_user_button.grid(row=3, columnspan=2)

# Grid layout for Address
address_label.grid(row=0, column=2, columnspan=2)
city_label.grid(row=1, column=2)
city_entry.grid(row=1, column=3)
neighborhood_label.grid(row=2, column=2)
neighborhood_entry.grid(row=2, column=3)
insert_address_button.grid(row=3, column=2, columnspan=2)

# Main loop
root.mainloop()

# Close the database connection
db.close()
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

# Insert data into Address table
def insert_address():
    city = city_entry.get()
    neighborhood = neighborhood_entry.get()

    query = "INSERT INTO Address (City, Neighborhood) VALUES (%s, %s)"
    values = (city, neighborhood)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Address inserted successfully")

# Create the GUI window
root = tk.Tk()
root.title("Database Insertion")

# Labels and Entry fields for User
user_label = tk.Label(root, text="User")
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
insert_user_button = tk.Button(root, text="Insert User", command=insert_user)

# Labels and Entry fields for Address
address_label = tk.Label(root, text="Address")
city_label = tk.Label(root, text="City:")
neighborhood_label = tk.Label(root, text="Neighborhood:")
city_entry = tk.Entry(root)
neighborhood_entry = tk.Entry(root)
insert_address_button = tk.Button(root, text="Insert Address", command=insert_address)

# Grid layout for User
user_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
insert_user_button.grid(row=3, columnspan=2)

# Grid layout for Address
address_label.grid(row=0, column=2, columnspan=2)
city_label.grid(row=1, column=2)
city_entry.grid(row=1, column=3)
neighborhood_label.grid(row=2, column=2)
neighborhood_entry.grid(row=2, column=3)
insert_address_button.grid(row=3, column=2, columnspan=2)

# Main loop
root.mainloop()

# Close the database connection
db.close()
import mysql.connector
import tkinter as tk
import sqlite3
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database

def insert_user():
    username = username_entry.get()
    password = password_entry.get()

    query = "INSERT INTO User (Username, Password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(query, values)

    db.commit()
    db.close()
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("User Insertion")

# Labels
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")

# Entry fields
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

# Insert button
insert_button = tk.Button(root, text="Insert User", command=insert_user)

# Grid layout
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
insert_button.grid(row=2, columnspan=2)

def insert_data():
    Address_ID = Address_ID_entry.get()
    City = City_entry.get()
    Neighborhood = Neighborhood_entry.get()
    cursor = db.cursor()

    # Insert values into the address_table
    query = "INSERT INTO address_table (address_id, city, neighborhood) VALUES (%s, %s, %s)"
    values = (Address_ID, City, Neighborhood)
    cursor.execute(query, values)

    # Commit changes and close the connection
    db.commit()
    db.close()

    # Clear the entry fields
    Address_ID_entry.delete(0, tk.END)
    City_entry.delete(0, tk.END)
    Neighborhood_entry.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
root.title("Insert Address")

# Labels
Address_ID_label = tk.Label(root, text="Address ID:")
City_label = tk.Label(root, text="City:")
Neighborhood_label = tk.Label(root, text="Neighborhood:")

# Entry fields
Address_ID_entry = tk.Entry(root)
City_entry = tk.Entry(root)
Neighborhood_entry = tk.Entry(root)

# Insert button
insert_button = tk.Button(root, text="Insert", command=insert_data)

# Grid layout
Address_ID_label.grid(row=0, column=0)
Address_ID_entry.grid(row=0, column=1)
City_label.grid(row=1, column=0)
City_entry.grid(row=1, column=1)
Neighborhood_label.grid(row=2, column=0)
Neighborhood_entry.grid(row=2, column=1)
insert_button.grid(row=3, columnspan=2)

# Start the GUI main loop


root.mainloop()


import mysql.connector
import tkinter as tk
from tkinter import messagebox
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database
# Database connection
cursor = db.cursor()
def address():
   def insert_address():
       Address_ID=Address_ID_entry.get()
       City = City_entry.get()
       District=District_entry.get()
       Neighborhood = Neighborhood_entry.get()

       query = "INSERT INTO Address (Address_ID,City,District,Neighborhood) VALUES (%s,%s,%s, %s)"
       values = (Address_ID,City,District,Neighborhood)
       cursor.execute(query,values)
       db.commit()
       messagebox.showinfo("Success", "Address inserted successfully")
       root.destroy()
       
       
       
       
       
   def update_address():
       Address_ID = Address_ID_entry.get()
       new_City = new_City_entry.get()
       new_District=new_District_entry.get()
       new_Neighborhood = new_Neighborhood_entry.get()

       query = "UPDATE Address SET City = %s,District=%s,Neighborhood = %s WHERE Address_ID = %s"
       values = (new_City, new_District,new_Neighborhood, Address_ID)
       cursor.execute(query, values)
       db.commit()
       messagebox.showinfo("Success", "Address updated successfully")
       root.destroy()

# Delete data from Address table
   def delete_address():
       Address_ID = int(Address_ID_entry.get())

       query = "DELETE FROM Address WHERE Address_ID = %s"
       values = (Address_ID,)
       cursor.execute(query, values)
       db.commit()
       messagebox.showinfo("Success", "Address deleted successfully")
       root.destroy()
   def next():
    print() 
    root.destroy()      

# Create the GUI window
   root = tk.Tk()
   root.title("Address Management")

# Labels and Entry fields for Address
   Address_ID_label = tk.Label(root, text="Address ID:")
   City_label = tk.Label(root, text="City:")
   District_label = tk.Label(root, text="District:")
   Neighborhood_label = tk.Label(root, text="Neighborhood:")
   Address_ID_entry = tk.Entry(root)
   City_entry = tk.Entry(root)
   District_entry=tk.Entry(root)
   Neighborhood_entry = tk.Entry(root)
   new_City_label = tk.Label(root, text="New City:")
   new_District_label = tk.Label(root, text="New District:")
   new_Neighborhood_label = tk.Label(root, text="New Neighborhood:")
   new_City_entry = tk.Entry(root)
   new_District_entry=tk.Entry(root)
   new_Neighborhood_entry = tk.Entry(root)

# Buttons for Address
   insert_button = tk.Button(root, text="Insert Address", command=insert_address)
   update_button = tk.Button(root, text="Update Address", command=update_address)
   delete_button = tk.Button(root, text="Delete Address", command=delete_address)
   next_button=tk.Button(root,text="Next",command=next)


# Grid layout for Address
   Address_ID_label.grid(row=0, column=0)
   Address_ID_entry.grid(row=0, column=1)
   City_label.grid(row=1, column=0)
   City_entry.grid(row=1, column=1)
   District_label.grid(row=2,column=0)
   District_entry.grid(row=2,column=1)
   Neighborhood_label.grid(row=3, column=0)
   Neighborhood_entry.grid(row=3, column=1)
   insert_button.grid(row=4, columnspan=2)
   new_City_label.grid(row=5, column=0)
   new_City_entry.grid(row=5, column=1)
   new_District_label.grid(row=6, column=0)
   new_District_entry.grid(row=6, column=1)
   new_Neighborhood_label.grid(row=7, column=0)
   new_Neighborhood_entry.grid(row=7, column=1)
   update_button.grid(row=8, columnspan=2)
   delete_button.grid(row=9, columnspan=2)
   next_button.grid(row=10,columnspan=3)
   root.mainloop()
 
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
       blood_type()
       
       
       
       
       
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
       blood_type()

# Delete data from Address table
   def delete_address():
       Address_ID = int(Address_ID_entry.get())

       query = "DELETE FROM Address WHERE Address_ID = %s"
       values = (Address_ID,)
       cursor.execute(query, values)
       db.commit()
       messagebox.showinfo("Success", "Address deleted successfully")
       root.destroy()
       blood_type()
   def next():
    print() 
    root.destroy() 
    blood_type()     

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
   
   
def blood_type():
   def display_blood_type():
      query = "SELECT * FROM Blood_Type"
      cursor.execute(query)
      results = cursor.fetchall()

      display_text.delete(1.0, tk.END)  # Clear the current text
      for result in results:
        display_text.insert(tk.END, f"Blood_ID: {result[0]}\n")
        display_text.insert(tk.END, f"Blood_Code: {result[1]}\n")
        display_text.insert(tk.END, f"Donates_To: {result[2]}\n")
        display_text.insert(tk.END, f"Receives_From: {result[3]}\n\n")
   def next():
       print()
       root.destroy() 
       donor()
            

   # Create the GUI window
   root = tk.Tk()
   root.title("Blood Type Display")

   # Button for displaying Blood_Type
   display_button = tk.Button(root, text="Display Blood Type", command=display_blood_type)
   next_button=tk.Button(root,text="Next",command=next)

   # Text widget to display results
   display_text = tk.Text(root, height=10, width=40)


   # Grid layout
   display_button.grid(row=0, column=0, columnspan=2)
   display_text.grid(row=1, column=0, columnspan=2)
   next_button.grid(row=1,column=3,columnspan=2)

# Main loop
   root.mainloop()

def donor():
    def insert_donor():
    
     Donor_ID = Donor_ID_entry.get()
     First_Name = First_Name_entry.get()
     Last_Name = Last_Name_entry.get()
     Blood_ID = Blood_ID_entry.get()
     Address_ID= Address_ID_entry.get()

     
     db.execute("SELECT COUNT(*) FROM Blood_Type WHERE Blood_ID=%s",(Blood_ID))
     count=db.fetchone()[0]
     db.execute("SELECT COUNT(*) FROM Address WHERE ADDRESS_ID=%s",(Address_ID))
     if count==0:
         print("the Blood_id doesn't exist in the database\nPlease enter a valid one")
     count=db.fetchone()[0]
     if count==0:
         print("the address_id doesn't exist in the database\nPlease enter a valid one")
     query = "INSERT INTO Donor (Donor_ID,First_Name, Last_Name, Blood_ID, Address_ID) VALUES (%s,%s, %s, %s, %s)"
     values = (Donor_ID,First_Name, Last_Name, Blood_ID,Address_ID)
     cursor.execute(query, values)
     db.commit()
     messagebox.showinfo("Success", "Donor inserted successfully")

# Update data in Donor table
    def update_donor():
      Donor_ID = int(Donor_ID_entry.get())
      new_First_Name = new_First_Name_entry.get()
      new_Last_Name = new_Last_Name_entry.get()
      new_Blood_ID = new_Blood_ID_entry.get()
      new_Address_ID = new_Address_ID_entry.get()

      query = "UPDATE Donor SET First_Name = %s, Last_Name = %s WHERE Donor_ID = %s"
      values = (new_First_Name, new_Last_Name,new_Blood_ID,new_Address_ID, Donor_ID)
      cursor.execute(query, values)
      db.commit()
      root.destroy()
      display_donor_details()
      messagebox.showinfo("Success", "Donor updated successfully")

# Delete data from Donor table
    def delete_donor():
      Donor_ID= Donor_ID_entry.get()

      query = "DELETE FROM Donor WHERE Donor_ID = %s"
      values = (Donor_ID,)
      cursor.execute(query, values)
      db.commit()
      root.destroy()
      display_donor_details()
      messagebox.showinfo("Success", "Donor deleted successfully")
    
    def display_donor_details():
      cursor.execute("SELECT * FROM Donor")
      donor_data = cursor.fetchall()
    
      result_text.delete(1.0, tk.END)  # Clear previous content
      for donor in donor_data:
        result_text.insert(tk.END, f"ID: {donor[0]}, First Name: {donor[1]}, Last Name: {donor[2]}, Blood ID: {donor[3]}, Address ID: {donor[4]}\n")    
    
    def next():
      root.destroy()   
      
   # Create the GUI window
    root = tk.Tk()
    root.title("Donor Management")

# Labels and Entry fields for Donor
    Donor_ID_label = tk.Label(root, text="Donor ID:")
    First_Name_label = tk.Label(root, text="First Name:")
    Last_Name_label = tk.Label(root, text="Last Name:")
    Blood_ID_label = tk.Label(root, text="Blood ID:")
    Address_ID_label = tk.Label(root, text="Address ID:")
    Donor_ID_entry = tk.Entry(root)
    First_Name_entry = tk.Entry(root)
    Last_Name_entry = tk.Entry(root)
    Blood_ID_entry = tk.Entry(root)
    Address_ID_entry = tk.Entry(root)
    new_First_Name_label = tk.Label(root, text="New First Name:")
    new_Last_Name_label = tk.Label(root, text="New Last Name:")
    new_First_Name_label = tk.Label(root, text="New First Name:")
    new_Address_ID_label = tk.Label(root, text="New Address_ID:")
    new_Blood_ID_label=tk.Label(root,text="New blood id:")
    new_First_Name_entry = tk.Entry(root)
    new_Last_Name_entry = tk.Entry(root)
    new_Address_ID_entry = tk.Entry(root)
    new_Blood_ID_entry = tk.Entry(root)

# Buttons for Donor
    insert_button = tk.Button(root, text="Insert Donor", command=insert_donor)
    update_button = tk.Button(root, text="Update Donor", command=update_donor)
    delete_button = tk.Button(root, text="Delete Donor", command=delete_donor)
    display_button =tk. Button(root, text="Display Donor Details", command=display_donor_details)
    result_text = tk.Text(root, wrap=tk.WORD,width=50, height=10)
    next_button=tk.Button(root,text="Next",command=next)

# Grid layout for Donor
    Donor_ID_label.grid(row=0, column=0)
    Donor_ID_entry.grid(row=0, column=1)
    First_Name_label.grid(row=1, column=0)
    First_Name_entry.grid(row=1, column=1)
    Last_Name_label.grid(row=2, column=0)
    Last_Name_entry.grid(row=2, column=1)
    Blood_ID_label.grid(row=3, column=0)
    Blood_ID_entry.grid(row=3, column=1)
    Address_ID_label.grid(row=4, column=0)
    Address_ID_entry.grid(row=4, column=1)
    insert_button.grid(row=5, columnspan=2)
    new_First_Name_label.grid(row=6, column=0)
    new_First_Name_entry.grid(row=6, column=1)
    new_Last_Name_label.grid(row=7, column=0)
    new_Last_Name_entry.grid(row=7, column=1)
    new_Address_ID_label.grid(row=8, column=0)
    new_Address_ID_entry.grid(row=8, column=1)
    new_Blood_ID_label.grid(row=9, column=0)
    new_Blood_ID_entry.grid(row=9, column=1)
    update_button.grid(row=10, columnspan=2)
    delete_button.grid(row=11, columnspan=2)
    display_button.grid(row=12, columnspan=2)
    result_text.grid(row=13, column=0, padx=10, pady=10)
    next_button.grid(row=14,columnspan=2)

# Main loop
    root.mainloop() 
    

 
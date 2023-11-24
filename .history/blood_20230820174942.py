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
       cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(Address_ID,))
       count1=cursor.fetchone()[0]
       if count1>0:
           messagebox.showinfo("Address_ID already taken")
       else:    
           query = "INSERT INTO Address (Address_ID,City,District,Neighborhood) VALUES (%s,%s,%s, %s)"
           values = (Address_ID,City,District,Neighborhood)
           cursor.execute(query,values)
           db.commit()
           messagebox.showinfo("Success", "Address inserted successfully")
           
       
       
       
       
       
   def update_address():
       Address_ID = Address_ID_entry.get()
       new_City = new_City_entry.get()
       new_District=new_District_entry.get()
       new_Neighborhood = new_Neighborhood_entry.get()
       cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(Address_ID,))
       count1=cursor.fetchone()[0]
       if count1==0:
           messagebox.showinfo("Enter a valid Address_ID to update!")
       else:    
           query = "UPDATE Address SET City = %s,District=%s,Neighborhood = %s WHERE Address_ID = %s"
           values = (new_City, new_District,new_Neighborhood, Address_ID)
           cursor.execute(query, values)
           db.commit()
           messagebox.showinfo("Success", "Address updated successfully")
           
# Delete data from Address table
   def delete_address():
       Address_ID = int(Address_ID_entry.get())
       cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(Address_ID,))
       count1=cursor.fetchone()[0]
       if count1==0:
           messagebox.showinfo("Enter a valid Address_ID to delete!")
       else:    
           query = "DELETE FROM Address WHERE Address_ID = %s"
           values = (Address_ID,)
           cursor.execute(query, values)
           db.commit()
           messagebox.showinfo("Success", "Address deleted successfully")
           
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
       choice()
   def previous():
        root.destroy()
        address()
                    

   # Create the GUI window
   root = tk.Tk()
   root.title("Blood Type Display")

   # Button for displaying Blood_Type
   display_button = tk.Button(root, text="Display Blood Type", command=display_blood_type)
   next_button=tk.Button(root,text="Next",command=next)
   previous_button=tk.Button(root,text="Prev",command=previous)

   # Text widget to display results
   display_text = tk.Text(root, height=10, width=40)


   # Grid layout
   display_button.grid(row=0, column=0, columnspan=2)
   display_text.grid(row=1, column=0, columnspan=2)
   previous_button.grid(row=2,column=0,columnspan=3)
   next_button.grid(row=2,column=1,columnspan=2)
   
   

# Main loop
   root.mainloop()
def choice():
    root=tk.Tk()
    root.title("Donor/Rec")
    d_button=tk.Button(root,text="Donor",command=donor)
    d_button.grid(row=0,column=0,columnspan=1)
    r_button=tk.Button(root,text="Recipient",command=recipient)
    r_button.grid(row=0,column=1,columnspan=1)
    def next():
      root.destroy()
      
    def previous():
        root.destroy()
        blood_type()
    next_button=tk.Button(root,text="Next",command=next)
    previous_button=tk.Button(root,text="prev",command=previous)
    previous_button.grid(row=2,column=0,columnspan=1)
    next_button.grid(row=2,column=1,columnspan=1)
    



def donor():
    root.destroy()
    def insert_donor():
     
     Donor_ID = Donor_ID_entry.get()
     First_Name = First_Name_entry.get()
     Last_Name = Last_Name_entry.get()
     Blood_ID = Blood_ID_entry.get()
     Address_ID= Address_ID_entry.get()

     
     cursor.execute("SELECT COUNT(*) FROM Blood_Type WHERE Blood_ID=%s",(Blood_ID,))
     count1=cursor.fetchone()[0]
     if count1==0:
         messagebox.showinfo("Insert a valid Blood_ID")
     cursor.execute("SELECT COUNT(*) FROM Address WHERE Address_ID=%s",(Address_ID,))    
     count2=cursor.fetchone()[0]
     if count2==0:
         messagebox.showinfo("Insert a valid Address_ID")
     if count1>0 and count2>0:
        cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
        count3=cursor.fetchone()[0]
        if count3>0:
           messagebox.showinfo("Donor_ID already taken!")
        else:        
           query = "INSERT INTO Donor (Donor_ID,First_Name, Last_Name, Blood_ID, Address_ID) VALUES (%s,%s, %s, %s, %s)"
           values = (Donor_ID,First_Name, Last_Name, Blood_ID,Address_ID)
           cursor.execute(query, values)
           db.commit()
           root.destroy()
           messagebox.showinfo("Success", "Donor inserted successfully")

# Update data in Donor table
    def update_donor():
      Donor_ID = int(Donor_ID_entry.get())
      new_First_Name = new_First_Name_entry.get()
      new_Last_Name = new_Last_Name_entry.get()
      new_Address_ID = new_Address_ID_entry.get()
      cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
      count1=cursor.fetchone()[0]
      if count1==0:
           messagebox.showinfo("Enter a valid Donor_ID to update!")
      else:
          cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(new_Address_ID,))
          count3=cursor.fetchone()[0]
          if count3==0:
           messagebox.showinfo("Enter a valid Address_ID!")
          else:       
           query = "UPDATE Donor SET First_Name = %s, Last_Name = %s,Address_ID=%s WHERE Donor_ID = %s"
           values = (new_First_Name, new_Last_Name,new_Address_ID, Donor_ID)
           cursor.execute(query, values)
           db.commit()
           root.destroy()
           display_donor_details()
           messagebox.showinfo("Success", "Donor updated successfully")

# Delete data from Donor table
    def delete_donor():
      Donor_ID= Donor_ID_entry.get()
      cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
      count1=cursor.fetchone()[0]
      if count1==0:
           messagebox.showinfo("Enter a valid Donor_ID to delete!")
      else:     
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
      
    def previous():
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
    new_First_Name_entry = tk.Entry(root)
    new_Last_Name_entry = tk.Entry(root)
    new_Address_ID_entry = tk.Entry(root)

# Buttons for Donor
    insert_button = tk.Button(root, text="Insert Donor", command=insert_donor)
    update_button = tk.Button(root, text="Update Donor", command=update_donor)
    delete_button = tk.Button(root, text="Delete Donor", command=delete_donor)
    display_button =tk. Button(root, text="Display Donor Details", command=display_donor_details)
    result_text = tk.Text(root, wrap=tk.WORD,width=50, height=10)
    next_button=tk.Button(root,text="Next",command=next)
    previous_button=tk.Button(root,text="prev",command=previous)

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
    update_button.grid(row=10, columnspan=2)
    delete_button.grid(row=11, columnspan=2)
    display_button.grid(row=12, columnspan=2)
    result_text.grid(row=13, column=0, padx=10, pady=10)
    previous_button.grid(row=14,column=0,columnspan=1)
    next_button.grid(row=14,column=1,columnspan=1)
    

# Main loop
    root.mainloop() 
    



def recipient():
  def insert_recipient():
    Recipient_ID=Recipient_ID_entry.get()
    First_Name = First_Name_entry.get()
    Last_Name = Last_Name_entry.get()
    Blood_ID = Blood_ID_entry.get()
    Address_ID = Address_ID_entry.get()
    Phone_No = Phone_No_entry.get()
    cursor.execute("SELECT COUNT(*) FROM Blood_Type WHERE Blood_ID=%s",(Blood_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
        messagebox.showinfo("Insert a valid Blood_ID")
    cursor.execute("SELECT COUNT(*) FROM Address WHERE Address_ID=%s",(Address_ID,))    
    count2=cursor.fetchone()[0]
    if count2==0:
        messagebox.showinfo("Insert a valid Address_ID")
    if count1>0 and count2>0:
        cursor.execute("Select COUNT(*) from Recipent where Recipient_ID=%s",(Recipient_ID,))
        count3=cursor.fetchone()[0]
        if count3>0:
           messagebox.showinfo("Recipient_ID already taken!")
        else:   
           query = "INSERT INTO Recipent(Recipient_ID,First_Name, Last_Name, Blood_ID, Address_ID, Phone_No) VALUES (%s, %s, %s, %s, %s,%s)"
           values = (Recipient_ID,First_Name, Last_Name, Blood_ID, Address_ID, Phone_No)
           cursor.execute(query, values)
           db.commit()
           messagebox.showinfo("Success", "Recipient inserted successfully")

# Update data in Recipient table
  def update_recipient():
    Recipient_ID = Recipient_ID_entry.get()
    new_First_Name = new_First_Name_entry.get()
    new_Last_Name = new_Last_Name_entry.get()
    new_Address_ID = new_Address_ID_entry.get()
    new_Phone_No=new_Phone_No.entry.get()
    cursor.execute("Select COUNT(*) from Recipent where Recipient_ID=%s",(Recipient_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
           messagebox.showinfo("Enter a valid Recipient_ID to update!")
    else:
           cursor.execute("Select COUNT(*) from Address where Address_ID=%s",(new_Address_ID,))
           count3=cursor.fetchone()[0]
           if count3==0:
             messagebox.showinfo("Enter a valid Address_ID!")
           else:
             query = "UPDATE Recipient SET First_Name = %s, Last_Name = %s,Address_ID=%s,Phone_No=%s WHERE Recipient_ID = %s"
             values = (new_First_Name, new_Last_Name,new_Address_ID,new_Phone_No,Recipient_ID)
             cursor.execute(query, values)
             db.commit()
             messagebox.showinfo("Success", "Recipient updated successfully")

# Delete data from Recipient table
  def delete_recipient():
    Recipient_ID = Recipient_ID_entry.get()

    query = "DELETE FROM Recipent WHERE Recipient_ID = %s"
    values = (Recipient_ID,)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Recipient deleted successfully")
    
    
  def display_recipient_details():
      cursor.execute("SELECT * FROM Recipent")
      Recipient_data = cursor.fetchall()
    
      result_text.delete(1.0, tk.END)  # Clear previous content
      for recipient in Recipient_data:
        result_text.insert(tk.END, f"ID: {recipient[0]}, First Name: {recipient[1]}, Last Name: {recipient[2]}, Blood ID: {recipient[3]}, Address ID: {recipient[4]},Phone No:{recipient[5]}\n")    
    
  def next():
      root.destroy()
         
  def previous():
        root.destroy()
        choice()
                      
# Create the GUI window
  root = tk.Tk()
  root.title("Recipient Management")

# Labels and Entry fields for Recipient
  Recipient_ID_label = tk.Label(root, text="Recipient ID:")
  First_Name_label = tk.Label(root, text="First Name:")
  Last_Name_label = tk.Label(root, text="Last Name:")
  Blood_ID_label = tk.Label(root, text="Blood ID:")
  Address_ID_label = tk.Label(root, text="Address ID:")
  Phone_No_label = tk.Label(root, text="Phone No:")
  Recipient_ID_entry = tk.Entry(root)
  First_Name_entry = tk.Entry(root)
  Last_Name_entry = tk.Entry(root)
  Blood_ID_entry = tk.Entry(root)
  Address_ID_entry = tk.Entry(root)
  Phone_No_entry = tk.Entry(root)
  new_First_Name_label = tk.Label(root, text="New First Name:")
  new_Last_Name_label = tk.Label(root, text="New Last Name:")
  new_Address_ID_label = tk.Label(root, text="New Address_ID:")
  new_Phone_No_label = tk.Label(root, text="New Phone_No:")
  new_First_Name_entry = tk.Entry(root)
  new_Last_Name_entry = tk.Entry(root)
  new_Address_ID_entry = tk.Entry(root)
  new_Phone_No_entry = tk.Entry(root)

# Buttons for Recipient
  insert_button = tk.Button(root, text="Insert Recipient", command=insert_recipient)
  update_button = tk.Button(root, text="Update Recipient", command=update_recipient)
  delete_button = tk.Button(root, text="Delete Recipient", command=delete_recipient)
  display_button =tk. Button(root, text="Display Recipient Details", command=display_recipient_details)
  result_text = tk.Text(root, wrap=tk.WORD,width=50, height=10)
  next_button=tk.Button(root,text="Next",command=next)
  previous_button=tk.Button(root,text="prev",command=previous)

# Grid layout for Recipient
  Recipient_ID_label.grid(row=0, column=0)
  Recipient_ID_entry.grid(row=0, column=1)
  First_Name_label.grid(row=1, column=0)
  First_Name_entry.grid(row=1, column=1)
  Last_Name_label.grid(row=2, column=0)
  Last_Name_entry.grid(row=2, column=1)
  Blood_ID_label.grid(row=3, column=0)
  Blood_ID_entry.grid(row=3, column=1)
  Address_ID_label.grid(row=4, column=0)
  Address_ID_entry.grid(row=4, column=1)
  Phone_No_label.grid(row=5, column=0)
  Phone_No_entry.grid(row=5, column=1)
  insert_button.grid(row=6, columnspan=2)
  new_First_Name_label.grid(row=7, column=0)
  new_First_Name_entry.grid(row=7, column=1)
  new_Last_Name_label.grid(row=8, column=0)
  new_Last_Name_entry.grid(row=8, column=1)
  new_Address_ID_label.grid(row=9,column=0)
  new_Address_ID_entry.grid(row=9,column=1)
  new_Phone_No_label.grid(row=10,column=0)
  new_Phone_No_entry.grid(row=10,column=1)
  update_button.grid(row=12, columnspan=2)
  delete_button.grid(row=13, columnspan=2)
  display_button.grid(row=14, columnspan=2)
  result_text.grid(row=15, column=0, padx=10, pady=10)
  previous_button.grid(row=16,column=0,columnspan=2)
  next_button.grid(row=16,column=1,columnspan=2)
    

# Main loop
  root.mainloop()
    
 
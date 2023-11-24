import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import font
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database
# Database connection
cursor = db.cursor() 



def option():
    root=tk.Tk() 
    root.configure(bg="#00296B")
    window_width=600
    window_height=400
    frame=tk.Frame(root,borderwidth=0.5,relief="solid",highlightthickness=0.5,highlightbackground="white",bg="white")
    frame.place(relx=0.5,rely=0.5,anchor="center")
    root.geometry(f"{window_width}x{window_height}")
    heading_label=tk.Label(root,text="MENU",font=("Comic Sans MS",12,"bold"),bg="#00296B",fg="WHITE")
    heading_label.pack(pady=20)
    a_button=tk.Button(frame,text="Address ",command=address,fg="white",bg="blue")
    b_button=tk.Button(frame,text="BloodType",command=blood_type,fg="white",bg="blue")
    d_button=tk.Button(frame,text="Donor",command=donor,fg="white",bg="blue")
    r_button=tk.Button(frame,text="Recipient ",command=recipient,fg="white",bg="blue")
    g_button=tk.Button(frame,text="Gives_To ",command=gives_to,fg="white",bg="blue")
    t_button=tk.Button(frame,text="Takes_from ",command=takes_from,fg="white",bg="blue")
 
    a_button.grid(row=1,column=2,padx=10,pady=10)
    b_button.grid(row=2,column=2,padx=10,pady=10)
    d_button.grid(row=3,column=2,padx=10,pady=10)
    r_button.grid(row=4,column=2,padx=10,pady=10)
    g_button.grid(row=5,column=2,padx=10,pady=10)
    t_button.grid(row=6,column=2,padx=10,pady=10)
   
    root.mainloop()
    
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
           query = "INSERT INTO Address (Address_ID,City,District,Neighborhood) VALUES (%s,%s,%s,%s)"
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
           
   def display_address():
      query = "SELECT * FROM Address"
      cursor.execute(query)
      results = cursor.fetchall()

      display_text.delete(1.0, tk.END)  # Clear the current text
      for result in results:
        display_text.insert(tk.END, f"Adress_ID: {result[0]}\n")
        display_text.insert(tk.END, f"City: {result[1]}\n")
        display_text.insert(tk.END, f"District: {result[2]}\n")
        display_text.insert(tk.END, f"Neighbhorood: {result[3]}\n\n")
        
   def next():
       root.destroy()        
           
   
    
    

# Create the GUI window
   root = tk.Tk()
   root.title("Address Management")
   window_width=600
   window_height=600
   heading_label=tk.Label(root,text="ADDRESS",font=("Serif",15,"bold"),bg="#00296B",fg="WHITE")
   heading_label.pack(pady=20)
   root.geometry(f"{window_width}x{window_height}")
   root.configure(bg="#00296B")
   frame=tk.Frame(root,borderwidth=1,relief="solid",highlightthickness=0.5,highlightbackground="white",bg="#C0C0C0")
   frame.place(relx=0.5,rely=0.5,anchor="center")
  

# Labels and Entry fields for Address
   Address_ID_label = tk.Label(frame, text="Address ID:",bg="#C0C0C0")
   City_label = tk.Label(frame, text="City:",bg="#C0C0C0")
   District_label = tk.Label(frame, text="District:",bg="#C0C0C0")
   Neighborhood_label = tk.Label(frame, text="Neighborhood:",bg="#C0C0C0")
   Address_ID_entry = tk.Entry(frame)
   City_entry = tk.Entry(frame)
   District_entry=tk.Entry(frame)
   Neighborhood_entry = tk.Entry(frame)
   new_City_label = tk.Label(frame, text="New City:",bg="#C0C0C0")
   new_District_label = tk.Label(frame, text="New District:",bg="#C0C0C0")
   new_Neighborhood_label = tk.Label(frame, text="New Neighborhood:",bg="#C0C0C0")
   new_City_entry = tk.Entry(frame)
   new_District_entry=tk.Entry(frame)
   new_Neighborhood_entry = tk.Entry(frame)

# Buttons for Address
   insert_button = tk.Button(frame, text="Insert Address", command=insert_address)
   update_button = tk.Button(frame, text="Update Address", command=update_address)
   delete_button = tk.Button(frame, text="Delete Address", command=delete_address)
   display_button = tk.Button(frame, text="Display Address", command=display_address)
   display_text = tk.Text(frame, height=10, width=40)
   next_button=tk.Button(frame,text="Next",command=next)
  

# Grid layout for Address
   Address_ID_label.grid(row=0,column=0)
   Address_ID_entry.grid(row=0,column=1)
   City_label.grid(row=1,column=0)
   City_entry.grid(row=1,column=1)
   District_label.grid(row=2,column=0)
   District_entry.grid(row=2,column=1)
   Neighborhood_label.grid(row=3,column=0)
   Neighborhood_entry.grid(row=3,column=1)
   insert_button.grid(row=4,column=1)
   new_City_label.grid(row=5,column=0)
   new_City_entry.grid(row=5,column=1)
   new_District_label.grid(row=6,column=0)
   new_District_entry.grid(row=6,column=1)
   new_Neighborhood_label.grid(row=7,column=0)
   new_Neighborhood_entry.grid(row=7,column=1)
   update_button.grid(row=8,column=1)
   delete_button.grid(row=9,column=1)
   display_button.grid()
   display_text.grid()
   next_button.grid(row=10,column=1)
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
 
                    

   # Create the GUI window
   root = tk.Tk()
   root.title("Blood Type Display")
   root.config(bg="#00296B")
   window_width=600
   window_height=400
   frame=tk.Frame(root,borderwidth=1,relief="solid",highlightthickness=0.5,highlightbackground="white",bg="#C0C0C0")
   frame.place(relx=0.5,rely=0.5,anchor="center")
   root.geometry(f"{window_width}x{window_height}")
   
   # Button for displaying Blood_Type
   display_button = tk.Button(frame, text="Display Blood Type", command=display_blood_type)
   done_button=tk.Button(frame,text="Next",command=next)
  #  previous_button=tk.Button(root,text="Prev",command=previous)

   # Text widget to display results
   display_text = tk.Text(frame, height=20, width=40)


   # Grid layout
   display_button.grid()
   display_text.grid()
  #  previous_button.grid(row=2,column=0,columnspan=3)
   done_button.grid()
   
   

# Main loop
   root.mainloop()





def donor():
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

      
    # def previous():
    #     root.destroy()
                      
      
        
      
   # Create the GUI window
    root = tk.Tk()
    root.title("Donor Management")
    root.config(bg="#00296B")
    window_width=600
    window_height=600
    frame=tk.Frame(root,borderwidth=1,relief="solid",highlightthickness=0.5,highlightbackground="white",bg="#C0C0C0")
    frame.place(relx=0.5,rely=0.5,anchor="center")
    root.geometry(f"{window_width}x{window_height}")

# Labels and Entry fields for Donor
    Donor_ID_label = tk.Label(frame, text="Donor ID:",bg="#C0C0C0")
    First_Name_label = tk.Label(frame, text="First Name:",bg="#C0C0C0")
    Last_Name_label = tk.Label(frame, text="Last Name:",bg="#C0C0C0")
    Blood_ID_label = tk.Label(frame, text="Blood ID:",bg="#C0C0C0")
    Address_ID_label = tk.Label(frame, text="Address ID:",bg="#C0C0C0")
    Donor_ID_entry = tk.Entry(frame)
    First_Name_entry = tk.Entry(frame)
    Last_Name_entry = tk.Entry(frame)
    Blood_ID_entry = tk.Entry(frame)
    Address_ID_entry = tk.Entry(frame)
    new_First_Name_label = tk.Label(frame, text="New First Name:",bg="#C0C0C0")
    new_Last_Name_label = tk.Label(frame, text="New Last Name:",bg="#C0C0C0")
    new_First_Name_label = tk.Label(frame, text="New First Name:",bg="#C0C0C0")
    new_Address_ID_label = tk.Label(frame, text="New Address_ID:",bg="#C0C0C0")
    new_First_Name_entry = tk.Entry(frame)
    new_Last_Name_entry = tk.Entry(frame)
    new_Address_ID_entry = tk.Entry(frame)

# Buttons for Donor
    insert_button = tk.Button(frame, text="Insert Donor", command=insert_donor)
    update_button = tk.Button(frame, text="Update Donor", command=update_donor)
    delete_button = tk.Button(frame, text="Delete Donor", command=delete_donor)
    display_button =tk. Button(frame, text="Display Donor Details", command=display_donor_details)
    result_text = tk.Text(frame, wrap=tk.WORD,width=50, height=10)
    done_button=tk.Button(frame,text="Next",command=next)
    # previous_button=tk.Button(root,text="prev",command=previous)

# Grid layout for Donor
    Donor_ID_label.grid(row=0,column=0)
    Donor_ID_entry.grid(row=0,column=1)
    First_Name_label.grid(row=1,column=0)
    First_Name_entry.grid(row=1,column=1)
    Last_Name_label.grid(row=2,column=0)
    Last_Name_entry.grid(row=2,column=1)
    Blood_ID_label.grid(row=3,column=0)
    Blood_ID_entry.grid(row=3,column=1)
    Address_ID_label.grid(row=4,column=0)
    Address_ID_entry.grid(row=4,column=1)
    insert_button.grid(row=5,column=1,columnspan=3)
    new_First_Name_label.grid(row=6,column=0)
    new_First_Name_entry.grid(row=6,column=1)
    new_Last_Name_label.grid(row=7,column=0)
    new_Last_Name_entry.grid(row=7,column=1)
    new_Address_ID_label.grid(row=8,column=0)
    new_Address_ID_entry.grid(row=8,column=1)
    update_button.grid(row=9,column=1)
    delete_button.grid(row=10,column=1)
    display_button.grid(row=11,column=1,columnspan=3)
    result_text.grid(row=12)
    # previous_button.grid(row=14,column=0,columnspan=1)
    done_button.grid(row=13,column=1)
    

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
  
                      
# Create the GUI window
  root = tk.Tk()
  root.title("Recipient Management")
  window_width=600
  window_height=600
  root.config(bg="#00296B")
  frame=tk.Frame(root,borderwidth=0.5,relief="solid",highlightthickness=0.5,highlightbackground="white",bg="#C0C0C0")
  frame.place(relx=0.5,rely=0.5,anchor="center")
  root.geometry(f"{window_width}x{window_height}")

# Labels and Entry fields for Recipient
  Recipient_ID_label = tk.Label(frame, text="Recipient ID:",bg="#C0C0C0")
  First_Name_label = tk.Label(frame, text="First Name:",bg="#C0C0C0")
  Last_Name_label = tk.Label(frame, text="Last Name:",bg="#C0C0C0")
  Blood_ID_label = tk.Label(frame, text="Blood ID:",bg="#C0C0C0")
  Address_ID_label = tk.Label(frame, text="Address ID:",bg="#C0C0C0")
  Phone_No_label = tk.Label(frame, text="Phone No:",bg="#C0C0C0")
  Recipient_ID_entry = tk.Entry(frame)
  First_Name_entry = tk.Entry(frame)
  Last_Name_entry = tk.Entry(frame)
  Blood_ID_entry = tk.Entry(frame)
  Address_ID_entry = tk.Entry(frame)
  Phone_No_entry = tk.Entry(frame)
  new_First_Name_label = tk.Label(frame, text="New First Name:",bg="#C0C0C0")
  new_Last_Name_label = tk.Label(frame, text="New Last Name:",bg="#C0C0C0")
  new_Address_ID_label = tk.Label(frame, text="New Address_ID:",bg="#C0C0C0")
  new_Phone_No_label = tk.Label(frame, text="New Phone_No:",bg="#C0C0C0")
  new_First_Name_entry = tk.Entry(frame)
  new_Last_Name_entry = tk.Entry(frame)
  new_Address_ID_entry = tk.Entry(frame)
  new_Phone_No_entry = tk.Entry(frame)

# Buttons for Recipient
  insert_button = tk.Button(frame, text="Insert Recipient", command=insert_recipient)
  update_button = tk.Button(frame, text="Update Recipient", command=update_recipient)
  delete_button = tk.Button(frame, text="Delete Recipient", command=delete_recipient)
  display_button =tk. Button(frame, text="Display Recipient Details", command=display_recipient_details)
  result_text = tk.Text(frame, wrap=tk.WORD,width=50, height=10)
  next_button=tk.Button(frame,text="Next",command=next)
  # previous_button=tk.Button(root,text="prev",command=previous)

# Grid layout for Recipient
  Recipient_ID_label.grid(row=0,column=0)
  Recipient_ID_entry.grid(row=0,column=1)
  First_Name_label.grid(row=1,column=0)
  First_Name_entry.grid(row=1,column=1)
  Last_Name_label.grid(row=2,column=0)
  Last_Name_entry.grid(row=2,column=1)
  Blood_ID_label.grid(row=3,column=0)
  Blood_ID_entry.grid(row=3,column=1)
  Address_ID_label.grid(row=4,column=0)
  Address_ID_entry.grid(row=4,column=1)
  Phone_No_label.grid(row=5,column=0)
  Phone_No_entry.grid(row=5,column=1)
  insert_button.grid(row=6,column=1)
  new_First_Name_label.grid(row=7,column=0)
  new_First_Name_entry.grid(row=7,column=1)
  new_Last_Name_label.grid(row=8,column=0)
  new_Last_Name_entry.grid(row=8,column=1)
  new_Address_ID_label.grid(row=9,column=0)
  new_Address_ID_entry.grid(row=9,column=1)
  new_Phone_No_label.grid(row=10,column=0)
  new_Phone_No_entry.grid(row=10,column=1)
  update_button.grid(row=11,column=1)
  delete_button.grid(row=12,column=1)
  display_button.grid(row=13,column=1)
  result_text.grid(row=14,column=1)
  # previous_button.grid(row=16,column=0,columnspan=2)
  next_button.grid(row=15,column=1)
    

# Main loop
  root.mainloop()
  
def blood_bank(): 
# Insert data into Blood_bank table
  def insert_blood_bank():
    Bank_ID = Bank_ID_entry.get()
    Name = Name_entry.get()
    Capacity = Capacity_entry.get()
    cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
    count1=cursor.fetchone()[0]
    if count1>0:
       messagebox.show("Bank_ID already taken:")
    else: 
      query = "INSERT INTO Blood_Bank (Bank_ID, Name, Capacity) VALUES (%s, %s, %s)"
      values = (Bank_ID, Name, Capacity)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Blood bank inserted successfully")

# Delete data from Blood_bank table
  def delete_blood_bank():
    Bank_ID = Bank_ID_entry.get()
    cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
    count2=cursor.fetchone()[0]
    if count2==0:
      messagebox.showinfo("Enter a valid Bank_ID")
    else: 
      query = "DELETE FROM Blood_Bank WHERE Bank_ID = %s"
      values = (Bank_ID,)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Blood bank deleted successfully")

# Display data from Blood_bank table
  def display_blood_banks():
    query = "SELECT * FROM Blood_bank"
    cursor.execute(query)
    results = cursor.fetchall()
    
    display_text.delete("1.0", tk.END)
    for result in results:
        display_text.insert(tk.END, f"Bank_ID: {result[0]}\nName: {result[1]}\nCapacity: {result[2]}\n\n")

# Update data in Blood_bank table
  def update_blood_bank():
    Bank_ID = Bank_ID_entry.get()
    new_Name = new_Name_entry.get()
    new_Capacity = new_Capacity_entry.get()
    cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
    count3=cursor.fetchone()[0]
    if count3==0:
      messagebox.showinfo("Enter a valid Bank_ID")
    else: 
      query = "UPDATE Blood_Bank SET Name = %s, Capacity = %s WHERE Bank_ID = %s"
      values = (new_Name, new_Capacity, Bank_ID)
      cursor.execute(query, values)
      db.commit()
   
      messagebox.showinfo("Success", "Blood bank updated successfully")
    
  def next():
      root.destroy()
  #     gives_to()
         
  # def previous():
  #       root.destroy()
  #       blood_bank()

# Create the GUI window
  root = tk.Tk()
  root.title("Blood Bank Management")
  root.config(bg="#00296B")
  window_width=600
  window_height=600
  frame=tk.Frame(root)
  frame.place(relx=0.5,rely=0.5,anchor="center")
  root.geometry(f"{window_width}x{window_height}")
  

# Labels and Entry fields for Blood_bank
  Bank_ID_label = tk.Label(frame, text="Bank ID:",bg="#C0C0C0")
  Name_label = tk.Label(frame, text="Name:")
  Capacity_label = tk.Label(frame, text="Capacity:",bg="#C0C0C0")
  Bank_ID_entry = tk.Entry(frame)
  Name_entry = tk.Entry(frame)
  Capacity_entry = tk.Entry(frame)

# Buttons for Blood_bank
  insert_button = tk.Button(frame, text="Insert Blood Bank", command=insert_blood_bank)
  delete_button = tk.Button(frame, text="Delete Blood Bank", command=delete_blood_bank)
  display_button = tk.Button(frame, text="Display Blood Banks", command=display_blood_banks)
  next_button=tk.Button(frame,text="Next",command=next)
  # previous_button=tk.Button(root,text="prev",command=previous)

# Labels and Entry fields for updating
  new_Name_label = tk.Label(frame, text="New Name:")
  new_Capacity_label = tk.Label(frame, text="New Capacity:")
  new_Name_entry = tk.Entry(frame)
  new_Capacity_entry = tk.Entry(frame)
  update_button = tk.Button(frame, text="Update Blood Bank", command=update_blood_bank)

# Display area
  display_text = tk.Text(frame, height=10, width=40)

# Grid layout for Blood_bank
  Bank_ID_label.grid(row=0,column=0)
  Bank_ID_entry.grid(row=0,column=1)
  Name_label.grid(row=1,column=0)
  Name_entry.grid(row=1,column=1)
  Capacity_label.grid(row=2,column=0)
  Capacity_entry.grid(row=2,column=1)
  insert_button.grid(row=3,column=1)
  delete_button.grid(row=4,column=1)
  display_button.pack(row=5,column=1)
  

# Grid layout for updating
  new_Name_label.grid(row=6,column=0)
  new_Name_entry.grid(row=6,column=1)
  new_Capacity_label.grid(row=7,column=0)
  new_Capacity_entry.grid(row=7,column=1)
  update_button.grid(row=8,column=1)

# Display area
  display_text.grid(row=9,column=1)
  # previous_button.grid(row=10,column=0,columnspan=2)
  next_button.grid(row=10,column=1)

# Main loop
  root.mainloop()
  
def gives_to():
  # Insert data into gives_to table
  def insert_gives_to():
    Donation_ID = int(Donation_ID_entry.get())
    Donor_ID = int(Donor_ID_entry.get())
    Bank_ID= int(Bank_ID_entry.get())
    Amount = float(Amount_entry.get())
    cursor.execute("Select COUNT(*) from Gives_To where Donation_ID=%s",(Donation_ID,))
    count1=cursor.fetchone()[0]
    if count1>0:
      messagebox.showinfo("Donation_ID already taken")
    else:
      cursor.execute("Select COUNT(*) from Donor where Donor_ID=%s",(Donor_ID,))
      count2=cursor.fetchone()[0]
      if count2==0:
        messagebox.showinfo("Enter a valid Donor_ID")   
      cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
      count3=cursor.fetchone()[0]
      if count3==0:
       messagebox.showinfo("Enter a valid Bank_ID")
      if count2>0 and count3>0: 
        query = "INSERT INTO gives_to (Donation_ID, Donor_ID, Bank_ID, amount) VALUES (%s, %s, %s, %s)"
        values = (Donation_ID, Donor_ID, Bank_ID, Amount)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully")

# Delete data from gives_to table
  def delete_gives_to():
    Donation_ID = int(Donation_ID_entry.get())
    cursor.execute("Select COUNT(*) from Gives_To where Donation_ID=%s",(Donation_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Donation_ID")
    else:  
      query = "DELETE FROM gives_to WHERE Donation_ID = %s"
      values = (Donation_ID,)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Data deleted successfully")

# Display data from gives_to table
  def display_gives_to():
    query = "SELECT * FROM gives_to"
    cursor.execute(query)
    results = cursor.fetchall()
    display_text.config(state=tk.NORMAL)
    display_text.delete(1.0, tk.END)
    for result in results:
        display_text.insert(tk.END, f"Donation ID: {result[0]}, Donor ID: {result[1]}, Bank ID: {result[2]}, Amount: {result[3]}\n")
    display_text.config(state=tk.DISABLED)

# Update data in gives_to table
  def update_gives_to():
    Donation_ID = int(Donation_ID_entry.get())
    Donor_ID = int(Donor_ID_entry.get())
    Bank_ID= int(Bank_ID_entry.get())
    new_Amount = float(new_Amount_entry.get())
    cursor.execute("Select COUNT(*) from Gives_To where Donation_ID=%s",(Donation_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Donation_ID")
    else:  
      query = "UPDATE gives_to SET amount = %s WHERE Donation_ID = %s"
      values = (new_Amount, Donation_ID)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Data updated successfully")
   
  def next():
      root.destroy()
  #     takes_from()
         
  # def previous():
  #       root.destroy()
  #       gives_to()    
  
# Create the GUI window
  root = tk.Tk()
  root.title("gives_to Management")

# Labels and Entry fields for gives_to
  Donation_ID_label = tk.Label(root, text="Donation ID:")
  Donor_ID_label = tk.Label(root, text="Donor ID:")
  Bank_ID_label = tk.Label(root, text="Bank ID:")
  Amount_label = tk.Label(root, text="Amount:")
  new_Amount_label = tk.Label(root, text="New Amount (for update):")
  Donation_ID_entry = tk.Entry(root)
  Donor_ID_entry = tk.Entry(root)
  Bank_ID_entry = tk.Entry(root)
  Amount_entry = tk.Entry(root)
  new_Amount_entry = tk.Entry(root)

# Buttons for gives_to
  insert_button = tk.Button(root, text="Insert Data", command=insert_gives_to)
  delete_button = tk.Button(root, text="Delete Data", command=delete_gives_to)
  display_button = tk.Button(root, text="Display Data", command=display_gives_to)
  update_button = tk.Button(root, text="Update Data", command=update_gives_to)
  next_button=tk.Button(root,text="Next",command=next)
  # previous_button=tk.Button(root,text="prev",command=previous)
# Text widget for display
  display_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)

# Grid layout for gives_to
  Donation_ID_label.pack()
  Donation_ID_entry.pack()
  Donor_ID_label.pack()
  Donor_ID_entry.pack()
  Bank_ID_label.pack()
  Bank_ID_entry.pack()
  Amount_label.pack()
  Amount_entry.pack()
  new_Amount_label.pack()
  new_Amount_entry.pack()
  insert_button.pack()
  delete_button.pack()
  display_button.pack()
  update_button.pack()
  display_text.pack()
  # previous_button.grid(row=10,column=0,columnspan=2)
  next_button.pack()

# Main loop
  root.mainloop()

  
    
def takes_from():
   # Insert data into Takes_from table
  def insert_takes_from():
    Transfer_ID = Transfer_ID_entry.get()
    Recipient_ID = Recipient_ID_entry.get()
    Bank_ID= Bank_ID_entry.get()
    Amount = Amount_entry.get()
    cursor.execute("Select COUNT(*) from Takes_from where Transfer_ID=%s",(Transfer_ID,))
    count1=cursor.fetchone()[0]
    if count1>0:
      messagebox.showinfo("Transfer_ID already taken")
    else:
      cursor.execute("Select COUNT(*) from Recipent where Recipient_ID=%s",(Recipient_ID,))
      count2=cursor.fetchone()[0]
      if count2==0:
        messagebox.showinfo("Enter a valid Recipient_ID")   
      cursor.execute("Select COUNT(*) from Blood_Bank where Bank_ID=%s",(Bank_ID,))
      count3=cursor.fetchone()[0]
      if count3==0:
       messagebox.showinfo("Enter a valid Bank_ID")
      if count2>0 and count3>0: 
        query = "INSERT INTO Takes_from (Transfer_id, Recipient_ID, Bank_ID, amount) VALUES (%s, %s, %s, %s)"
        values = (Transfer_ID, Recipient_ID, Bank_ID, Amount)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Record inserted successfully")

# Delete data from Takes_from table
  def delete_takes_from():
    Transfer_ID = Transfer_ID_entry.get()
    cursor.execute("Select COUNT(*) from Takes_from where Transfer_ID=%s",(Transfer_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Transfer_ID")
    else:  
      query = "DELETE FROM Takes_from WHERE Transfer_ID = %s"
      values = (Transfer_ID,)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Record deleted successfully")

# Display data from Takes_from table
  def display_takes_from():
    query = "SELECT * FROM Takes_From"
    cursor.execute(query)
    records = cursor.fetchall()
    display_text.config(state=tk.NORMAL)
    display_text.delete("1.0", tk.END)
    for record in records:
        display_text.insert(tk.END, f"Transfer ID: {record[0]}, Recipient ID: {record[1]}, Bank ID: {record[2]}, Amount: {record[3]}\n")
    display_text.config(state=tk.DISABLED)

# Update data in Takes_from table
  def update_takes_from():
    Transfer_ID = Transfer_ID_entry.get()
    Recipient_ID = Recipient_ID_entry.get()
    Bank_ID = Bank_ID_entry.get()
    new_Amount = new_Amount_entry.get()
    cursor.execute("Select COUNT(*) from Gives_To where Transfer_ID=%s",(Transfer_ID,))
    count1=cursor.fetchone()[0]
    if count1==0:
      messagebox.showinfo("Enter a valid Donation_ID")
    else:  
      query = "UPDATE Takes_from SET amount = %s WHERE transfer_id = %s"
      values = (new_Amount, Transfer_ID)
      cursor.execute(query, values)
      db.commit()
      messagebox.showinfo("Success", "Record updated successfully")
      
  def next():
     root.destroy() 

# Create the GUI window
  root = tk.Tk()
  root.title("Takes_from Management")

# Labels and Entry fields for Takes_from
  Transfer_ID_label = tk.Label(root, text="Transfer ID:")
  Recipient_ID_label = tk.Label(root, text="Recipient ID:")
  Bank_ID_label = tk.Label(root, text="Bank ID:")
  Amount_label = tk.Label(root, text="Amount:")
  Transfer_ID_entry = tk.Entry(root)
  Recipient_ID_entry = tk.Entry(root)
  Bank_ID_entry = tk.Entry(root)
  Amount_entry = tk.Entry(root)
  new_Amount_label = tk.Label(root, text="New Amount:")
  new_Amount_entry = tk.Entry(root)

# Buttons for Takes_from
  insert_button = tk.Button(root, text="Insert", command=insert_takes_from)
  delete_button = tk.Button(root, text="Delete", command=delete_takes_from)
  display_button = tk.Button(root, text="Display", command=display_takes_from)
  update_button = tk.Button(root, text="Update", command=update_takes_from)
  next_button=tk.Button(root,text="Next",command=next)

# Text widget to display records
  display_text = tk.Text(root, height=10, width=50)
  display_text.config(state=tk.DISABLED)

# Grid layout for Takes_from
  Transfer_ID_label.pack()
  Transfer_ID_entry.pack()
  Recipient_ID_label.pack()
  Recipient_ID_entry.pack()
  Bank_ID_label.pack()
  Bank_ID_entry.pack()
  Amount_label.pack()
  Amount_entry.pack()
  new_Amount_label.pack()
  new_Amount_entry.pack()
  insert_button.pack()
  delete_button.pack()
  display_button.pack()
  update_button.pack()
  display_text.pack()
  next_button.pack()

# Main loop
  root.mainloop()
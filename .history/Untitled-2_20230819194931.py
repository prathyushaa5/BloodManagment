
# Insert data into Donor table
def insert_donor():
    
    Donor_ID = Donor_ID_entry.get()
    First_Name = First_Name_entry.get()
    Last_Name = Last_Name_entry.get()
    Blood_ID = Blood_ID_entry.get()
    Address_ID= Address_ID_entry.get()

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
    messagebox.showinfo("Success", "Donor updated successfully")

# Delete data from Donor table
def delete_donor():
    Donor_ID= Donor_ID_entry.get()

    query = "DELETE FROM Donor WHERE Donor_ID = %s"
    values = (Donor_ID,)
    cursor.execute(query, values)
    db.commit()
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

# # Insert data into Blood_Bank table
# def insert_blood_bank():
#     name = name_entry.get()
#     capacity = capacity_entry.get()

#     query = "INSERT INTO Blood_Bank (Name, Capacity) VALUES (%s, %s)"
#     values = (name, capacity)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Blood bank inserted successfully")

# # Update data in Blood_Bank table
# def update_blood_bank():
#     bank_id = bank_id_entry.get()
#     new_name = new_name_entry.get()
#     new_capacity = new_capacity_entry.get()

#     query = "UPDATE Blood_Bank SET Name = %s, Capacity = %s WHERE Bank_ID = %s"
#     values = (new_name, new_capacity, bank_id)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Blood bank updated successfully")

# # Delete data from Blood_Bank table
# def delete_blood_bank():
#     bank_id = bank_id_entry.get()

#     query = "DELETE FROM Blood_Bank WHERE Bank_ID = %s"
#     values = (bank_id,)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Blood bank deleted successfully")

# # Create the GUI window
# root = tk.Tk()
# root.title("Blood Bank Management")

# # Labels and Entry fields for Blood_Bank
# bank_id_label = tk.Label(root, text="Bank ID:")
# name_label = tk.Label(root, text="Name:")
# capacity_label = tk.Label(root, text="Capacity:")
# bank_id_entry = tk.Entry(root)
# name_entry = tk.Entry(root)
# capacity_entry = tk.Entry(root)
# new_name_label = tk.Label(root, text="New Name:")
# new_capacity_label = tk.Label(root, text="New Capacity:")
# new_name_entry = tk.Entry(root)
# new_capacity_entry = tk.Entry(root)

# # Buttons for Blood_Bank
# insert_button = tk.Button(root, text="Insert Blood Bank", command=insert_blood_bank)
# update_button = tk.Button(root, text="Update Blood Bank", command=update_blood_bank)
# delete_button = tk.Button(root, text="Delete Blood Bank", command=delete_blood_bank)

# # Grid layout for Blood_Bank
# bank_id_label.grid(row=0, column=0)
# bank_id_entry.grid(row=0, column=1)
# name_label.grid(row=1, column=0)
# name_entry.grid(row=1, column=1)
# capacity_label.grid(row=2, column=0)
# capacity_entry.grid(row=2, column=1)
# insert_button.grid(row=3, columnspan=2)
# new_name_label.grid(row=4, column=0)
# new_name_entry.grid(row=4, column=1)
# new_capacity_label.grid(row=5, column=0)
# new_capacity_entry.grid(row=5, column=1)
# update_button.grid(row=6, columnspan=2)
# delete_button.grid(row=7, columnspan=2)

# # Main loop
# root.mainloop()
# # Insert data into Gives_To table
# # Insert data into Recipient table
# def insert_recipient():
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     blood_id = blood_id_entry.get()
#     address_id = address_id_entry.get()
#     phone_no = phone_no_entry.get()

#     query = "INSERT INTO Recipient (First_Name, Last_Name, Blood_ID, Address_ID, Phone_No) VALUES (%s, %s, %s, %s, %s)"
#     values = (first_name, last_name, blood_id, address_id, phone_no)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Recipient inserted successfully")

# # Update data in Recipient table
# def update_recipient():
#     recipient_id = recipient_id_entry.get()
#     new_first_name = new_first_name_entry.get()
#     new_last_name = new_last_name_entry.get()

#     query = "UPDATE Recipient SET First_Name = %s, Last_Name = %s WHERE Recipient_ID = %s"
#     values = (new_first_name, new_last_name, recipient_id)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Recipient updated successfully")

# # Delete data from Recipient table
# def delete_recipient():
#     recipient_id = recipient_id_entry.get()

#     query = "DELETE FROM Recipient WHERE Recipient_ID = %s"
#     values = (recipient_id,)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Recipient deleted successfully")

# # Create the GUI window
# root = tk.Tk()
# root.title("Recipient Management")

# # Labels and Entry fields for Recipient
# recipient_id_label = tk.Label(root, text="Recipient ID:")
# first_name_label = tk.Label(root, text="First Name:")
# last_name_label = tk.Label(root, text="Last Name:")
# blood_id_label = tk.Label(root, text="Blood ID:")
# address_id_label = tk.Label(root, text="Address ID:")
# phone_no_label = tk.Label(root, text="Phone No:")
# recipient_id_entry = tk.Entry(root)
# first_name_entry = tk.Entry(root)
# last_name_entry = tk.Entry(root)
# blood_id_entry = tk.Entry(root)
# address_id_entry = tk.Entry(root)
# phone_no_entry = tk.Entry(root)
# new_first_name_label = tk.Label(root, text="New First Name:")
# new_last_name_label = tk.Label(root, text="New Last Name:")
# new_first_name_entry = tk.Entry(root)
# new_last_name_entry = tk.Entry(root)

# # Buttons for Recipient
# insert_button = tk.Button(root, text="Insert Recipient", command=insert_recipient)
# update_button = tk.Button(root, text="Update Recipient", command=update_recipient)
# delete_button = tk.Button(root, text="Delete Recipient", command=delete_recipient)

# # Grid layout for Recipient
# recipient_id_label.grid(row=0, column=0)
# recipient_id_entry.grid(row=0, column=1)
# first_name_label.grid(row=1, column=0)
# first_name_entry.grid(row=1, column=1)
# last_name_label.grid(row=2, column=0)
# last_name_entry.grid(row=2, column=1)
# blood_id_label.grid(row=3, column=0)
# blood_id_entry.grid(row=3, column=1)
# address_id_label.grid(row=4, column=0)
# address_id_entry.grid(row=4, column=1)
# phone_no_label.grid(row=5, column=0)
# phone_no_entry.grid(row=5, column=1)
# insert_button.grid(row=6, columnspan=2)
# new_first_name_label.grid(row=7, column=0)
# new_first_name_entry.grid(row=7, column=1)
# new_last_name_label.grid(row=8, column=0)
# new_last_name_entry.grid(row=8, column=1)
# update_button.grid(row=9, columnspan=2)
# delete_button.grid(row=10, columnspan=2)

# # Main loop
# root.mainloop()
# def insert_gives_to():
#     donor_id = donor_id_entry.get()
#     bank_id = bank_id_entry.get()
#     amount = amount_entry.get()

#     query = "INSERT INTO Gives_To (Donor_ID, Bank_ID, Amount) VALUES (%s, %s, %s)"
#     values = (donor_id, bank_id, amount)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Donation inserted successfully")

# # Delete data from Gives_To table
# def delete_gives_to():
#     donation_id = donation_id_entry.get()

#     query = "DELETE FROM Gives_To WHERE Donation_ID = %s"
#     values = (donation_id,)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Donation deleted successfully")

# # Update data in Gives_To table
# def update_gives_to():
#     donation_id = donation_id_entry.get()
#     new_amount = new_amount_entry.get()

#     query = "UPDATE Gives_To SET Amount = %s WHERE Donation_ID = %s"
#     values = (new_amount, donation_id)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Donation updated successfully")

# # Display data from Gives_To table
# def display_gives_to():
#     query = "SELECT * FROM Gives_To"
#     cursor.execute(query)
#     results = cursor.fetchall()

#     result_text.delete("1.0", tk.END)
#     for row in results:
#         result_text.insert(tk.END, f"Donation ID: {row[0]}, Donor ID: {row[1]}, Bank ID: {row[2]}, Amount: {row[3]}\n")

# # Create the GUI window
# root = tk.Tk()
# root.title("Donation Management")

# # Labels and Entry fields for Donation
# donation_id_label = tk.Label(root, text="Donation ID:")
# donor_id_label = tk.Label(root, text="Donor ID:")
# bank_id_label = tk.Label(root, text="Bank ID:")
# amount_label = tk.Label(root, text="Amount:")
# donation_id_entry = tk.Entry(root)
# donor_id_entry = tk.Entry(root)
# bank_id_entry = tk.Entry(root)
# amount_entry = tk.Entry(root)
# new_amount_label = tk.Label(root, text="New Amount:")
# new_amount_entry = tk.Entry(root)

# # Buttons for Donation
# insert_button = tk.Button(root, text="Insert Donation", command=insert_gives_to)
# delete_button = tk.Button(root, text="Delete Donation", command=delete_gives_to)
# update_button = tk.Button(root, text="Update Donation", command=update_gives_to)
# display_button = tk.Button(root, text="Display Donations", command=display_gives_to)

# # Text widget to display results
# result_text = tk.Text(root, height=10, width=50)

# # Grid layout for Donation
# donation_id_label.grid(row=0, column=0)
# donation_id_entry.grid(row=0, column=1)
# donor_id_label.grid(row=1, column=0)
# donor_id_entry.grid(row=1, column=1)
# bank_id_label.grid(row=2, column=0)
# bank_id_entry.grid(row=2, column=1)
# amount_label.grid(row=3, column=0)
# amount_entry.grid(row=3, column=1)
# insert_button.grid(row=4, columnspan=2)
# delete_button.grid(row=5, columnspan=2)
# new_amount_label.grid(row=6, column=0)
# new_amount_entry.grid(row=6, column=1)
# update_button.grid(row=7, columnspan=2)
# display_button.grid(row=8, columnspan=2)
# result_text.grid(row=9, columnspan=2)

# # Main loop
# root.mainloop()

# # Insert data into Takes_from table
# def insert_takes_from():
#     recipient_id = recipient_id_entry.get()
#     bank_id = bank_id_entry.get()
#     amount = amount_entry.get()

#     query = "INSERT INTO Takes_from (Recipient_ID, Bank_ID, Amount) VALUES (%s, %s, %s)"
#     values = (recipient_id, bank_id, amount)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Transfer inserted successfully")

# # Update data in Takes_from table
# def update_takes_from():
#     transfer_id = transfer_id_entry.get()
#     new_amount = new_amount_entry.get()

#     query = "UPDATE Takes_from SET Amount = %s WHERE Transfer_ID = %s"
#     values = (new_amount, transfer_id)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Transfer updated successfully")

# # Delete data from Takes_from table
# def delete_takes_from():
#     transfer_id = transfer_id_entry.get()

#     query = "DELETE FROM Takes_from WHERE Transfer_ID = %s"
#     values = (transfer_id,)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Transfer deleted successfully")

# # Create the GUI window
# root = tk.Tk()
# root.title("Transfer Management")

# # Labels and Entry fields for Takes_from
# transfer_id_label = tk.Label(root, text="Transfer ID:")
# recipient_id_label = tk.Label(root, text="Recipient ID:")
# bank_id_label = tk.Label(root, text="Bank ID:")
# amount_label = tk.Label(root, text="Amount:")
# transfer_id_entry = tk.Entry(root)
# recipient_id_entry = tk.Entry(root)
# bank_id_entry = tk.Entry(root)
# amount_entry = tk.Entry(root)
# new_amount_label = tk.Label(root, text="New Amount:")
# new_amount_entry = tk.Entry(root)

# # Buttons for Takes_from
# insert_button = tk.Button(root, text="Insert Transfer", command=insert_takes_from)
# update_button = tk.Button(root, text="Update Transfer", command=update_takes_from)
# delete_button = tk.Button(root, text="Delete Transfer", command=delete_takes_from)

# # Grid layout for Takes_from
# transfer_id_label.grid(row=0, column=0)
# transfer_id_entry.grid(row=0, column=1)
# recipient_id_label.grid(row=1, column=0)
# recipient_id_entry.grid(row=1, column=1)
# bank_id_label.grid(row=2, column=0)
# bank_id_entry.grid(row=2, column=1)
# amount_label.grid(row=3, column=0)
# amount_entry.grid(row=3, column=1)
# insert_button.grid(row=4, columnspan=2)
# new_amount_label.grid(row=5, column=0)
# new_amount_entry.grid(row=5, column=1)
# update_button.grid(row=6, columnspan=2)
# delete_button.grid(row=7, columnspan=2)

# # Main loop
# root.mainloop()
# # Insert data into Takes_from table
# def insert_takes_from():
#     recipient_id = recipient_id_entry.get()
#     bank_id = bank_id_entry.get()
#     amount = amount_entry.get()

#     query = "INSERT INTO Takes_from (Recipient_ID, Bank_ID, Amount) VALUES (%s, %s, %s)"
#     values = (recipient_id, bank_id, amount)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Transfer inserted successfully")

# # Delete data from Takes_from table
# def delete_takes_from():
#     transfer_id = transfer_id_entry.get()

#     query = "DELETE FROM Takes_from WHERE Transfer_ID = %s"
#     values = (transfer_id,)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Transfer deleted successfully")

# # Update data in Takes_from table
# def update_takes_from():
#     transfer_id = transfer_id_entry.get()
#     new_amount = new_amount_entry.get()

#     query = "UPDATE Takes_from SET Amount = %s WHERE Transfer_ID = %s"
#     values = (new_amount, transfer_id)
#     cursor.execute(query, values)
#     db.commit()
#     messagebox.showinfo("Success", "Transfer updated successfully")

# # Display data from Takes_from table
# def display_takes_from():
#     query = "SELECT * FROM Takes_from"
#     cursor.execute(query)
#     results = cursor.fetchall()

#     result_text.delete("1.0", tk.END)
#     for row in results:
#         result_text.insert(tk.END, f"Transfer ID: {row[0]}, Recipient ID: {row[1]}, Bank ID: {row[2]}, Amount: {row[3]}\n")

# # Create the GUI window
# root = tk.Tk()
# root.title("Transfer Management")

# # Labels and Entry fields for Transfer
# transfer_id_label = tk.Label(root, text="Transfer ID:")
# recipient_id_label = tk.Label(root, text="Recipient ID:")
# bank_id_label = tk.Label(root, text="Bank ID:")
# amount_label = tk.Label(root, text="Amount:")
# transfer_id_entry = tk.Entry(root)
# recipient_id_entry = tk.Entry(root)
# bank_id_entry = tk.Entry(root)
# amount_entry = tk.Entry(root)
# new_amount_label = tk.Label(root, text="New Amount:")
# new_amount_entry = tk.Entry(root)

# # Buttons for Transfer
# insert_button = tk.Button(root, text="Insert Transfer", command=insert_takes_from)
# delete_button = tk.Button(root, text="Delete Transfer", command=delete_takes_from)
# update_button = tk.Button(root, text="Update Transfer", command=update_takes_from)
# display_button = tk.Button(root, text="Display Transfers", command=display_takes_from)

# # Text widget to display results
# result_text = tk.Text(root, height=10, width=50)

# # Grid layout for Transfer
# transfer_id_label.grid(row=0, column=0)
# transfer_id_entry.grid(row=0, column=1)
# recipient_id_label.grid(row=1, column=0)
# recipient_id_entry.grid(row=1, column=1)
# bank_id_label.grid(row=2, column=0)
# bank_id_entry.grid(row=2, column=1)
# amount_label.grid(row=3, column=0)
# amount_entry.grid(row=3, column=1)
# insert_button.grid(row=4, columnspan=2)
# delete_button.grid(row=5, columnspan=2)
# new_amount_label.grid(row=6, column=0)
# new_amount_entry.grid(row=6, column=1)
# update_button.grid(row=7, columnspan=2)
# display_button.grid(row=8, columnspan=2)
# result_text.grid(row=9, columnspan=2)

# # Main loop
# root.mainloop()

# # Close the database connection
db.close()
    
# Main loop
root.mainloop()

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


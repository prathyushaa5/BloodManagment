import tkinter as tk
from tkinter import messagebox

from blood import *


def staff_login():
     username = username_entry.get()
     password = password_entry.get()
    
     if username == "1" and password == "1":
        message_label.config(text="Login successful!", fg="green")
        root.destroy()
        option()
     else:
        message_label.config(text="Login failed. Please try again.", fg="red")

# GUI setup
root = tk.Tk()
window_width=600
window_height=400
root.geometry(f"{window_width}x{window_height}")
root.config(background="lightgray")
root.title("Login Page")
username_label = tk.Label(root, text="Username:",background="lightgray")
password_label = tk.Label(root, text="Password:",background="lightgray")
message_label = tk.Label(root, text="", fg="black",background="lightgray")

username_entry = tk.Entry(root,)
password_entry = tk.Entry(root, show="*")

login_button = tk.Button(root, text="Login", command=staff_login)

    # Layout using grid
username_label.grid(row=0,column=0,padx=20,pady=10)
username_entry.grid(row=0,column=1,padx=20,pady=10)
password_label.grid(row=1,column=0,padx=20,pady=10)
password_entry.grid(row=1,column=1,padx=20,pady=10)
login_button.grid(row=2,column=1,pady=20)
message_label.grid(row=3,columnspan=2)
root.mainloop()
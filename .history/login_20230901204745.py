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
root.config(bg="#00296B")
root.title("Login Page")
heading_label=tk.Label(root,text="BLOOD MANAGEMENT SYSTEM",font=("Helvetica",20,"bold"),bg="#00296B",fg="WHITE")
heading_label.pack(pady=20)
frame=tk.Frame(root,bg="#00509d")
frame.place(relx=0.5,rely=0.5,anchor="center")
username_label = tk.Label(frame, text="Username:",bg="#FFBD00")
password_label = tk.Label(frame, text="Password:",bg="#FFBD00")
message_label = tk.Label(frame, text="", bg="#FFBD00",fg="black")

username_entry = tk.Entry(frame)
password_entry = tk.Entry(frame, show="*")

login_button = tk.Button(frame, text="Login", command=staff_login,bg="BLACK",fg="white")

    # Layout using grid
username_label.grid(row=0,column=0,padx=20,pady=10)
username_entry.grid(row=0,column=1,padx=20,pady=10)
password_label.grid(row=1,column=0,padx=20,pady=10)
password_entry.grid(row=1,column=1,padx=20,pady=10)
login_button.grid(row=2,column=1,pady=20)
message_label.grid(row=3,columnspan=2)
root.mainloop()
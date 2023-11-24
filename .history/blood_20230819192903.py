import mysql.connector
import tkinter as tk
from tkinter import messagebox
from login import show_login
db=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
# Function to insert values into the database
# Database connection
cursor = db.cursor()

show_login()


import mysql.connector
conn=mysql.connector.connect(host='localhost',password='7338499857',username='root',port="3305",database="21csblood")
if conn.is_connected():
    print("Connection established")
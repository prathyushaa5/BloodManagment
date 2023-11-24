import mysql.connector
conn=mysql.connector.connect(host='localhost',password='7338499857',user='root',port="3307",database="21csblood")
if conn.is_connected():
    print("Connection established")
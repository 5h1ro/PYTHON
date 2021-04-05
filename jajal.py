import io
from tkinter import *
from tkinter import messagebox
# import tkinter as tk
import mysql.connector

db = mysql.connector.connect(
    user='root', 
    password='',
    host='127.0.0.1',
    database='design')
mycursor = db.cursor()

mycursor.execute("SELECT * FROM proyeks WHERE id = '1'")
p1 = mycursor.fetchone()

id = p1[0]
mycursor.execute("SELECT * FROM tasks WHERE idProyek = %s", (id,))
t2 = mycursor.fetchall()
mycursor.execute("SELECT * FROM proyeks")
t3 = mycursor.fetchall()
mycursor.execute("SELECT COUNT(id) FROM proyeks")
result = mycursor.fetchall()
print(t3)
# print(result)
for x in enumerate(result):
    z = 0
    c = 0
    for a in x:
        print(t3[c][1])
        print(z)
        z += 10
        c += 1
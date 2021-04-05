import io
from tkinter import *
from tkinter import messagebox
# import tkinter as tk
import mysql.connector

class uts:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.atas()
        self.menu()

    def atas(self):
        frameAtas = Frame(self.parent)
        frameAtas.pack()
        frameKiriUtama = Frame(frameAtas, background="black", border=2)
        frameKiriUtama.pack(side=LEFT, expand=YES, fill=Y)
        frameKiri = Frame(frameKiriUtama, height=50, width=1920)
        frameKiri.pack()
        al1 = Label(frameKiri, text="LOGO", font="Arial 20 bold")
        al1.pack()
        al1.place(x=1, y=6)
        ar1 = Button(frameKiri, text="LOGOUT", font="Arial 20 bold")
        ar1.pack()
        ar1.place(x=1780)

    def menu(self):
        frameMenu = Frame(self.parent)
        frameMenu.pack(pady=2)
        frameKiri = Frame(frameMenu, background="black", border=2)
        frameKiri.pack(side=LEFT, expand=YES, fill=BOTH)
        frameB2 = Frame(frameKiri, height=1030, width=200)
        frameB2.pack()
        self.menu1 = Button(frameB2, text="Dashboard", font="Arial 12 bold", relief="flat", command=self.dashboard)
        self.menu1.place(x=30, y=4)
        self.menu2 = Button(frameB2, text="Tambah Proyek", font="Arial 12 bold", relief="flat")
        self.menu2.place(x=30, y=44)
        self.menu3 = Button(frameB2, text="Tambah Task", font="Arial 12 bold", relief="flat", command=self.formTask)
        self.menu3.place(x=30, y=84)

        self.db = mysql.connector.connect(
            user='root', 
            password='',
            host='127.0.0.1',
            database='design')
        self.mycursor = self.db.cursor()

        self.mycursor.execute("SELECT * FROM proyeks WHERE id = '1'")
        p1 = self.mycursor.fetchone()

        frameKanan = Frame(frameMenu, background="black", border=2)
        frameKanan.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.frameMain = Frame(frameKanan, height=1030, width=1780)
        self.frameMain.pack()
        self.frameDashboard = Frame(self.frameMain, height=1030, width=1780)
        self.frameDashboard.place(x=2, y=2) 
        self.mycursor.execute("SELECT COUNT(id) FROM proyeks")
        result = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM proyeks")
        t1 = self.mycursor.fetchall()
        for x in enumerate(result):
            n = 0
            m = 0
            for a in x:
                self.frameProyek = Label(self.frameDashboard, height=15, width=60, relief=SOLID, borderwidth=2)
                self.frameProyek.place(x=2+n, y=2)  
                self.menuUtama1 = Label(self.frameProyek, text=t1[m][1], font="Arial 20 bold")
                self.menuUtama1.place(x=1, y=1)
                self.menuUtama2a = Label(self.frameProyek, text="Tanggal Mulai      :" , font="Arial 15 bold")
                self.menuUtama2a.place(x=1, y=50)
                self.menuUtama2b = Label(self.frameProyek, text=t1[m][3], font="Arial 15 bold")
                self.menuUtama2b.place(x=180, y=50)
                self.menuUtama3a = Label(self.frameProyek, text="Tanggal Berakhir :" , font="Arial 15 bold")
                self.menuUtama3a.place(x=1, y=80)
                self.menuUtama3b = Label(self.frameProyek, text=t1[m][4], font="Arial 15 bold")
                self.menuUtama3b.place(x=180, y=80)
                self.menuUtama4a = Label(self.frameProyek, text="Supervisor           :" , font="Arial 15 bold")
                self.menuUtama4a.place(x=1, y=110)
                self.menuUtama4b = Label(self.frameProyek, text=t1[m][2], font="Arial 15 bold")
                self.menuUtama4b.place(x=180, y=110)
                self.buttonDetail = Button(self.frameProyek, text="detail", font="Arial 12 bold", relief="flat", command=self.daftarTask)
                self.buttonDetail.place(x=360, y=190)
                n += 450
                m += 1

        id = p1[0]
        self.mycursor.execute("SELECT * FROM tasks WHERE idProyek = %s", (id,))
        t1 = self.mycursor.fetchone()
        self.frameDaftarTask = Frame(self.frameMain, height=1030, width=1780)
        self.frameTask = Label(self.frameDaftarTask, height=15, width=60, relief=SOLID, borderwidth=2)
        self.frameTask.place(x=2, y=2)  
        self.daftarTask1 = Label(self.frameTask, text=p1[1], font="Arial 20 bold")
        self.daftarTask1.place(x=1, y=1)
        self.daftarTask2a = Label(self.frameTask, text="Task                        :" , font="Arial 15 bold")
        self.daftarTask2a.place(x=1, y=50)
        self.daftarTask2b = Label(self.frameTask, text=t1[2], font="Arial 15 bold")
        self.daftarTask2b.place(x=205, y=50)
        self.daftarTask3a = Label(self.frameTask, text="Tanggal Mulai          :" , font="Arial 15 bold")
        self.daftarTask3a.place(x=1, y=80)
        self.daftarTask3b = Label(self.frameTask, text=t1[3], font="Arial 15 bold")
        self.daftarTask3b.place(x=205, y=80)
        self.daftarTask4a = Label(self.frameTask, text="Tanggal Berakhir     :" , font="Arial 15 bold")
        self.daftarTask4a.place(x=1, y=110)
        self.daftarTask4b = Label(self.frameTask, text=t1[4], font="Arial 15 bold")
        self.daftarTask4b.place(x=205, y=110)
        self.daftarTask5a = Label(self.frameTask, text="Penanggung Jawab :" , font="Arial 15 bold")
        self.daftarTask5a.place(x=1, y=140)
        self.daftarTask5b = Label(self.frameTask, text=t1[5], font="Arial 15 bold")
        self.daftarTask5b.place(x=205, y=140)
 

        self.frameTambahTask = Frame(self.frameMain, height=1030, width=1780)
        self.frameForm = Label(self.frameTambahTask, height=45, width=80, relief=SOLID, borderwidth=2)
        self.frameForm.pack()
        self.frameForm.place(x=2, y=2)  
        self.form1a = Label(self.frameForm, text="Masukkan Id Proyek :", font="Arial 15 bold")
        self.form1a.place(x=1, y=1)
        self.form1b = Entry(self.frameForm, font="Arial 15", width = 20, bd=2)
        self.form1b.place(x=280, y=1)
        self.form2a = Label(self.frameForm, text="Masukkan Nama Task :", font="Arial 15 bold")
        self.form2a.place(x=1, y=40)
        self.form2b = Entry(self.frameForm, font="Arial 15", width = 20, bd=2)
        self.form2b.place(x=280, y=40)
        self.form3a = Label(self.frameForm, text="Masukkan Tanggal Mulai :", font="Arial 15 bold")
        self.form3a.place(x=1, y=80)
        self.form3b = Entry(self.frameForm, font="Arial 15", width = 20, bd=2)
        self.form3b.place(x=280, y=80)
        self.form4a = Label(self.frameForm, text="Masukkan Tanggal Selesai :", font="Arial 15 bold")
        self.form4a.place(x=1, y=120)
        self.form4b = Entry(self.frameForm, font="Arial 15", width = 20, bd=2)
        self.form4b.place(x=280, y=120)
        self.form5a = Label(self.frameForm, text="Penanggung Jawab :", font="Arial 15 bold")
        self.form5a.place(x=1, y=160)
        self.form5b = Entry(self.frameForm, font="Arial 15", width = 20, bd=2)
        self.form5b.place(x=280, y=160)
        self.buttonTambahTask = Button(self.frameForm, text="Tambah", font="Arial 12 bold", relief="flat", command=self.tambahTask)
        self.buttonTambahTask.place(x=370, y=190)
        
    def dashboard(self, event=None):
        self.hideframe()
        self.frameDashboard.place(x=2, y=2) 
        
    def formTask(self, event=None):
        self.hideframe()
        self.frameTambahTask.place(x=2, y=2) 

    def daftarTask(self, event=None):
        self.hideframe()
        self.frameDaftarTask.place(x=2, y=2) 

    def daftarTask(self, event=None):
        self.hideframe()
        self.frameDaftarTask.place(x=2, y=2) 

    def hideframe(self, event=None):
        self.frameDashboard.place_forget()
        self.frameTambahTask.place_forget()
        self.frameDaftarTask.place_forget()
    
    
    def tambahTask(self, event=None):
        query = "INSERT INTO tasks (id, idProyek, namaTask, tglMulai, tglBerakhir, pj) VALUES(NULL,%s,%s,%s,%s,%s)"
        values = (self.form1b.get(), self.form2b.get(), self.form3b.get(), self.form4b.get(),  self.form5b.get())
        self.mycursor.execute(query, values)
        self.db.commit()
        self.form1b.delete(0,END)
        self.form2b.delete(0,END)
        self.form3b.delete(0,END)
        self.form4b.delete(0,END)
        self.form5b.delete(0,END)

if __name__ == '__main__' :
    root = Tk()
    spt = uts(root, "Penghitungan Pajak")
    root.mainloop()
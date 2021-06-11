import tkinter as tk
from tkinter import *
from tkinter import messagebox

class uts(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.atas()
        self.text1()
        self.identitas()
        self.text2()
        self.midA()
        self.midB()
        # s
        self.midC()
        self.footer()
    

    def atas(self):
        frameAtas = Frame(self)
        frameAtas.pack()
        frameKiriUtama = Frame(frameAtas, background="black", border=2)
        frameKiriUtama.pack(side=LEFT, expand=YES, fill=Y)
        frameKiri = Frame(frameKiriUtama, height=150, width=286)
        frameKiri.pack()
        al1 = Label(frameKiri, text="1770 SS", font="Arial 54 bold")
        al1.pack()
        al1.place(x=1, y=1)
        al2 = Label(frameKiri, text="PERHATIAN :", font="Arial 12 bold")
        al2.pack()
        al2.place(x=1, y=80)
        al3 = Label(frameKiri, text="● SEBELUM MENGISI BACA DAHULU PETUNJUK PENGISIAN", font="Arial 7 bold")
        al3.pack()
        al3.place(x=1, y=100)
        al4 = Label(frameKiri, text="● ISI DENGAN HURUF CETAK/DIKETIK DENGAN TINTA HITAM", font="Arial 7 bold")
        al4.pack()
        al4.place(x=1, y=115)
        al5 = Label(frameKiri, text="● SEBELUM MENGISI BACA DAHULU PETUNJUK PENGISIAN", font="Arial 7 bold")
        al5.pack()
        al5.place(x=1, y=130)

        
        frameKananUtama = Frame(frameAtas, background="black", border=2)
        frameKananUtama.pack(side=RIGHT, expand=YES, fill=Y)
        frameKanan = Frame(frameKananUtama, height=150, width=286)
        frameKanan.pack()
        ar1 = Label(frameKanan, text="TAHUN PAJAK", font="Arial 10 bold")
        ar1.pack()
        ar1.place(x=5, y=20)  
        ar2 = Label(frameKanan, text="2", font="Arial 20 bold", relief=SOLID, borderwidth=2, width=2)
        ar2.pack()
        ar2.place(x=110, y=22)
        ar3 = Label(frameKanan, text="0", font="Arial 20 bold", relief=SOLID, borderwidth=2, width=2)
        ar3.pack()
        ar3.place(x=148, y=22)
        ar4 = Entry(frameKanan, font="Arial 20 bold", relief=SOLID, borderwidth=2, width=2, justify=CENTER)
        ar4.pack()
        ar4.place(x=186, y=22)
        ar5 = Entry(frameKanan, font="Arial 20 bold", relief=SOLID, borderwidth=2, width=2, justify=CENTER)
        ar5.pack()
        ar5.place(x=220, y=22)
        kotakpetugas = Label(frameKanan, height=4, width=34, relief=SOLID, borderwidth=2)
        kotakpetugas.pack()
        kotakpetugas.place(x=13, y=65)  
        ar6 = Label(frameKanan, text="DIISI OLEH PETUGAS KPP", font="Arial 7")
        ar6.pack()
        ar6.place(x=75, y=80)
        ar7 = Label(frameKanan, text="BARCODE DITEMPEL DISINI", font="Arial 9")
        ar7.pack()
        ar7.place(x=55, y=95)
        
        frameTengahAtasUtama = Frame(frameAtas, background="black", border=2)
        frameTengahAtasUtama.pack(side=TOP, expand=YES, fill=BOTH)
        frameTengahAtas = Frame(frameTengahAtasUtama, height=48, width=286)
        frameTengahAtas.pack()
        ata1 = Label(frameTengahAtas, text="KEMENTERIAN KEUANGAN RI", font="Arial 13 bold")
        ata1.pack()
        ata1.place(x=20, y=5)
        ata2 = Label(frameTengahAtas, text="DIREKTORAT JENDERAL PAJAK", font="Arial 10")
        ata2.pack()
        ata2.place(x=40, y=25)

        
        frameTengahBawahUtama = Frame(frameAtas, background="black", border=2)
        frameTengahBawahUtama.pack(side=TOP, expand=YES, fill=BOTH)
        frameTengahBawah = Frame(frameTengahBawahUtama, height=98, width=286)
        frameTengahBawah.pack()
        atb1 = Label(frameTengahBawah, text="SPT TAHUNAN", font="Arial 20 bold")
        atb1.pack()
        atb1.place(x=40, y=5)
        atb2 = Label(frameTengahBawah, text="PAJAK PENGHASILAN", font="Arial 10 bold")
        atb2.pack()
        atb2.place(x=70, y=35)
        atb3 = Label(frameTengahBawah, text="WAJIB PAJAK ORANG PRIBADI", font="Arial 10 bold")
        atb3.pack()
        atb3.place(x=40, y=55)

    def text1(self):
        frameText = Frame(self)
        frameText.pack()
        l1 = Label(frameText, text="FORMULIR INI DIPERUNTUKKAN BAGI WP ORANG PRIBADI BERPENGHASILAN DARI SELAIN USAHA DAN/ATAU PEKERJAAN BEBAS DAN TIDAK LEBIH DARI Rp60 JUTA DALAM SATU TAHUN", font="Arial 7 bold")
        l1.pack()

    def identitas(self):
        frameIdentitas = Frame(self)
        frameIdentitas.pack()
        frameIdentity = Frame(frameIdentitas, background="black", border=2)
        frameIdentity.pack()
        
        frameIsiIdentitas = Frame(frameIdentity, height=100, width=866)
        frameIsiIdentitas.pack()
        i1 = Label(frameIsiIdentitas, text="NPWP", font="Arial 10")
        i1.pack()
        i1.place(x=50, y=25)

        i2 = Label(frameIsiIdentitas, text="NAMA WAJIB PAJAK", font="Arial 10")
        i2.pack()
        i2.place(x=50, y=50)

        i3 = Label(frameIsiIdentitas, text=":", font="Arial 10")
        i3.pack()
        i3.place(x=230, y=25)

        i4 = Label(frameIsiIdentitas, text=":", font="Arial 10")
        i4.pack()
        i4.place(x=230, y=50)
        
        i5 = Entry(frameIsiIdentitas, font="Arial 10", width=40)
        i5.pack()
        i5.place(x=270, y=25)

        i6 = Label(frameIsiIdentitas, text="-", font="Arial 10")
        i6.pack()
        i6.place(x=555, y=25)
        
        i7 = Entry(frameIsiIdentitas, font="Arial 10", width=15)
        i7.pack()
        i7.place(x=565, y=25)
        
        i8 = Label(frameIsiIdentitas, text="-", font="Arial 10")
        i8.pack()
        i8.place(x=675, y=25)
        
        i9 = Entry(frameIsiIdentitas, font="Arial 10", width=15)
        i9.pack()
        i9.place(x=685, y=25)
        
        i10 = Entry(frameIsiIdentitas, font="Arial 10", width=74)
        i10.pack()
        i10.place(x=270, y=50)

    def text2(self):
        frameText = Frame(self)
        frameText.pack()
        l1 = Label(frameText, text="Pengisian kolom-kolom yang berisi nilai rupiah harus tanpa nilai desimal", font="Arial 10 bold")
        l1.pack()

    def midA(self):
        frameMidA = Frame(self)
        frameMidA.pack(pady=2)
        frameAtas = Frame(frameMidA, background="black", border=2)
        frameAtas.pack(side=TOP, expand=YES, fill=X)
        frameA1 = Frame(frameAtas, height=25, width=866)
        frameA1.pack()
        aa1 = Label(frameA1, text="A. PAJAK PENGHASILAN", font="Arial 13 bold")
        aa1.pack()
        aa1.place(x=1, y=1)

        frameKiri = Frame(frameMidA, background="black", border=2)
        frameKiri.pack(side=LEFT, expand=YES, fill=BOTH)
        frameA2 = Frame(frameKiri, height=270, width=25)
        frameA2.pack()
        al1 = Label(frameA2, text="1", font="Arial 8 bold")
        al1.pack()
        al1.place(x=4, y=5)
        al2 = Label(frameA2, text="2", font="Arial 8 bold")
        al2.pack()
        al2.place(x=4, y=45)
        al3 = Label(frameA2, text="3", font="Arial 8 bold")
        al3.pack()
        al3.place(x=4, y=85)
        al4 = Label(frameA2, text="4", font="Arial 8 bold")
        al4.pack()
        al4.place(x=4, y=125)
        al5 = Label(frameA2, text="5", font="Arial 8 bold")
        al5.pack()
        al5.place(x=4, y=165)
        al6 = Label(frameA2, text="6", font="Arial 8 bold")
        al6.pack()
        al6.place(x=4, y=205)
        al7 = Label(frameA2, text="7", font="Arial 8 bold")
        al7.pack()
        al7.place(x=4, y=245)

        frameKanan = Frame(frameMidA, background="black", border=2)
        frameKanan.pack(side=RIGHT, expand=YES, fill=BOTH)
        frameA3 = Frame(frameKanan, height=270, width=837)
        frameA3.pack()
        ar1 = Label(frameA3, text="Penghasilan Bruto dalam Negeri Sehubungan dengan Pekerjaan dan Penghasilan Netto dalam Negeri Lainnya", font="Arial 8")
        ar1.pack()
        ar1.place(x=1, y=5)
        ar12 = Label(frameA3, text="1", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar12.pack()
        ar12.place(x=570, y=5)
        ar13 = Label(frameA3, text="A.01", font="Arial 8")
        ar13.pack()
        ar13.place(x=590, y=5)
        ar14 = Entry(frameA3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar14.pack()
        ar14.place(x=620, y=5)

        ar2 = Label(frameA3, text="Pengurangan", font="Arial 8")
        ar2.pack()
        ar2.place(x=1, y=45)
        ar2k = Label(frameA3, text="(Diisi jumlah pengurangan dari Formulir 1721-A1 angka 13 atau 1721-A2 angka 13)", font="Arial 6")
        ar2k.pack()
        ar2k.place(x=1, y=60)
        ar22 = Label(frameA3, text="2", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar22.pack()
        ar22.place(x=570, y=45)
        ar23 = Label(frameA3, text="A.02", font="Arial 8")
        ar23.pack()
        ar23.place(x=590, y=45)
        ar24 = Entry(frameA3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar24.pack()
        ar24.place(x=620, y=45)
        
        ar3 = Label(frameA3, text=" Penghasilan Tidak Kena Pajak", font="Arial 8")
        ar3.pack()
        ar3.place(x=1, y=85)
        ar32 = Label(frameA3, text="3", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar32.pack()
        ar32.place(x=570, y=85)
        ar33 = Label(frameA3, text="A.06", font="Arial 8")
        ar33.pack()
        ar33.place(x=590, y=85)
        ar34 = Entry(frameA3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar34.pack()
        ar34.place(x=620, y=85)      
        
        ar4 = Label(frameA3, text="Penghasilan Kena Pajak ( 1 - 2 - 3 )", font="Arial 8")
        ar4.pack()
        ar4.place(x=1, y=125)
        ar42 = Label(frameA3, text="4", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar42.pack()
        ar42.place(x=570, y=125)
        ar43 = Label(frameA3, text="A.07", font="Arial 8")
        ar43.pack()
        ar43.place(x=590, y=125)
        ar44 = Entry(frameA3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar44.pack()
        ar44.place(x=620, y=125)
        
        ar5 = Label(frameA3, text="Pajak Penghasilan Terutang", font="Arial 8")
        ar5.pack()
        ar5.place(x=1, y=165)
        ar52 = Label(frameA3, text="5", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar52.pack()
        ar52.place(x=570, y=165)
        ar53 = Label(frameA3, text="A.08", font="Arial 8")
        ar53.pack()
        ar53.place(x=590, y=165)
        ar54 = Entry(frameA3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar54.pack()
        ar54.place(x=620, y=165)
        
        ar6 = Label(frameA3, text="Pajak Penghasilan yang telah Dipotong oleh Pihak Lain", font="Arial 8")
        ar6.pack()
        ar6.place(x=1, y=205)
        ar62 = Label(frameA3, text="6", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar62.pack()
        ar62.place(x=570, y=205)
        ar63 = Label(frameA3, text="A.09", font="Arial 8")
        ar63.pack()
        ar63.place(x=590, y=205)
        ar64 = Entry(frameA3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar64.pack()
        ar64.place(x=620, y=205)
        
        ar7 = Label(frameA3, text="Pengurangan", font="Arial 8")
        ar7.pack()
        ar7.place(x=1, y=245)
        ar72 = Label(frameA3, text="7", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar72.pack()
        ar72.place(x=570, y=245)
        ar73 = Label(frameA3, text="A.12", font="Arial 8")
        ar73.pack()
        ar73.place(x=590, y=245)
        ar74 = Entry(frameA3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar74.pack()
        ar74.place(x=620, y=245)


        def tk0():
            a1=int(ar14.get())
            ptkp = 24300000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def tk1():
            a1=int(ar14.get())
            ptkp = 26325000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def tk2():
            a1=int(ar14.get())
            ptkp = 28350000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def tk3():
            a1=int(ar14.get())
            ptkp = 30375000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))

# tk

        def k0():
            a1=int(ar14.get())
            ptkp = 26315000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def k1():
            a1=int(ar14.get())
            ptkp = 28350000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def k2():
            a1=int(ar14.get())
            ptkp = 30375000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def k3():
            a1=int(ar14.get())
            ptkp = 32400000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))

        def ki0():
            a1=int(ar14.get())
            ptkp = 50625000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def ki1():
            a1=int(ar14.get())
            ptkp = 52650000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def ki2():
            a1=int(ar14.get())
            ptkp = 54675000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
        
        def ki3():
            a1=int(ar14.get())
            ptkp = 56700000
            a2=int(ar24.get())
            
            ar34.delete(0, END)
            ar34.insert(END, str(ptkp))
            a5 = a1+ptkp+a2
            ar44.delete(0, END)
            ar44.insert(END, str(a5))
            if a5 <= 50000000:
                totala5 = a5*0.05
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 50000000 and a5 <= 250000000:
                totala5 = a5*0.15
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 250000000 and a5 <= 500000000:
                totala5 = a5*0.25
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))
            elif a5 >= 500000000:
                totala5 = a5*0.30
                ar54.delete(0, END)
                ar54.insert(END, int(totala5))

        ar351 = Menubutton(frameA3, text="TK", relief=SOLID ,borderwidth=2 ,width=3)
        ar351.pack()
        ar351.place(x=300, y=85)
        ar351a = Menu(ar351, tearoff=0, bg='white')
        ar351["menu"]=ar351a
        ar351a.add_cascade(label='TK/0', command=tk0)
        ar351a.add_cascade(label='TK/1', command=tk1)
        ar351a.add_cascade(label='TK/2', command=tk2)
        ar351a.add_cascade(label='TK/3', command=tk3)

        
        ar352 = Menubutton(frameA3, text="K", relief=SOLID ,borderwidth=2 ,width=3)
        ar352.pack()
        ar352.place(x=350, y=85)
        ar352a = Menu(ar352, tearoff=0, bg='white')
        ar352["menu"]=ar352a
        ar352a.add_cascade(label='K/0', command=k0)
        ar352a.add_cascade(label='K/1', command=k1)
        ar352a.add_cascade(label='K/2', command=k2)
        ar352a.add_cascade(label='K/3', command=k3)
        
        ar353 = Menubutton(frameA3, text="K/I", relief=SOLID ,borderwidth=2 ,width=3)
        ar353.pack()
        ar353.place(x=400, y=85)
        ar353a = Menu(ar353, tearoff=0, bg='white')
        ar353["menu"]=ar353a
        ar353a.add_cascade(label='K/I/0', command=ki0)
        ar353a.add_cascade(label='K/I/1', command=ki1)
        ar353a.add_cascade(label='K/I/2', command=ki2)
        ar353a.add_cascade(label='K/I/3', command=ki3)

        
        def ar75b1(self, event=None):
            messagebox.showinfo("Lampirkan", "Lampirkan SSP Lembar Ke 3")

        i = StringVar()
        ar75 = Radiobutton(frameA3, text="Pajak Penghasilan yang harus Dibayar Sendiri *", font="Arial 6 bold", variable=i)
        ar75.pack()
        ar75.place(x=145, y=230)
        ar75.bind("<Button-1>", ar75b1)

        def ar75b2(self, event=None):
            ar54b2 = int(ar54.get())
            ar64b2 = int(ar64.get())
            ar75b2total = ar64b2 - ar54b2
            ar74.delete(0, END)
            ar74.insert(END, int(ar75b2total))
            

        i = StringVar()
        ar76 = Radiobutton(frameA3, text="Pajak Penghasilan yang Lebih Dipotong", font="Arial 6 bold", variable=i)
        ar76.pack()
        ar76.place(x=145, y=250)
        ar76.bind("<Button-1>", ar75b2)


        
    def midB(self):
        frameMidB = Frame(self)
        frameMidB.pack(pady=2)
        frameAtas = Frame(frameMidB, background="black", border=2)
        frameAtas.pack(side=TOP, expand=YES, fill=X)
        frameB1 = Frame(frameAtas, height=25, width=866)
        frameB1.pack()
        aa1 = Label(frameB1, text="B. PENGHASILAN YANG DIKENAKAN PPh FINAL DAN YANG DIKECUALIKAN DARI OBJEK PAJAK", font="Arial 13 bold")
        aa1.pack()
        aa1.place(x=1, y=1)

        frameKiri = Frame(frameMidB, background="black", border=2)
        frameKiri.pack(side=LEFT, expand=YES, fill=BOTH)
        frameB2 = Frame(frameKiri, height=110, width=25)
        frameB2.pack()
        al8 = Label(frameB2, text="8", font="Arial 8 bold")
        al8.pack()
        al8.place(x=4, y=5)
        al9 = Label(frameB2, text="9", font="Arial 8 bold")
        al9.pack()
        al9.place(x=4, y=45)
        al10 = Label(frameB2, text="10", font="Arial 8 bold")
        al10.pack()
        al10.place(x=4, y=85)

        frameKanan = Frame(frameMidB, background="black", border=2)
        frameKanan.pack(side=RIGHT, expand=YES, fill=BOTH)
        frameB3 = Frame(frameKanan, height=110, width=837)
        frameB3.pack()
        ar8 = Label(frameB3, text="Dasar Pengenaan Pajak/Penghasilan Bruto Pajak Penghasilan Final", font="Arial 8")
        ar8.pack()
        ar8.place(x=1, y=5)
        ar82 = Label(frameB3, text="8", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar82.pack()
        ar82.place(x=570, y=5)
        ar83 = Label(frameB3, text="B.01", font="Arial 8")
        ar83.pack()
        ar83.place(x=590, y=5)
        ar84 = Entry(frameB3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar84.pack()
        ar84.place(x=620, y=5)

        ar9 = Label(frameB3, text="Pajak Penghasilan Final Terutang", font="Arial 8")
        ar9.pack()
        ar9.place(x=1, y=45)
        ar92 = Label(frameB3, text="9", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar92.pack()
        ar92.place(x=570, y=45)
        ar93 = Label(frameB3, text="B.02", font="Arial 8")
        ar93.pack()
        ar93.place(x=590, y=45)
        ar94 = Entry(frameB3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar94.pack()
        ar94.place(x=620, y=45)
        
        ar10 = Label(frameB3, text="Penghasilan yang Dikecualikan dari Objek Pajak", font="Arial 8")
        ar10.pack()
        ar10.place(x=1, y=85)
        ar102 = Label(frameB3, text="10", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar102.pack()
        ar102.place(x=570, y=85)
        ar103 = Label(frameB3, text="B.03", font="Arial 8")
        ar103.pack()
        ar103.place(x=590, y=85)
        ar104 = Entry(frameB3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar104.pack()
        ar104.place(x=620, y=85)
    
    def midC(self):
        frameMidC = Frame(self)
        frameMidC.pack(pady=2)
        frameAtas = Frame(frameMidC, background="black", border=2)
        frameAtas.pack(side=TOP, expand=YES, fill=X)
        frameC1 = Frame(frameAtas, height=25, width=866)
        frameC1.pack()
        aa1 = Label(frameC1, text="C. DAFTAR HARTA DAN KEWAJIBAN", font="Arial 13 bold")
        aa1.pack()
        aa1.place(x=1, y=1)

        frameKiri = Frame(frameMidC, background="black", border=2)
        frameKiri.pack(side=LEFT, expand=YES, fill=BOTH)
        frameC2 = Frame(frameKiri, height=70, width=25)
        frameC2.pack()
        al11 = Label(frameC2, text="11", font="Arial 8 bold")
        al11.pack()
        al11.place(x=4, y=5)
        al12 = Label(frameC2, text="12", font="Arial 8 bold")
        al12.pack()
        al12.place(x=4, y=45)

        frameKanan = Frame(frameMidC, background="black", border=2)
        frameKanan.pack(side=RIGHT, expand=YES, fill=BOTH)
        frameC3 = Frame(frameKanan, height=70, width=837)
        frameC3.pack()
        ar11 = Label(frameC3, text="Jumlah Keseluruhan Harta yang Dimiliki pada Akhir Tahun Pajak", font="Arial 8")
        ar11.pack()
        ar11.place(x=1, y=5)
        ar112 = Label(frameC3, text="11", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar112.pack()
        ar112.place(x=570, y=5)
        ar113 = Label(frameC3, text="C.01", font="Arial 8")
        ar113.pack()
        ar113.place(x=590, y=5)
        ar114 = Entry(frameC3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar114.pack()
        ar114.place(x=620, y=5)

        ar12 = Label(frameC3, text="Jumlah Keseluruhan Kewajiban/Utang pada Akhir Tahun Pajak", font="Arial 8")
        ar12.pack()
        ar12.place(x=1, y=45)
        ar122 = Label(frameC3, text="12", font="Arial 8 bold", relief=SOLID, borderwidth=2, width=2)
        ar122.pack()
        ar122.place(x=570, y=45)
        ar123 = Label(frameC3, text="C.02", font="Arial 8")
        ar123.pack()
        ar123.place(x=590, y=45)
        ar124 = Entry(frameC3, font="Arial 8", relief=SOLID, borderwidth=2, width=34)
        ar124.pack()
        ar124.place(x=620, y=45)

    def footer(self):
        frameMidC = Frame(self)
        frameMidC.pack(pady=2)
        frameAtas = Frame(frameMidC, background="black", border=2)
        frameAtas.pack(side=TOP, expand=YES, fill=X)
        frameC1 = Frame(frameAtas, height=25, width=866)
        frameC1.pack()
        aa1 = Label(frameC1, text="PERNYATAAN", font="Arial 13 bold")
        aa1.pack()
        aa1.place(x=350, y=1)

        frameUtama = Frame(frameMidC, background="black", border=2)
        frameUtama.pack()
        frameC3 = Frame(frameUtama, height=140, width=866)
        frameC3.pack()
        af1 = Label(frameC3, text="Dengan menyadari sepenuhnya akan segala akibatnya termasuk sanksi-sanksi sesuai dengan ketentuan peraturan perundang-undangan yang berlaku", font="Arial 8")
        af1.pack()
        af1.place(x=30, y=10)
        af2 = Label(frameC3, text="Saya menyatakan bahwa apa yang telah saya beritahukan di atas adalah benar, lengkap, jelas.", font="Arial 8")
        af2.pack()
        af2.place(x=30, y=30)
        afk = Label(frameC3, text="P.01", font="Arial 6")
        afk.pack()
        afk.place(x=300, y=80)
        af3 = Entry(frameC3, font="Arial 12", width=4, justify=CENTER)
        af3.pack()
        af3.place(x=325, y=80)
        af3b = Label(frameC3, text="dd", font="Arial 7 italic")
        af3b.pack()
        af3b.place(x=335, y=105)
        af4 = Label(frameC3, text="-", font="Arial 12 bold")
        af4.pack()
        af4.place(x=370, y=78)
        af5 = Entry(frameC3, font="Arial 12", width=4, justify=CENTER)
        af5.pack()
        af5.place(x=385, y=80)
        af5b = Label(frameC3, text="mm", font="Arial 7 italic")
        af5b.pack()
        af5b.place(x=395, y=105)
        af6 = Label(frameC3, text="-", font="Arial 12 bold")
        af6.pack()
        af6.place(x=430, y=78)
        af7 = Entry(frameC3, font="Arial 12", width=8, justify=CENTER)
        af7.pack()
        af7.place(x=445, y=80)
        af7b = Label(frameC3, text="yyyy", font="Arial 7 italic")
        af7b.pack()
        af7b.place(x=465, y=105)

        
        kotakttd = Label(frameC3, height=4, width=30, relief=SOLID, borderwidth=2)
        kotakttd.pack()
        kotakttd.place(x=580, y=40)   
        ttd = Label(frameC3, text="Tanda Tangan", font="Arial 7 ")
        ttd.pack()
        ttd.place(x=580, y=108)


        
# header finish





def main():
    app = uts()
    app.master.title("Penghitungan Pajak")
    # app.master.resizable(0, 0)
    app.mainloop()

if __name__ == "__main__" :
    main()
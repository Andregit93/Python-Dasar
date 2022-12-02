from tkinter import *
import re
from typing import ContextManager, Pattern


root = Tk()
root.config(background="darkgray")
root.title("Kelulusan Mahasiswa")
root.resizable(FALSE,FALSE)
root.geometry("290x410")


label1 = Label(root, text="NAMA", width=20, anchor="w", bg="darkgrey", fg="yellow")
label1.grid(row=1, column=1) 
label2 = Label(root, text="NIM", width=20, anchor="w", bg="darkgrey", fg="yellow")
label2.grid(row=2, column=1) 
label3 = Label(root, text="KEHADIRAN", width=20, anchor="w", bg="darkgrey", fg="yellow")
label3.grid(row=3, column=1)
label4 = Label(root, text="NILAI TUGAS", width=20, anchor="w", bg="darkgrey", fg="yellow")
label4.grid(row=4, column=1)
label5 = Label(root, text="NILAI UTS", width=20, anchor="w", bg="darkgrey", fg="yellow")
label5.grid(row=5, column=1)
label6 = Label(root, text="NILAI UAS",  width=20, anchor="w", bg="darkgrey", fg="yellow")
label6.grid(row=6, column=1)
label11 = Label(root, text="HASIL", width=20, bg="darkgrey", fg="yellow")
label11.grid(row=7, column=1, columnspan=2)
label12 = Label(root, text="NAMA", width=20, anchor="w", bg="darkgrey", fg="yellow")
label12.grid(row=8, column=1)
label13 = Label(root, text="NIM", width=20, anchor="w", bg="darkgrey", fg="yellow")
label13.grid(row=9, column=1)
label7 = Label(root, text="JUMLAH NILAI", width=20, anchor="w", bg="darkgrey", fg="yellow")
label7.grid(row=10, column=1)
label8 = Label(root, text="RATA-RATA", width=20, anchor="w", bg="darkgrey", fg="yellow")
label8.grid(row=11, column=1)
label9 = Label(root, text="GRADE", width=20, anchor="w", bg="darkgrey", fg="yellow")
label9.grid(row=12, column=1)
label10 = Label(root, text="KETERANGAN", width=20, anchor="w", bg="darkgrey", fg="yellow")
label10.grid(row=13, column=1)


nama = Label(root, text=" ", width=20, bg="darkgrey", fg="yellow")
nama.grid(row=8, column=2)
nim = Label(root, text=" ", width=20, bg="darkgrey", fg="yellow")
nim.grid(row=9, column=2)
jumlah = Label(root, text="0", width=20, bg="darkgrey", fg="yellow")
jumlah.grid(row=10, column=2)
rata = Label(root, text="0", width=20, bg="darkgrey", fg="yellow")
rata.grid(row=11, column=2)
grade = Label(root, text="0", width=20, bg="darkgrey", fg="yellow")
grade.grid(row=12, column=2)
keterangan = Label(root, text="0", width=20, bg="darkgrey", fg="yellow")
keterangan.grid(row=13, column=2)


entry1 = Entry(root, width=20, bd=5)
entry1.grid(row=1, column=2)
entry2 = Entry(root, width=20, bd=5)
entry2.grid(row=2, column=2)
entry3 = Entry(root, width=20, bd=5)
entry3.grid(row=3, column=2)
entry4 = Entry(root, width=20, bd=5)
entry4.grid(row=4, column=2)
entry5 = Entry(root, width=20, bd=5)
entry5.grid(row=5, column=2)
entry6 = Entry(root, width=20, bd=5)
entry6.grid(row=6, column=2)


def Lihat_hasil():
   a = int(entry3.get())
   b = int(entry4.get())
   c = int(entry5.get())
   d = int(entry6.get())
   absen = (a / 16 * 100)
   jumlah.configure(text=(absen + b + c + d))
   jmlh = (0.1*absen + 0.2*b + 0.3*c + 0.4*d)
   rata.configure(text=(jmlh))
   if (jmlh >= 0) and (jmlh <30):
       grade.configure(text=("E"))
       keterangan.configure(text=("TIDAK LULUS"))
   elif (jmlh >= 30) and (jmlh <50):
       grade.configure(text=("D"))
       keterangan.configure(text=("TIDAK LULUS"))
   elif(jmlh >= 50) and (jmlh <70):
       grade.configure(text=("C"))
       keterangan.configure(text=("TIDAK LULUS"))
   elif(jmlh >= 70) and (jmlh <90):
       grade.configure(text=("B"))
       keterangan.configure(text=("LULUS"))
   elif (jmlh >= 90):
       grade.configure(text=("A"))
       keterangan.configure(text=("LULUS"))
   
   Pattern = "\D[^0123456789]""\D$"
   if (re.search(Pattern, entry1.get())):
       nama.configure(text=(entry1.get()))
   else:
       nama.configure(text=("Format Nama Salah"))

   pattern = re.compile(r'\d\d\d\d\d\d\d\d\d')
   if (re.search(pattern, entry2.get())):
       nim.configure(text=(entry2.get()))
   else:
       nim.configure(text=("Format Nim Salah"))


def hapus():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


button1 = Button(root, text="LIHAT HASIL", bg="darkgrey", fg="yellow", height=2, width=38, bd=5, activebackground="yellow", command=Lihat_hasil)
button1.grid(row=14, column=1, columnspan=2)
button2 = Button(root, text="HAPUS", bg="darkgrey", fg="yellow", height=2, width=38, bd=5, activebackground="yellow", command=hapus)
button2.grid(row=15, column=1, columnspan=2)

root.mainloop()
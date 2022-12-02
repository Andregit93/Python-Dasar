from tkinter import *
from tkinter import messagebox


root = Tk()
root.config(background="darkgray")
root.title("KASIR")
root.resizable(FALSE,FALSE)
root.geometry("670x470")


#MENU
lbl1 = Label(root, text="KASIR WARKOP ANDRE", fg="chocolate", bg="darkgrey")
lbl1.grid(column=1, columnspan=4)
lbl2 = Label(root, text="KODE MENU :", anchor="e", width=20, bg="darkgrey")
lbl2.grid(row=3, column=1)
lbl3 = Label(root, text="1. Cappucino   20K", anchor="w", width=20, bg="darkgrey",)
lbl3.grid(row=4, column=2)
lbl4 = Label(root, text="2. Machiato   19K", anchor="w", width=20, bg="darkgrey")
lbl4.grid(row=5, column=2)
lbl5 =Label(root, text="3. Affogato   20K", anchor="w", width=20, bg="darkgrey")
lbl5.grid(row=6, column=2) 
lbl6 = Label(root, text="4. Espresso   15K", anchor="w", width=20, bg="darkgrey")
lbl6.grid(row=4, column=3)
lbl7 = Label(root, text="5. Coffee Latte   20K", anchor="w", width=20, bg="darkgrey")
lbl7.grid(row=5, column=3)
lbl8 = Label(root, text="6. Vanilla Latte   23K", anchor="w", width=20, bg="darkgrey")
lbl8.grid(row=6, column=3)
lbl9 = Label(root, text="7. Americano   15K", anchor="w", width=20, bg="darkgrey")
lbl9.grid(row=4, column=4)
lbl10 = Label(root, text="8. Frapucino   22K", anchor="w", width=20, bg="darkgrey")
lbl10.grid(row=5, column=4)
lbl11 = Label(root, text="9. Caramel Latte   23K", anchor="w", width=20, bg="darkgrey")
lbl11.grid(row=6, column=4)


#PESANAN
lbl12 = Label(root, text="PESANAN :", anchor="e", width=20, bg="darkgrey")
lbl12.grid(row=7, column=1)
lbl13 = Label(root, text="Kode Menu", anchor="w", width=20, bg="darkgrey")
lbl13.grid(row=8, column=2)
lbl14 = Label(root, text="Jumlah Pesan", anchor="w", width=20, bg="darkgrey")
lbl14.grid(row=9, column=2)
ent1 = Entry(root, width=10, bg="darkgrey")
ent1.grid(row=8, column=3)
ent2 = Entry(root, width=10, bg="darkgrey")
ent2.grid(row=9, column=3)
ent3 = Entry(root, width=20, bg="darkgrey")
ent3.grid(row=11, column=3)
ent4 = Entry(root, width=20, bg="darkgrey")
ent4.grid(row=13, column=3)
lbl15 = Label(root, text="TOTAL", anchor="w", width=20, bg="darkgrey")
lbl15.grid(row=10, column=2)
total = Entry(root, text=" ", width=20, bg="darkgrey")
total.grid(row=10, column=3)
lbl16 = Label(root, text="Masukan Uang", anchor="w", width=20, bg="darkgrey")
lbl16.grid(row=11, column=2)
lbl19 = Label(root, text="Masukan Kembalian", anchor="w", width=20, bg="darkgrey")
lbl19.grid(row=13, column=2)


#FUCTION
def total_harga():
    a = int(ent1.get())
    b = int(ent2.get())
    if a == 1:
        hrga = int(20000)
    elif a == 2:
        hrga = int(19000)
    elif a == 3:
        hrga = int(20000)
    elif a == 4:
        hrga = int(15000)
    elif a == 5:
        hrga = int(20000)
    elif a == 6:
        hrga = int(23000)
    elif a == 7:
        hrga = int(15000)
    elif a == 8:
        hrga = int(22000)
    elif a == 9:
        hrga = int(23000)
    c = hrga * b
    total.insert(0, c)
    second_number = c
    if math == 'tambah':
        total.delete(0, END)
        total.insert(0, f_num + second_number)

def mulang():
    a = int(ent3.get())
    b = int(total.get())
    global tip
    tip = str(a - b)
    if a == b:
        messagebox.showinfo("KASIR WARKOP ANDRE","UANG PAS \nTRANSAKSI SELESAI \nTERIMA KASIH")
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        total.delete(0, END)
    elif a <b:
        messagebox.showinfo("KASIR WARKOP ANDRE","UANG KURANG")
        ent3.delete(0, END)
    else:
        messagebox.showinfo("KASIR WARKOP ANDRE", "KEMBALIAN :"+tip)
    
def selesai():  
    a = str(ent4.get())
    if a == tip:
        messagebox.showinfo("KASIR WARKOP ANDRE","TRANSAKSI SELESAI \nTERIMA KASIH")
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        total.delete(0, END)
    else:
        messagebox.showinfo("KASIR WARKOP ANDRE","KEMBALIAN SALAH")
        ent4.delete(0, END)

def nambah():
    a = int(ent1.get())
    b = int(ent2.get())
    if a == 1:
        hrga = int(20000)
    elif a == 2:
        hrga = int(19000)
    elif a == 3:
        hrga = int(20000)
    elif a == 4:
        hrga = int(15000)
    elif a == 5:
        hrga = int(20000)
    elif a == 6:
        hrga = int(23000)
    elif a == 7:
        hrga = int(15000)
    elif a == 8:
        hrga = int(22000)
    elif a == 9:
        hrga = int(23000)
    c = hrga*b
    first_number = c
    global f_num
    global math
    math = 'tambah'
    f_num = int(first_number)
    ent1.delete(0, END)
    ent2.delete(0, END)

def list():
    ent4.insert(0, list1.get(ANCHOR))

def tambah():
    first_number = ent4.get()
    global f_num
    global math
    math = 'tambah'
    f_num = int(first_number)
    ent4.delete(0, END)

def samdeng():
    second_number = ent4.get()
    ent4.delete(0, END)
    if math == 'tambah':
        ent4.insert(0, f_num + int(second_number))



#LIST
list1 = Listbox(root, height=8, bg="darkgrey")
list1.grid(row=14, column=3)
list1_isi = ["500", "1000", "2000", "5000", "10000", "20000", "50000", "100000"]
for isi in list1_isi:
    list1.insert(END, isi)


#tombol
btn1 = Button(root, text="TAMBAH", width=20, bg="darkgrey", command=nambah)
btn1.grid(row=12, column=2)
btn2 = Button(root, text="CEK TOTAL", width=20, command=total_harga, bg="darkgrey")
btn2.grid(row=12, column=3)
btn3 = Button(root, text="CEK KEMBALIAN", width=20, command=mulang, bg="darkgrey")
btn3.grid(row=12, column=4)
btn4 = Button(root, text="SELESAI", width=20, command=selesai, bg="darkgrey")
btn4.grid(row=13, column=4)
btn5 = Button(root, text="PILIH", width=20, command=list, bg="darkgrey")
btn5.grid(row=15, column=3)
btn6 = Button(root, text="TAMBAH", width=20, command=tambah, bg="darkgrey")
btn6.grid(row=15, column=2)
btn7 = Button(root, text="HASIL", width=20, command=samdeng, bg="darkgrey")
btn7.grid(row=15, column=4)


root.mainloop()
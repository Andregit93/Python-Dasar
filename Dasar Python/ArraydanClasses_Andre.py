#Array
#Data
#Apk = Meta, Whatsapp, Instagram, Youtube
#Buah = Alpukat, Mangga, Nanas, Salak
#HeroDC = Batman, Superman, WonderWowan, TheFlash
#penerapan array 1 dimensi 
Data = [["Meta", "Whatsapp", "Instagram", "Youtube"], ["Alpukat", "Mangga", "Nanas", "Salak"], ["Batman", "Superman", "WonderWowan", "TheFlash"]]
print(Data)
print(Data[1])
print(Data[2][2])

#penerapan array 2 dimensi
Tabel = [["Meta", "Whatsapp", "Instagram", "Youtube"], ["Alpukat", "Mangga", "Nanas", "Salak"], ["Batman", "Superman", "WonderWowan", "TheFlash"]]
for i in Tabel: #membuat data menjadi matrik
    print(i) #perintah untuk menampilkan matrik

#penerapan array 3 dimensi 
# array 3 dimensi merupakan array yang elemennya memiliki larik 2-D array atau matriks
Data1 = ([[["Meta", "Whatsapp", "Instagram", "Youtube"], 
["Alpukat", "Mangga", "Nanas", "Salak"], 
["Batman", "Superman", "WonderWowan", "TheFlash"]]])
print(Data1[0][1][2])
print(Data1[0][2][1], Data1[0][0][3], Data1[0][2][3])


#class
#contoh pertama
class MyClass: #perintah untuk membuat class 
    a = 12 #perintah untuk membuat properti bernama a
b = MyClass() #perintah untuk membuat object b
print(b.a) #perintah untuk mencetak nilai a

#contoh kedua
class Sejarah: # perintah untuk membuat class bernama Sejarah
  def __init__(self, Negara, Merdeka): #perintah untuk menetapkan Negara dan tahun merdeka
    self.Negara = Negara
    self.Merdeka = Merdeka 

a = Sejarah("Indonesia", 1945) #perintah untuk memberi tahu object yang di cetak adalah a

print(a.Negara) #perintah untuk mencetak a berupa Negara
print(a.Merdeka) #perintah untuk mencetak a berupa Merdeka

#contoh ketiga
class Saya: #perintah untuk membuat class bernama Sejarah
  def __init__(self, nama, umur): #perintah untuk menetapkan nama dan umur
    self.nama = nama
    self.umur = umur

  def myfunc(self):
    print("Hai Nama Saya adalah " + self.nama) #perintah untuk mencetak teks Hai nama saya adalah ditambah dengan nama

a = Saya("Andre Sevtian", 18)
a.myfunc()
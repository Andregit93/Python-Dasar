#python inheritance
#contoh 1
class Laptop: #perintah untuk membuat super class bernama Laptop
  def __init__(self, tipe, processor, ram, penyimpanan): #perintah untuk menambahkan variabel tipe, processor, ram, dan penyimpanan pada super class Laptop
    self.tipe = tipe
    self.processor = processor
    self.ram = ram
    self.penyimpanan = penyimpanan

  def cek_spesifikasi(self): #menambahkan perintah cek_spesifikasi
    print("tipe:", self.tipe, "\nprocessor:", self.processor,"\nram:", self.ram, "\npeyimpanan:", self.penyimpanan) #perintah untuk menampilkan output tipe, processor, ram, dan penyimpanan

class Macbook(Laptop): #perintah untuk membuat super class baru bernama Macbook tapi mewariskan atau menurunkan super class Laptop
  def cek_spesifikasi(self):
    print("cek website apple.com") #perintah untuk mengganti output menjadi cek website apple.com


laptop1 = Laptop("ASUS", "Intel core i5 10th","8 GB", "512GB SSD") #perintah untuk membuat subclass dan mengisi variabel tipe, processor, ram, dan penyimpanan
laptop2 = Laptop("Lenovo", "AMD Ryzen5 5300u", "8 GB", "1TB SSD") #perintah untuk membuat subclass dan mengisi variabel tipe, processor, ram, dan penyimpanan
laptop3 = Macbook("Macbook pro M1", "? ", "? ", "? ") #perintah untuk membuat subclass dan mengisi variabel tipe, processor, ram, dan penyimpanan

laptop1.cek_spesifikasi() #menampilkan output subclass laptop1 dengan perintah cek_spesifikasi
laptop2.cek_spesifikasi()#menampilkan output subclass laptop2 dengan perintah cek_spesifikasi
laptop3.cek_spesifikasi()#menampilkan output subclass laptop3 dengan perintah cek_spesifikasi

#contoh 2
class Ojek:
  def __init__(self, nama, kendaraan, daerah):
    self.nama = nama
    self.kendaraan = kendaraan
    self.daerah = daerah

  def cek_bio(self):
    print("nama:", self.nama, "\nkendaraan:", self.kendaraan, "\ndaerah:", self.daerah)

class Gojek(Ojek):
  def cek_bio(self):
    print("cek aplikasi gojek")


ojek1 = Ojek("udin", "Honda Beat", "pasar pagi")
ojek2 = Ojek("dani", "Scoopy", "K.keramat")
ojek3 = Gojek("toni", "supra", "selindung")

ojek1.cek_bio()
ojek2.cek_bio()
ojek3.cek_bio()
# while loops
a = 9 #perintah untuk menginput angka 9 kedalam variabel a 
while a < 36: #perintah untuk menjalankan perulangan selama variabel a kurang dari 36
    print(a) #perintah untuk menampilkan angka di variabel a
    a += 9 #perintah untuk menaikan nilai variabel a sebanyak 9 angka di setiap pengulangan

b = 5 #perintah untuk menginput angka 5 kedalam variabel b
while b < 30: #perintah untuk menjalankan perulangan selama variabel b kurang dari 30
  print(b) #perintah untuk menampilkan angka di variabel b
  if (b == 15): #perintah untuk menghentikan kenaikan nilai variabel b di angka 15 di pengulangan
    break #perintah untuk menghentikan kenaikan nilai variabel b di pengulangan
  b += 5 #perintah untuk menaikan nilai variabel b sebanyak 5 angka di setiap pengulangan

c = 2 #perintah untuk menginput angka 2 kedalam variabel c
while c < 10: #perintah untuk menjalankan perulangan selama variabel c kurang dari 10
  c += 2 #perintah untuk menaikan nilai variabel c sebanyak 2 angka di setiap pengulangan
  if c == 8: #perintah untuk menghilangkan angka 8 di pengulangan
    continue #perintah untuk menghilangkan angka di pengulangan 
  print(c) #perintah untuk menampilkan angka di variabel c


#for loops
fruits = ["Jambu", "Manggis", "Kates"] #objek fruits untuk dicetak
for a in fruits: #perintah untuk mencetak menggunakan variabel a di objek fruits
  print(a) #perintah untuk mencetak variabel a

for b in "Jambu": #perintah untuk mengulangi per huruf dalam kata Jambu menggunakan variabel b
  print(b) #perintah untuk menampilkan per huruf Jambu di variabel b

fruits = ["Jambu", "Manggis", "Kates"] #objek fruits untuk dicetak
for c in fruits: #perintah untuk mencetak menggunakan variabel c di objek fruits
  print(c) #perintah untuk mencetak variabel c
  if c == "Manggis": #perintah untuk mencetak variabel c dan berhenti di objek Manggis
    break #perintah untuk berhenti mencetak di objek Manggis di variabel c


#functions
def my_function(Buah = ""): #perintah untuk memasukkan(Buah) kedalam 'my_function'
    print("saya suka buah " + Buah) #perintah untuk menambahkan teks saya suka buah pada 'my_function'
my_function("Jambu") #my_function blok kode yang hanya berjalan ketika dipanggil

def my_function(Minum = ""): #perintah untuk memasukkan(Minum) kedalam 'my_function'
    print("saya suka " + Minum) #perintah untuk menambahkan teks saya suka pada 'my_function'
my_function("Kuku bima") #my_function blok kode yang hanya berjalan ketika dipanggil

def my_function(Makan = ""): #perintah untuk memasukkan(Makan) kedalam 'my_function'
    print("saya suka " + Makan) #perintah untuk menambahkan teks saya suka pada 'my_function'
my_function("Alpukat") #my_function blok kode yang hanya berjalan ketika dipanggil
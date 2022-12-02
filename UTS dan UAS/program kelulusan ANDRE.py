#Program untuk menentukan kelulusan mahasiswa
import re #perintah untuk menambahkan module regex
pattern = "\D[^0123456789]""\D$" #regex untuk input berupa karakter dari a-z A-Z tidak boleh menggunakan angka
nama = input ("Masukan Nama : ") #perintah untuk membuat var nama yang outputnya "masukan nama :" dan harus di input sesuatu
if (re.search(pattern, nama)): #perintah untuk mencocokan data antara var pattern dan input pada output var nama
    print("Nama Tersedia") #jika data antara var pattern dan var nama cocok, maka outputnya adalah "nama tersedia" 
else:
    print("Nama Tidak Tersedia") #jika data antara var pattern dan var nama tidak cocok, maka outputnya adalah "nama tidak tersedia"

pattern = re.compile(r'\d\d\d\d\d\d\d\d\d') #regex untuk input hanya angka tidak boleh menggunakan huruf
nim = input("Masukan NIM : " ) #perintah untuk membuat var nim yang outputnya "masukan nim :" dan harus di input sesuatu
if (re.search(pattern, nim)): #perintah untuk mencocokan data antara var pattern dan input pada output var nim
    print("NIM Tersedia") #jika data antara var pattern dan var nim cocok, maka outputnya adalah "nama tersedia" 
else:
    print("NIM Tidak Tersedia") #jika data antara var pattern dan var nim tidak cocok, maka outputnya adalah "nama tidak tersedia"

absen = int(input("Masukan Nilai Kehadiran : ")) #perintah untuk membuat var absen yang outputnya "masukan nilai kehadiran :" dan harus di input dengan angka
tugas = int(input("Masukan Nilai Tugas : ")) #perintah untuk membuat var tugas yang outputnya "masukan nilai tugas :" dan harus di input dengan angka
uts = int(input("Masukan Nilai UTS : ")) #perintah untuk membuat var uts yang outputnya "masukan nilai uts :" dan harus di input dengan angka
uas = int(input("Masukan Nilai UAS : ")) #perintah untuk membuat var uas yang outputnya "masukan nilai uas :" dan harus di input dengan angka

na = (0.1 * absen) + (0.2 * tugas) + (0.3 * uts) + (0.4 * uas) #perintah untuk membuat var na yang melakukan perkalian terhadap var absen, tugas, uts, dan uas
if (na >= 0) and (na <30): #jika var na lebih dari 0 dan kurang dari 30
    Grade = "E" #maka outputnya adalah "E"
    ket = "TIDAK LULUS" #maka outputnya "TIDAK LULUS"
elif (na >= 31) and (na <50): #jika var na lebih dari 31 dan kurang dari 50
    Grade = "D" #maka outputnya adalah "D"
    ket = "TIDAK LULUS" #maka outputnya "TIDAK LULUS"
elif (na >= 51) and (na <70): #jika var na lebih dari 51 dan kurang dari 70
    Grade = "C" #maka outputnya adalah "C"
    ket = "TIDAK LULUS" #maka outputnya "TIDAK LULUS"
elif (na >= 71) and (na <90): #jika var na lebih dari 71 dan kurang dari 90
    Grade = "B" #maka outputnya adalah "B"
    ket = "LULUS" #maka outputnya "LULUS"
elif (na >= 91) and (na <100): #jika var na lebih dari 91 dan kuang dari 100
    Grade = "A" #maka outputnya adalah "A"
    ket = "LULUS" #maka outputnya "LULUS"

print("Jumlah Nilai :", absen + tugas + uts + uas) #perintah untuk mengeluarkan output "jumlah nilai :" dan melakukan penjumlahan pada var absen, tugas, uts, dan uas
print("Nilai Rata-rata :", na) #perintah untuk mengeluarkan output "nilai rata-rata :" dan hasil parkalian pada var na
print("Nilai Grade :", Grade) #perintah untuk mengeluarkan output "nilai grade :" dan output var Grade 
print("Keterangan: ", ket) #perintah untuk mengeluarkan output "keterangan :" dan output var ket
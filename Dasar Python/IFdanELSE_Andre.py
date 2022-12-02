# list
List1 = ["apple","banana","cherry"]
List2 = [1, 5, 7, 9, 3]
List3 = [True, False, False]
print(List1)
print(List2)
print(List3)

# if else
a=200
b=200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("b is not greater than a")

#jika pernyataan pada if bernilai TRUE maka if akan diekse
nilai = 56
if (nilai > 8):
    print("selamat anda lulus")
else:
    print("maaf anda tidak lulus")

#hari
hari_ini = input("hari : ")
if(hari_ini == "senin"):
    print("saya akan kuliah")
elif(hari_ini == "selasa"):
    print("saya akan kuliah")
elif(hari_ini == "rabu"):
    print("saya akan kuliah")
elif(hari_ini == "kamis"):
    print("saya akan kuliah")
elif(hari_ini == "jumat"):
    print("saya akan kuliah")
elif(hari_ini == "sabtu"):
    print("saya akan kuliah")
elif(hari_ini == "minggu"):
    print("saya akan tidur")

#Belanja
total = int(input("Total Belanja : Rp."))
if total > 100000:
    print("bonus Bimoli 1L")
elif total >= 90000:
    print("bonus Bimoli 500ml")
elif total >= 80000:
    print("bonus Bimoli 200ml")
elif total >= 50000:
    print("bonus lifeboy")
elif total >= 25000:
    print("bonus sunlight")
else:
    print("tidak ada bonus")

#Nilai
nilai = int(input('Masukan nilai: '))
if nilai >= 95:
    print('predikat A')
elif nilai >= 85:
    print('predikat B')
elif nilai >= 75:
    print('predikat C')
elif nilai >= 55:
    print('predikat D')
else:
    print('predikat E')

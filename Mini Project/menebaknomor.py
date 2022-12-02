from ast import Continue
import random

masukan_nomor = input("masukan angka: ")

if masukan_nomor.isdigit():
    masukan_nomor = int(masukan_nomor)

    if masukan_nomor <= 0:
        print("masukan angka yang lebih dari 0")
        quit()

else:
    print("masukan nomor lain kali")

angkarandom = random.randint(0, masukan_nomor)
berapa_tebakan = 0
while True:
    berapa_tebakan += 1
    tebakan = input("buat tebakan: ")
    if tebakan.isdigit():
        tebakan = int(tebakan)
    else:
        print("masukan nomor lain kali")
        continue

    if tebakan == angkarandom:
        print("kamu benar")
        break
    else:
        print("kamu salah")

print("kamu benar setelah", berapa_tebakan, "kali menebak")
    
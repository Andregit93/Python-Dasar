import random 

poin_pemain = 0
poin_computer = 0

pilihan = ["batu", "gunting", "kertas"]

while True:
    pilihan_pemain = input("ketik batu/gunting/kertas atau q untuk keluar: ")
    if pilihan_pemain == "q":
        break

    if pilihan_pemain not in pilihan:
        continue

    angka_acak = random.randint(0, 2)
    pilihan_komputer = pilihan[angka_acak]
    print("komputer memilih", pilihan_komputer + ".")

    if pilihan_pemain == "batu" and pilihan_komputer == "gunting":
        print("kamu menang")
        poin_pemain += 1
    
    elif pilihan_pemain == "gunting" and pilihan_komputer == "kertas":
        print("kamu menang")
        poin_pemain += 1

    elif pilihan_pemain == "kertas" and pilihan_komputer == "batu":
        print("kamu menang")
        poin_pemain += 1
    
    elif pilihan_pemain == pilihan_komputer:
        print("seri")
    
    else:
        print("kamu kalah")
        poin_computer += 1

print("kamu menang", poin_pemain, "kali")
print("komputer menang", poin_computer, "kali")
print("goodbye")

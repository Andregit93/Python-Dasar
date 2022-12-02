print("selamat datang di SevtianQuiz")

main = input("apakah anda mau bermain? ")

if main.lower() != "mau":
    quit()

print("oke ayo mulai")
nilai = 0

soal1 = input("apa yang dimaksud dengan RAM? ")
if soal1.lower() == "random access memory":
    print("benar!")
    nilai += 1
else:
    print ("salah!")

soal2 = input("apa yang dimaksud dengan CPU? ")
if soal2.lower() == "central processor unit":
    print("benar!")
    nilai += 1
else:
    print ("salah!")

soal3 = input("apa yang dimaksud dengan GPU? ")
if soal3.lower() == "ghraphic processor unit":
    print("benar!")
    nilai += 1
else:
    print ("salah!")

soal4 = input("apa yang dimaksud dengan PSU? ")
if soal4.lower() == "power supply unit":
    print("benar!")
    nilai += 1
else:
    print ("salah!")

print("jawaban benar " + str(nilai))
print("nilai " + str(nilai/4*100))
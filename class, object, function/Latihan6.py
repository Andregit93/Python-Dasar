class handphone:
    def __init__(self):
        print("--SELAMAT DATANG DI SEVCELL--\nMerek Handphone yg tersedia : \n1. Samsung\n2. Xiaomi")
        self.merek = input("merek : ")
        if (self.merek == 'samsung' or self.merek == '1'):
            print(
                "--Silahkan Pilih Type--\n1. Samsung 1\n2. Samsung 2\n3. Samsung 3")
            self.Type = input("Pilih Type : ")
        if (self.merek == 'xiaomi' or self.merek == '2'):
            print(
                "--Silahkan Pilih Type--\n1. Xiaomi 1\n2. Xiaomi 2\n3. Xiaomi 3")
            self.Type = input("Pilih Type : ")

    def merekhp(self):
        print("--Merk dan Type Handphone yg dipilih")
        if (self.merek == 'samsung' or self.merek == '1'):
            print("merek : Samsung")
        elif (self.merek == 'xiaomi' or self.merek == '2'):
            print("merek : Xiaomi")
        else:
            print("merek : Tidak Tersedia")

    def hpsamsung(self):
        if (self.merek == "samsung" or self.merek == "1"):
            if (self.Type == 'samsung 1' or self.Type == '1'):
                print("Type : Samsung 1")
            if (self.Type == 'samsung 2' or self.Type == '2'):
                print("Type : Samsung 2")
            if (self.Type == 'samsung 3' or self.Type == '3'):
                print("Type : Samsung 3")

    def hpxiaomi(self):
        if (self.merek == "xiaomi" or self.merek == "2"):
            if (self.Type == 'xiaomi 1' or self.Type == '1'):
                print("Type : Xiaomi 1")
            if (self.Type == 'xiaomi 2' or self.Type == '2'):
                print("Type : Xiaomi 2")
            if (self.Type == 'xiaomi 3' or self.Type == '3'):
                print("Type : Xiaomi 3")


class hasilsemua(handphone):
    def __init__(self):
        hp1 = handphone()
        hp1.merekhp()
        hp1.hpsamsung()
        hp1.hpxiaomi()


hasilsemua()

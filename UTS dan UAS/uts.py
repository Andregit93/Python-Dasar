class unmuhbabel:
    def __init__(self):
        print("--SELAMAT DATANG di UNMUH BABEL--\nSilahkan Pilih Fakultas Anda\n1. FKIP\n2. FTS")
        self.fakultas = input('Pilih Fakultas : ')
        if (self.fakultas == "FKIP" or self.fakultas == "fkip" or self.fakultas == "Fkip" or self.fakultas == "1"):
            print(
                "--Selamat Datang di FKIP--\nSilahkan Pilih Prodi Anda\n1. PGSD\n2. PMTK\n3. PJKR\n4. PBI")
            self.jurusan = input("Pilih Prodi : ")

        elif (self.fakultas == "FTS" or self.fakultas == "fts" or self.fakultas == "Fts" or self.fakultas == "2"):
            print(
                "--Selamat Datang di FTS--\nSilahkan Pilih Prodi Anda\n1. ILKOM\n2. KSDA\n3. TEKSIP")
            self.jurusan = input("Pilih Prodi : ")

    def prodifkip(self):
        if (self.fakultas == "FKIP" or self.fakultas == "fkip" or self.fakultas == "Fkip" or self.fakultas == "1"):
            if (self.jurusan == 'PGSD' or self.jurusan == 'pgsd' or self.jurusan == 'Pgsd' or self.jurusan == '1'):
                print("Prodi : PGSD")
            elif (self.jurusan == 'PMTK' or self.jurusan == 'pmtk' or self.jurusan == 'Pmtk' or self.jurusan == '2'):
                print("Prodi : PMTK")
            elif (self.jurusan == 'PJKR' or self.jurusan == 'pjkr' or self.jurusan == 'Pjkr' or self.jurusan == '3'):
                print("Prodi : PJKR")
            elif (self.jurusan == 'PBI' or self.jurusan == 'pbi' or self.jurusan == 'Pbi' or self.jurusan == '4'):
                print("Prodi : PBI")
            else:
                print("Prodi : Tidak Tersedia")

    def prodifts(self):
        if (self.fakultas == "FTS" or self.fakultas == "fts" or self.fakultas == "Fts" or self.fakultas == "2"):
            if (self.jurusan == 'ILKOM' or self.jurusan == 'ilkom' or self.jurusan == 'Ilkom' or self.jurusan == '1'):
                print("Prodi : ILKOM")
            elif (self.jurusan == 'KSDA' or self.jurusan == 'ksda' or self.jurusan == 'Ksda' or self.jurusan == '2'):
                print("Prodi : KSDA")
            elif (self.jurusan == 'TEKSIP' or self.jurusan == 'teksip' or self.jurusan == 'Teksip' or self.jurusan == '3'):
                print("Prodi : TEKSIP")
            else:
                print("Prodi : Tidak Tersedia")

    def tampilfakultas(self):
        if (self.fakultas == "FKIP" or self.fakultas == "fkip" or self.fakultas == "Fkip" or self.fakultas == "1"):
            print("Fakultas : FKIP")
        elif (self.fakultas == "FTS" or self.fakultas == "fts" or self.fakultas == "Fts" or self.fakultas == "2"):
            print("Fakultas : FTS")
        else:
            print("Fakultas : Tidak Tersedia")


class mahasiswa(unmuhbabel):
    def __init__(self):
        self.nama = input("Masukkan Nama Anda : ")
        self.nim = int(input("Masukkan NIM Anda : "))

    def tampildata(self):
        print("--DATA MAHASISWA--")
        print("Nama : ", self.nama)
        print("NIM : ", self.nim)


class nilaiakhir(mahasiswa):
    def __init__(self):
        self.matkul = input("Masukkan Mata Kuliah : ")
        self.UTS = int(input("Masukkan Nilai UTS : "))
        self.UAS = int(input("Masukkan Nilai UAS : "))

    def hitunggrade(self):
        ratarata = int(0.4 * self.UTS) + (self.UAS * 0.6)
        print("Nilai Rata-rata : ", ratarata)

        if (ratarata <= 50):
            print("Grade : E")
            print("Ket : Tidak Lulus")
        if (ratarata <= 64) and (ratarata >= 51):
            print("Grade : D")
            print("Ket : Tidak Lulus")
        if (ratarata <= 74) and (ratarata >= 65):
            print("Grade : C")
            print("Ket : Lulus")
        if (ratarata <= 84) and (ratarata >= 75):
            print("Grade : B")
            print("Ket : Lulus")
        if (ratarata >= 85):
            print("Grade : A")
            print("Ket : Lulus")

    def hasilgrade(self):
        print("Mata Kuliah : ", self.matkul)
        print("Nilai UTS : ", self.UTS)
        print("Nilai UAS : ", self.UAS)


class tampilsemua(nilaiakhir):
    def __init__(self):
        jr = unmuhbabel()
        mh = mahasiswa()
        na = nilaiakhir()
        mh.tampildata()
        jr.tampilfakultas()
        jr.prodifkip()
        jr.prodifts()
        na.hasilgrade()
        na.hitunggrade()


tampilsemua()

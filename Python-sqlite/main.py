import sqlite3

# membuat koneksi ke database
conn = sqlite3.connect('student.db')

# membuat cursor
cursor = conn.cursor()

# membuat table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        nim INTEGER,
        no_hp INTEGER
    )
''')

while True:
    try:
        end = input("Masukkan q untuk keluar : ")
        if end == "q" or end == "Q":
            print("Terima Kasih!")
            break

        # mengisi data ke dalam table
        name = input("Masukkan Nama : ")
        nim = input("Masukkan Nim : ")
        phoneNum = input("Masukkan no HP : ")

        query = """INSERT INTO students
            (nama, nim, no_hp)
            VALUES ('{}', '{}', '{}')""".format(
                name, nim, phoneNum)
        cursor.execute(query)

        # menyimpan perubahan
        conn.commit()
        print("Berhasil Menambahkan Data")

    except sqlite3.Error as e:
        print("Gagal Menambahkan Data Karena", e)

    

# menutup koneksi ke database
conn.close()
print("Sambungan ke Database Terputus!")

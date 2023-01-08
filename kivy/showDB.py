import sqlite3
import pandas as pd

# membuat koneksi ke database
conn = sqlite3.connect("student.db")

# membuat cursor
cursor = conn.cursor()

# Menampilkan Semua isi dari tabel students
cursor.execute("select * from employs ")
for row in cursor:
    print(row)

conn.close()
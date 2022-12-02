import sqlite3
import pandas as pd

# load gta.db file (make sure you run main.py first to create it)
connection = sqlite3.connect("seleven.db")
# create a cursor object to execute SQL
cursor = connection.cursor()

# SELECT all isi dari tabel sale_item yang ada di dalam file seleven.db
cursor.execute("select * from sale_items")
for row in cursor:
    print(row)

connection.close()

import sqlite3

# menghubungkan ke file database, jika filenya tidak ada akan dibuatkan 
connection = sqlite3.connect("seleven.db")
# communicate with the database
cursor = connection.cursor()

# data yang akan dimasukkan ke database
item_list = [
    (2323, "Indomie", 3500, "PT UsusBuntu"),
    (2324, "Torpedo", 2000, "PT GinjalRusak"),
    (2325, "Beng-beng", 3000, "PT KantongKering"),
    (2326, "Taro", 5000, "PT Madura"),
    (2327, "Ale ale", 2000, "PT GinjalRusak"),
    (2328, "Ciki-ciki", 4000, "PT Madura"),
    (2329, "Mie Sedap", 3500, "PT UsusBuntu")
]
 
price_list = [
    (3500, 5000),
    (2000, 3000),
    (3000, 4000),
    (4000, 6000),
    (5000, 8000)
]

# create database table and populate it with release_list
cursor.execute("create table sale_items (product_Id integer, product_name text, product_price integer, supplier text)")
cursor.executemany("insert into sale_items values (?,?,?,?)", item_list)
# save changes immediatley
connection.commit()

# print semua baris pada tabel
for row in cursor.execute("select * from sale_items"):
    print(row)

# print specific rows from the gta table
print("******************************")
cursor.execute("select * from sale_items where supplier=:s", {"s": "PT UsusBuntu"})
items_search = cursor.fetchall()
print(items_search)

# membuat tabel baru price
cursor.execute("create table price (price integer, update_price integer)")
cursor.executemany("insert into price values (?,?)", price_list)
# # save changes immediatley
connection.commit()
# select only the rows where gta_city=Liberty City
cursor.execute("select * from price where price=:p", {"p": 3500})
price_search = cursor.fetchall()
print(price_search)

# combine data from 2 tables and manipulate it
print("***************************************")
for i in items_search:
    #replace every instance of "Liberty City" with "New York"
    update = [price_search[0][1] if value==price_search[0][0] else value for value in i]
    print(update)

# terminate the connection to "seleven.db"
connection.close()

from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"

		# Create Database Or Connect To One
		conn = sqlite3.connect('Seleven.db')

		# Create A Cursor
		c = conn.cursor()

		# Create A Table
		c.execute("""CREATE TABLE if not exists saleItems(
		    id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            harga INTEGER)
		 """)

		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()

		return Builder.load_file('function.kv')



	def submit(self):
		# Create Database Or Connect To One
		conn = sqlite3.connect('Seleven.db')

		# Create A Cursor
		c = conn.cursor()

		# Add A Record
		c.execute("""INSERT INTO saleItems (nama, harga) 
					VALUES ('{}', '{}')""".format(
						self.root.ids.input_nama.text, self.root.ids.input_harga.text))

		# Add a little message
		self.root.ids.nama_label.text = f'{self.root.ids.nama_input.text} Berhasil Ditambahkan'

		# Clear the input box
		
		self.root.ids.nama_input.text = ''


		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()

		

	def show_records(self):
		# Create Database Or Connect To One
		conn = sqlite3.connect('Seleven.db')

		# Create A Cursor
		c = conn.cursor()

		# Grab records from database
		c.execute("SELECT * FROM saleItems")
		records = c.fetchall()

		word = ''
		# Loop thru records
		for record in records:
			word = f'{word}\n{record[0]}'
			self.root.ids.nama_label.text = f'{word}'

		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()


MainApp().run()
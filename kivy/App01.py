# Import the necessary modules
import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window




# Connect to the database
conn = sqlite3.connect('sevtianstore.db')
cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS saleItems (
                    id_brg INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_brg TEXT, 
                    harga_brg INTEGER
    )
""")

# Define a function that allows the user to input data
def input_data(self):

    self.name = name_input.text
    self.price = price_input.text
    
  # Insert the data into the database
    query = """INSERT INTO saleItems
            (nama_brg, harga_brg)
            VALUES ('{}', '{}')""".format(
                self.name, self.price)
    cursor.execute(query)
    conn.commit()

    # Clear the input fields
    name_input.text = ''
    price_input.text = ''


# Define a function that shows the data from the database
def show_data(self):
    # Query the database for all records
    self.result = cursor.execute("SELECT * FROM saleItems")

    # Create a string to hold the output
    self.output_barang = "ID            NAMA | HARGA\n\n"
    

    # Loop through the query results and append them to the output string
    for row in self.result:
        self.output_barang += str(row[0])
        self.output_barang += "              " + str(row[1])
        self.output_barang += "    |    Rp. " + str(row[2]) + '\n'

    # Set the label's text to the output string
    output_barang.text = self.output_barang

# Define the GUI
class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        # Create the input fields
        global name_input
        name_input = TextInput(multiline=False)
        layout.add_widget(Label(text='Nama Barang'))
        layout.add_widget(name_input)

        global price_input
        price_input = TextInput(multiline=False)
        layout.add_widget(Label(text='Harga Barang'))
        layout.add_widget(price_input)

        # Create the buttons
        input_button = Button(text='Tambah')
        input_button.bind(on_press=input_data)
        layout.add_widget(input_button)

        show_button = Button(text='Riwayat')
        show_button.bind(on_press=show_data)
        layout.add_widget(show_button)

        # Create the output label
        global output_barang
        output_barang = Label(text='')
        layout.add_widget(output_barang)

        return layout

    def on_start(self):
        Window.size = (500, 900)
        

# Run the app
if __name__ == "__main__":
    MyApp().run()

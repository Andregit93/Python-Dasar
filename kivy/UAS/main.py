import kivy
import sqlite3
from kivymd.app import MDApp
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# menangkap data dari input dan memasukkannya ke database
def input_to_database(nama_value, ttg_value, email_value, username_value, password_value, handphone_value):
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS employs (
                    nama_emp TEXT, 
                    ttg_emp INTEGER,
                    email_emp TEXT,
                    username TEXT,
                    password TEXT,
                    Handphone INTEGER
                    )
                """)

    cur.execute("""INSERT INTO employs 
                    (nama_emp, ttg_emp, email_emp, username, password, Handphone) 
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
                    nama_value, ttg_value, email_value, username_value, password_value, handphone_value
                     ))
    conn.commit()
    conn.close()

# screen pertama
class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_label = Label(text='SELAMAT DATANG DI', markup=True, pos_hint={'x': 0.20, 'y': 0.44 }, pos=(100, 100), 
        text_size=(300, None))
        self.add_widget(self.data_label)
        self.data_label = Label(text='BRI MOBILE', markup=True, pos_hint={'x': 0.29, 'y': 0.41}, pos=(100, 100), 
        text_size=(300, None))
        self.add_widget(self.data_label)

        self.layout = GridLayout(cols=1, padding=[40, 30, 40, 300])
        self.add_widget(self.layout)

        self.image = Image(source='img/bri.png', pos_hint={'x': 0.1, 'y': 0.1}, pos=(100, 100), 
        size_hint=(0.9, 0.9), size=(150, 150))
        self.layout.add_widget(self.image)

        self.layout1 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 70])
        self.add_widget(self.layout1)
        self.button1 = Button(text='Masuk', size_hint=(0.8, 0.15))        
        self.button1.bind(on_press=self.open_login_window)        
        self.layout1.add_widget(self.button1)
        
        self.layout2 = BoxLayout(orientation='horizontal', padding=[40, 0, 40, 150])
        self.add_widget(self.layout2)
        self.button2 = Button(text='Daftar', size_hint=(0.8, 0.15))        
        self.button2.bind(on_press=self.open_second_window)        
        self.layout2.add_widget(self.button2)
        
    def open_second_window(self, instance):
        self.manager.current = 'second'    

    def open_login_window(self, instance):
        self.manager.current = 'login'    

# screen kedua / screen daftar
class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 200])
        self.add_widget(self.layout)
        
        self.nama = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='Nama'))
        self.layout.add_widget(self.nama)
        
        self.ttg = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='Tangal Lahir'))
        self.layout.add_widget(self.ttg)

        self.email = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='Email'))
        self.layout.add_widget(self.email)

        self.username = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='Username'))
        self.layout.add_widget(self.username)

        self.password = TextInput(size_hint=(1, 0.8), password=True)
        self.layout.add_widget(Label(text='Password'))
        self.layout.add_widget(self.password)

        self.handphone = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='Handphone'))
        self.layout.add_widget(self.handphone)

        self.layout2 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 130])
        self.add_widget(self.layout2)

        self.button1 = Button(text='Batal', size_hint=(0.5, 0.15))
        self.button1.bind(on_press=self.open_main_window)
        self.layout2.add_widget(self.button1)
        
        self.button2 = Button(text='Daftar', size_hint=(0.5, 0.15))
        self.button2.bind(on_press=self.input_to_database)
        self.layout2.add_widget(self.button2)

        self.layout3 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 64])
        self.add_widget(self.layout3)
        
        self.button3 = Button(text='Masuk', size_hint=(0.8, 0.15))        
        self.button3.bind(on_press=self.open_login_window)        
        self.layout3.add_widget(self.button3)

    def open_main_window(self, instance):
        self.manager.current = 'main'
        
    def open_login_window(self, instance):
        self.manager.current = 'login'
        
    def input_to_database(self, instance):
        nama_value = self.nama.text
        ttg_value = self.ttg.text
        email_value = self.email.text
        username_value = self.username.text
        password_value = self.password.text
        handphone_value = self.handphone.text
        
        input_to_database(nama_value, ttg_value, email_value, username_value, password_value, handphone_value)

        self.nama.text = ''
        self.ttg.text = ''
        self.email.text = ''
        self.username.text = ''
        self.password.text = ''
        self.handphone.text = ''

# screen 3 / screen login
class LoginWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_popup1 = Popup(title='Error', content=Label(text='Username atau password salah'), size_hint=(None, None), size=(400, 400))
        self.error_popup2 = Popup(title='Error', content=Label(text='Masukkan Username atau Password terlebih dahulu'), size_hint=(None, None), size=(400, 400))
        self.data_label = Label(text='SILAHKAN MASUKKAN', pos_hint={'x': 0.20, 'y': 0.45 }, pos=(100, 100), 
        text_size=(300, None))
        self.add_widget(self.data_label)
        self.data_label = Label(text='USERNAME DAN PASSWORD', pos_hint={'x': 0.15, 'y': 0.40}, pos=(100, 100), 
        text_size=(300, None))
        self.add_widget(self.data_label)

        self.layout1 = GridLayout(cols=1, padding=[40, 30, 40, 300])
        self.add_widget(self.layout1)
        self.image = Image(source='img/bri.png', pos_hint={'x': 0.1, 'y': 0.1}, pos=(100, 100), 
        size_hint=(0.9, 0.9), size=(150, 150))
        self.layout1.add_widget(self.image)

        self.layout2 = BoxLayout(orientation='vertical', padding=[40, 260, 40, 200])
        self.add_widget(self.layout2)
        global username
        username = TextInput(size_hint=(1, 0.8))
        self.layout2.add_widget(Label(text='Username'))
        self.layout2.add_widget(username)
        
        global password
        password = TextInput(size_hint=(1, 0.8), password=True)
        self.layout2.add_widget(Label(text='Password'))
        self.layout2.add_widget(password)

        self.layout3 = BoxLayout(orientation='horizontal', padding=[40, 80, 40, 100])
        self.add_widget(self.layout3)
        self.button3 = Button(text='Batal', size_hint=(0.8, 0.15))        
        self.button3.bind(on_press=self.open_main_window)      
        self.layout3.add_widget(self.button3)
        self.button4 = Button(text='Login', size_hint=(0.8, 0.15))        
        self.button4.bind(on_press=self.login)      
        self.layout3.add_widget(self.button4)

    def login(self, *args):
        username_value = username.text
        password_value = password.text

        # mengambil data dari database berdasarkan username dan ditampilkan di screen 4 
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        self.result = cur.execute("SELECT * FROM employs WHERE username='{}'".format(username_value))
        self.output_username = ""
        self.output_password = ""
        self.output_nama = ""
        self.output_ttg = ""
        self.output_email = ""
        self.output_handphone = ""
            
        for row in self.result:
            self.output_username += str(row[3])
            self.output_password += str(row[4])
            self.output_nama += str(row[0])
            self.output_ttg += str(row[1])
            self.output_email += str(row[2])
            self.output_handphone += str(row[5])
        
        # validasi username dan password
        if username_value == "" and password_value == "":
            self.error_popup2.open()
        else:
            if username_value == self.output_username and password_value == self.output_password:
                self.manager.current = 'third'
                output_username.text += self.output_username
                output_password.text += self.output_password
                output_nama.text += self.output_nama
                output_ttg.text += self.output_ttg
                output_email.text += self.output_email
                output_handphone.text += self.output_handphone

                username.text = ''
                password.text = ''
            
            else:
                self.error_popup1.open()
                username.text = ''
                password.text = ''  

    def open_main_window(self, instance):
        self.manager.current = 'main'

# screen empat / screen data
class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout1 = GridLayout(cols=1, padding=[40, 20, 40, 350])
        self.add_widget(self.layout1)
        self.image = Image(source='img/andre.jpg', pos_hint={'x': 0.1, 'y': 0.1}, pos=(100, 100), 
        size_hint=(0.5, 0.5), size=(100, 100))
        self.layout1.add_widget(self.image)

        self.layout = BoxLayout(orientation='vertical', padding=[100, 270, 0, 120])
        global output_username
        output_username = Label(text='Username  :   ', pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(350, None))
        self.layout.add_widget(output_username)
        global output_password
        output_password = Label(text='Password  :   ', pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(350, None))
        self.layout.add_widget(output_password)
        global output_nama
        output_nama = Label(text='Nama  :   ', pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(350, None))
        self.layout.add_widget(output_nama)
        global output_ttg
        output_ttg = Label(text='Tanggal Lahir  :   ', pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(350, None))
        self.layout.add_widget(output_ttg)
        global output_email
        output_email = Label(text='Email    :   ', pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(350, None))
        self.layout.add_widget(output_email)
        global output_handphone
        output_handphone = Label(text='Handphone    :   ', pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(350, None))
        self.layout.add_widget(output_handphone)
        self.add_widget(self.layout)

        self.layout2 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 30])
        self.add_widget(self.layout2)
        self.button1 = Button(text='Log Out', size_hint=(0.8, 0.15))        
        self.button1.bind(on_press=self.open_main_window)        
        self.layout2.add_widget(self.button1)
        
    # mereset semua data di screen 4 / screen data
    def open_main_window(self, instance):
        self.manager.current = 'main'
        output_username.text = ""
        output_password.text = ""
        output_nama.text = ""
        output_ttg.text = ""
        output_email.text = ""
        output_handphone.text = ""

        output_username.text += "Username : "
        output_password.text += "Password : "
        output_nama.text += "Nama : "
        output_ttg.text += "Tanggal Lahir : "
        output_email.text += "Email : "
        output_handphone.text += "Handphone : "

class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager() 
        
        self.main_window = MainWindow(name='main')
        self.second_window = SecondWindow(name='second')
        self.third_window = ThirdWindow(name='third')
        self.login_window = LoginWindow(name='login')
        
        self.screen_manager.add_widget(self.main_window)
        self.screen_manager.add_widget(self.second_window)
        self.screen_manager.add_widget(self.third_window)
        self.screen_manager.add_widget(self.login_window)
        
        return self.screen_manager
        
    # mengatur ukuran window
    def on_start(self):
        Window.size = (360, 600)    

if __name__ == '__main__':
    MainApp().run()

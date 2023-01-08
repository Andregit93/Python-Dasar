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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

def input_to_database(nama_value, nim_value, prodi_value):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    no INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_mhs TEXT, 
                    nim_mhs INTEGER,
                    prodi_mhs TEXT
                    )
                """)

    cur.execute("""INSERT INTO students 
                    (nama_mhs, nim_mhs, prodi_mhs) 
                    VALUES ('{}', '{}', '{}')""".format(
                    nama_value, nim_value, prodi_value
                     ))
    conn.commit()
    conn.close()

def show_data(self):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    self.result = cur.execute("SELECT * FROM students")

    self.output_no = ""
    self.output_nama = ""
    self.output_nim = ""
    self.output_prodi = ""
        
    for row in self.result:
        self.output_no += '\n' + str(row[0])
        self.output_nama += '\n' + str(row[1])
        self.output_nim += '\n' + str(row[2])
        self.output_prodi += '\n' + str(row[3])

    output_no.text += self.output_no
    output_nama.text += self.output_nama
    output_nim.text += self.output_nim
    output_prodi.text += self.output_prodi


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, padding=[40, 50, 40, 100])
        self.add_widget(self.layout)
        
        self.image = Image(source='test/img/bro.jpg', pos_hint={'x': 0.1, 'y': 0.1}, pos=(100, 100), 
        size_hint=(0.8, 0.9), size=(100, 100))
        self.layout.add_widget(self.image)
        self.button = Button(text='Start', pos_hint={'x': 0.1, 'y': 0.1}, pos=(100, 100),
        size_hint=(0.8, 0.15), size=(100, 100))
        self.button.bind(on_press=self.open_second_window)
        self.layout.add_widget(self.button)
        
    def open_second_window(self, instance):
        self.manager.current = 'second'    


class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # layout 1
        self.layout = BoxLayout(orientation='vertical', padding=[40, 70, 40, 250])
        self.add_widget(self.layout)
        
        self.nama = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='NAMA'))
        self.layout.add_widget(self.nama)
        
        self.nim = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='NIM'))
        self.layout.add_widget(self.nim)

        self.prodi = TextInput(size_hint=(1, 0.8))
        self.layout.add_widget(Label(text='PRODI'))
        self.layout.add_widget(self.prodi)

        # layout 2
        self.layout2 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 170])
        self.add_widget(self.layout2)

        self.button1 = Button(text='Back', size_hint=(0.5, 0.15))
        self.button1.bind(on_press=self.open_main_window)
        self.layout2.add_widget(self.button1)
        
        self.button2 = Button(text='Save', size_hint=(0.5, 0.15))
        self.button2.bind(on_press=self.input_to_database)
        self.layout2.add_widget(self.button2)

        # layout 3
        self.layout3 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 111])
        self.add_widget(self.layout3)
        
        self.button3 = Button(text='History', size_hint=(0.8, 0.15))        
        self.button3.bind(on_press=self.open_third_window)        
        self.layout3.add_widget(self.button3)

    def open_main_window(self, instance):
        self.manager.current = 'main'
        
    def open_third_window(self, instance):
        self.manager.current = 'third'
        
    def input_to_database(self, instance):
        nama_value = self.nama.text
        nim_value = self.nim.text
        prodi_value = self.prodi.text
        
        input_to_database(nama_value, nim_value, prodi_value)

        self.nama.text = ''
        self.nim.text = ''
        self.prodi.text = ''
        

class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # layout 1
        self.layout = BoxLayout(orientation='horizontal', padding=[10, 40, 10, 500])
        self.data_label = Label(text='[u]STUDENTS DATA[/u]', markup=True, pos_hint={'x': 0.25, 'y': 0.45}, pos=(100, 100), 
        text_size=(300, None))
        self.add_widget(self.data_label)
        global output_no
        output_no = Label(text='[u]NO[/u]', markup=True)
        self.layout.add_widget(output_no)
        global output_nama
        output_nama = Label(text='[u]NAMA[/u]', markup=True, pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(100, None))
        self.layout.add_widget(output_nama)
        global output_nim
        output_nim = Label(text='[u]NIM[/u]', markup=True, pos_hint={'x': 0.1, 'y': 0.01}, pos=(100, 100),
        text_size=(100, None))
        self.layout.add_widget(output_nim)
        global output_prodi
        output_prodi = Label(text='[u]PRODI[/u]', markup=True)
        self.layout.add_widget(output_prodi)
        self.add_widget(self.layout)

        # layout 3
        self.layout3 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 101])
        self.add_widget(self.layout3)
        self.button1 = Button(text='Back', size_hint=(0.5, 0.15))
        self.button1.bind(on_press=self.back_to_second_window)
        self.layout3.add_widget(self.button1)
        self.button2 = Button(text='Show Data', size_hint=(0.5, 0.15))
        self.button2.bind(on_press=show_data)
        self.layout3.add_widget(self.button2)

        # layout 4
        self.layout4 = BoxLayout(orientation='horizontal', padding=[40, 100, 40, 30])
        self.add_widget(self.layout4)
        self.button3 = Button(text='Log Out', size_hint=(0.8, 0.15))        
        self.button3.bind(on_press=self.open_main_window)        
        self.layout4.add_widget(self.button3)
        
    def back_to_second_window(self, instance):
        self.manager.current = 'second'
    
    def open_main_window(self, instance):
        self.manager.current = 'main'
    

class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager() 
        
        self.main_window = MainWindow(name='main')
        self.second_window = SecondWindow(name='second')
        self.third_window = ThirdWindow(name='third')
        
        self.screen_manager.add_widget(self.main_window)
        self.screen_manager.add_widget(self.second_window)
        self.screen_manager.add_widget(self.third_window)
        
        return self.screen_manager

    def on_start(self):
        Window.size = (360, 600)    

if __name__ == '__main__':
    MainApp().run()

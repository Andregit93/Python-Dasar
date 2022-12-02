import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout_utama = BoxLayout(orientation="vertical")
        label1 = Label(text="Aplikasi Pertama")
        entry1 = TextInput(hint_text="Masukkan Nama")
        entry2 = TextInput(hint_text="Masukkan NIM")
        entry3 = TextInput(hint_text="Masukkan Alamat")
        button1 = Button(text="Save")
        layout_utama.add_widget(label1)
        layout_utama.add_widget(entry1)
        layout_utama.add_widget(entry2)
        layout_utama.add_widget(entry3)
        layout_utama.add_widget(button1)
        return layout_utama
tester = MyApp()
tester.run()
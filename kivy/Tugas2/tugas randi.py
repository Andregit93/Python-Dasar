from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window

class FirstWindow(Screen):
	def spinner_clicked(self, value):
		self.ids.click_label.text = f'Ini {value}'

class SecondWindow(Screen):
	pass

class ThirdWindow(TabbedPanel, Screen):
	pass
        
class WindowManager(ScreenManager):
	pass

kv = Builder.load_file('tugas randi.kv')


class AwesomeApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	AwesomeApp().run()
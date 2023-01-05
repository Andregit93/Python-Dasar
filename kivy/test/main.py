from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window

#Define our different screens
class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
	def spinner_clicked(self, value):
		self.ids.click_label.text = f'Login As {value}'

class ThirdWindow(TabbedPanel, Screen):
	pass
        


class WindowManager(ScreenManager):
	pass

# Designate Our .kv design file 
kv = Builder.load_file('main.kv')


class AwesomeApp(App):
	def build(self):
		return kv
    
    

if __name__ == '__main__':
	AwesomeApp().run()

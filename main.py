from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy



#class for design ,will be in kivy file

class MyRoot(BoxLayout):
    def __init__(self):
        super().__init__() 




class mycal(App):
    def build(self):
        return MyRoot()



cal = mycal()

cal.run()
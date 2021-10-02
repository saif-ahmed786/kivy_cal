from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy



#class for design ,will be in kivy file

class MyRoot(BoxLayout):
    def __init__(self):
        super().__init__() 
    def calc_symbol(self,symbol):
        self.calc_field.text += symbol




class AndCalculator(App):
    def build(self):
        return MyRoot()



andcalculator = AndCalculator()

andcalculator.run()
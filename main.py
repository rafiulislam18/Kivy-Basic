from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        label1 = Label(text='Hello World')
        label2 = Label(text='Button 2')
        layout.add_widget(label1)
        layout.add_widget(label2)

        return layout
    
if __name__ == '__main__':
    MyApp().run()
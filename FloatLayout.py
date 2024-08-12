# FloatLayout in Kivy
# FloatLayout is a layout that allows widgets to be placed anywhere on the screen.

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        
        # Relative positioning
        label1 = Label(text='hello', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        # Absolute positioning
        button = Button(text='click', size=(50,50), size_hint=(None,None), pos=(100,200))

        layout.add_widget(label1)
        layout.add_widget(button)

        return layout
    
if __name__ == '__main__':
    MyApp().run()
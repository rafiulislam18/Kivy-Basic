# on_press Event in Kivy
# on_press Event is a method that is called when a button is pressed.

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        # New Label button
        self.button = Button(text='New Label')
        self.button.bind(on_press=self.new_label)
        # Remove Label button
        self.button2 = Button(text='Remove Label')
        self.button2.bind(on_press=self.remove_label)

        self.add_widget(self.button)
        self.add_widget(self.button2)
    
    # New Label function
    def new_label(self, button):
        self.label = Label(text='new label')
        self.add_widget(self.label)

    # Remove Label function
    def remove_label(self, button):
        self.remove_widget(self.label)
            

class MyApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    MyApp().run()
# Kivy - KV File
# .kv files are used to define the layout of the app.

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyBox(Widget):
    myInput = ObjectProperty(None)

    def printOut(self):
        print(self.myInput.text)


class KvBasicApp(App):
    def build(self):
        return MyBox()
    
if __name__ == '__main__':
    KvBasicApp().run()
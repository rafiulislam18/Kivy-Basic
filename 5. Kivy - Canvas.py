from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

class MyWidget(Widget):
    def on_touch_down(self, touch):
        self.canvas.add(Rectangle(pos=(touch.x, touch.y), size=(50, 50)))

class MyApp(App):
    def build(self):
        return MyWidget()
    
if __name__ == '__main__':
    MyApp().run()
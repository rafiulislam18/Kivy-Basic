# Kivy - Image
# The Image widget is used to display an image.

from kivy.app import App
from kivy.uix.image import Image    # , AsyncImage [ for async image ]

# the class below is for async image
# class MyImage(AsyncImage):
#     pass

class MyImage(Image):
    pass

class KvImageApp(App):
    def build(self):
        # we can also use the Image class directly as shown in the next line
        # return Image(source='image.png')
        return MyImage()

KvImageApp().run()
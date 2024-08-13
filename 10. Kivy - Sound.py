# Kivy - Sound
# The Sound class is used to play sound.

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class SoundPlayer(BoxLayout):

    def play_sound(self):
        sound = SoundLoader.load('audio.mp3')
        if sound:
            sound.volume = 0.2  # Adjusted the volume to 20%
            sound.play()

class KvSoundApp(App):
    def build(self):
        return SoundPlayer()
    
KvSoundApp().run()
import random

from kivy import properties
from kivy.app import App
from kivy.uix.label import Label


class HexMeshApp(App):
    map_location = properties.StringProperty("Untouched")

    def update_press(self, text):
        self.map_location = "Pressed {}".format(text)


class Hex(Label):
    tile_color = properties.ListProperty([0, 1, 0, 0.5])

    def __init__(self, **kwargs):
        super(Hex, self).__init__(**kwargs)
        for hue in range(0, 3):
            self.tile_color[hue] = random.random()


if __name__ == '__main__':
    HexMeshApp().run()

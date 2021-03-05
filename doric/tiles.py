import kivy.utils
from kivy.graphics import Color, Line, Ellipse
from kivy.logger import Logger
from kivy.uix.label import Label
from kivy.vector import Vector

from doric.map import Coordinates
from doric.terrain import Terrain
from passer import Tree


# TODO: Migrate this into a better setup via inheritance or composition of MapTile info.
Terrains = {
    'grass': {
        'color': '#71CD00'
    },
    'hill': {
        'color': '#505355'
    },
    'water': {
        'color': '#5D88F8'
    },
    'sand': {
        'color': '#F9CF29'
    },
    'forest': {
        'color': '#10A71E'
    },
    'space': {
        'color': '#000000'
    },
    'rock': {
        'color': '#A1A5AA'
    },
    'city': {
        'color': '#A1A5AA'
    },
    'ice': {
        'color': '#EEEEEE'
    }
}


class MapTile(Label):
    def __init__(self, row=0, col=0, **kwargs):
        super(MapTile, self).__init__(**kwargs)
        self.coords = Coordinates(row, col)
        self.terrain = Terrain.choose_random_terrain()

        with self.canvas:
            Color(*self.terrain_colour)
            self.tile_background = Ellipse(pos=(self.x, self.y), size=(self.height, self.height), segments=6)

            self.coord_label = Label(
                text=" ",
                center_x=self.center_x,
                center_y=self.center_y)
            if(self.coords.even_r_coordinate_text()=="[0, 0]"):
                self.coord_label = Label(
                text="START",
                    center_x=self.center_x,
                    center_y=self.center_y)            
            elif(self.coords.even_r_coordinate_text()=="[4, 4]"):
                self.coord_label = Label(
                text="FINISH",
                    center_x=self.center_x,
                    center_y=self.center_y)              
            else:
                self.coord_label = Label(
                text=" ",
                center_x=self.center_x,
                center_y=self.center_y)

        self.bind(pos=self.update_positions, size=self.update_positions)

    @property
    def terrain_colour(self):
        hex_colour = Terrains[self.terrain.substrate.name]['color']
        return kivy.utils.get_color_from_hex(hex_colour)
    
    @property
    def next_move(self):
        next = Tree.coordinates(self.coords.even_r_coordinate_text())
        return '{}\n'.format(next)

    @property
    def border_colour(self):
        border_color = '#FFFFFF'
        #border_width = NumericProperty(1)
        return kivy.utils.get_color_from_hex(border_color)
 
    @property
    def hex_radius(self):
        return self.height / 2

    def map_display_text(self):
        return "{}\n{}".format(
            self.coords.even_r_coordinate_text(),self.terrain.description())

    def update_positions(self, instance, value):
        self.tile_background.pos = (self.x, self.y)
        self.tile_background.size = (self.height, self.height)

        self.coord_label.center_x = self.center_x
        self.coord_label.center_y = self.center_y

    def on_touch_down(self, touch):
        if super(MapTile, self).on_touch_down(touch):
            return False

        if not self.collide_with_bounding_circle(touch.x, touch.y):
            return False

        self.parent.parent.game.on_selected_cell(self)
        with self.canvas:
            Color(*self.border_colour)
            self.tile_background = Ellipse(pos=(self.x-4, self.y-4), size=(self.height+8,self.height+8), segments=6)
            Color(*self.terrain_colour)
            self.tile_background = Ellipse(pos=(self.x, self.y), size=(self.height, self.height), segments=6)
            self.coord_label = Label(
                text=" ",
                center_x=self.center_x,
                center_y=self.center_y)
            if(self.coords.even_r_coordinate_text()=="[0, 0]"):
                self.coord_label = Label(
                text="START",
                    center_x=self.center_x,
                    center_y=self.center_y)             
            elif(self.coords.even_r_coordinate_text()=="[4, 4]"):
                self.coord_label = Label(
                text="FINISH",
                    center_x=self.center_x,
                    center_y=self.center_y)              
            else:
                self.coord_label = Label(
                text=" ",
                center_x=self.center_x,
                center_y=self.center_y)
        return True

    def collide_with_bounding_circle(self, coord_x, coord_y):
        # Register if within bounds of circle that the hex is inscribed in.
        dist = Vector(self.center_x, self.center_y).distance((coord_x, coord_y))
        Logger.debug('Distance: ({:.2f}, {:.2f}) -> ({:.2f}, {:.2f})'.format(
            self.center_x, self.center_y, coord_x, coord_y))
        Logger.debug('Distance: {:.2f} / Diff: {:.2f}'.format(dist, dist - self.hex_radius))
        return dist - self.hex_radius <= 0


class SpacerTile(Label):
    def __init__(self):
        super(SpacerTile, self).__init__(size_hint=(0.5, 1))
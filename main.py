from kivy import app, properties
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle , Ellipse , Line
from kivy.logger import Logger
from kivy.uix.label import Label
from kivy.vector import Vector
import kivy.utils
from doric.tiles import MapTile, SpacerTile


class StrategyGame(BoxLayout):
    main_map = properties.ObjectProperty(None)
    status = properties.ObjectProperty(None)
    map_rows = properties.NumericProperty(0)
    map_cols = properties.NumericProperty(0)

    def __init__(self, **kwargs):
        super(StrategyGame, self).__init__(**kwargs)

        for row in range(0, self.map_rows):

            hex_map_row = BoxLayout(orientation='horizontal')

            if row % 2 == 1:
                hex_map_row.add_widget(SpacerTile())

            for col in range(0, self.map_cols):
                map_tile = MapTile(row=row, col=col)
                hex_map_row.add_widget(map_tile)

            if row % 2 == 0:
                hex_map_row.add_widget(SpacerTile())

            self.main_map.add_widget(hex_map_row)
    
    
    
    def on_selected_cell(self, selected_tile, *args):
        self.status.text = selected_tile.map_display_text()
        with self.status.canvas.before:
            Color(*selected_tile.terrain_colour)
            Rectangle(pos=self.status.pos, size=self.status.size)
        
        
        self.status.text = selected_tile.next_move()
        with self.status.canvas.before:
            Color(*selected_tile.terrain_colour)
            Rectangle(pos=self.status.pos, size=self.status.size)
        


        
    
    #def press(self,selection,*args):
    
        #terrain

        

class StrategyGameApp(app.App):
    def build(self):
        return StrategyGame()

if __name__ == '__main__':
    StrategyGameApp().run()
 
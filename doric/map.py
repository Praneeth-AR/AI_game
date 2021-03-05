from math import ceil


class Coordinates(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

        # set the cube coordinates of the hexagon as [x, y, z]
        self.cube_coords = self.even_r_to_cube(self.row, self.col)

    @staticmethod
    def even_r_to_cube(row, col):
        """compute cube coordinates from even-r hex coordinates"""
        x = int(col - ceil(float(row) / 2))
        z = row
        y = - x - z
        return [x, y, z]

    @staticmethod
    def cube_to_even_r(x,y, z):
        row = int(x + ceil(z / 2))
        col = z
        return [row, col]

    @property
    def even_r_coords(self):
        """return even-r coordinates of the hexagon."""
        return self.cube_to_even_r(*self.cube_coords)

    @even_r_coords.setter
    def even_r_coords(self, value):
        self.cube_coords = self.even_r_to_cube(*value)

    def even_r_coordinate_text(self):
        return '{}'.format(self.even_r_coords)
        

    def cube_coordinate_text(self):
        return '{!r}'.format(self.cube_coords)

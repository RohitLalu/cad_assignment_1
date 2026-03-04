class LineEquation:
    #ax+by=c
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
    
    def slope(self):
        if self.b == 0:
            return int('inf')
        return -self.a / self.b


class block:
    def __init__(self, block_id: int, colour_code: int, height: int, width: int, 
                 left_bottom_coord: tuple, west: LineEquation, south: LineEquation):
        self.block_id = block_id
        self.colour_code = colour_code
        self.height = height
        self.width = width
        self.left_bottom_coord = left_bottom_coord
        self.west = west
        self.south = south

    def area(self):
        return self.height * self.width
    def east(self):
        return LineEquation(self.west.a, self.west.b, self.west.c + self.width)
    def north(self):
        return LineEquation(self.south.a, self.south.b, self.south.c + self.height)
    def left_top_coord(self):
        return (self.left_bottom_coord[0], self.left_bottom_coord[1] + self.height)
    def right_bottom_coord(self):
        return (self.left_bottom_coord[0] + self.width, self.left_bottom_coord[1])
    def right_top_coord(self):
        return (self.left_bottom_coord[0] + self.width, self.left_bottom_coord[1] + self.height)
    

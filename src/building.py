from src.headers import *

class Building:

    # spawning points
    # town hall
    # huts
    # walls
    # cannons
    # each building will have an associated health

    def __init__(self, name, x, point1, point2):
        # setting up the name and dimensions of the village
        self.name = name
        self.hitpoint = x
        self.x_coordinate = point1
        self.y_coordinate = point2

class Canon(Building):
    def __init__(self, name, x, point1, point2, range, damage_value):
        # setting up the name and dimensions of the village
        
        self.range = range
        self.damage_value = damage_value

        Building.__init__(self, name, x, point1, point2)
    
class Wizard_Tower(Building):
    def __init__(self, name, x, point1, point2, range, damage_value):
        
        self.range = range
        self.damage_value = damage_value

        Building.__init__(self, name, x, point1, point2)

class Player:
    def __init__(self, name, first_try, levels_complete):
        self.name = name
        self.inv = Inventory([])
        self.first_try = first_try
        self.levels_complete = levels_complete
        self.position = Position(0,0,0,0)

class Inventory:
    def __init__(self, items):
        self.items = items
        self.position = Position(0,0,0,0)


class Rooms:   
    def __init__(self, lock, enviroment, progress):
        self.lock = lock
        self.enviroment = enviroment
        self.inv = Inventory([])
        self.progress = progress


class Position:
    def __init__(self, north, south, east, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class Condition:
    def __init__(self):
        self.positions = Position(0,0,0,0)
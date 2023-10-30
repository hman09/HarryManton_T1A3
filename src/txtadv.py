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


class Rooms:   
    def __init__(self, lock, condition):
        self.lock = lock
        self.condition = condition
        self.inv = Inventory([])


class Position:
    def __init__(self, north, south, east, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class Condition:
    def __init__(self):
        self.positions = Position()
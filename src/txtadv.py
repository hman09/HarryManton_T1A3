class Player:
    def __init__(self, name, first_try, levels_complete):
        self.name = name
        self.inv = Inventory([])
        self.first_try = first_try
        self.levels_complete = levels_complete

class Inventory:
    def __init__(self, items):
        self.items = items

class Rooms:   
    def __init__(self, lock, condition):
        self.lock = lock
        self.condition = condition
        self.inv = Inventory([])

class Help:
    def __init__(self):
        pass
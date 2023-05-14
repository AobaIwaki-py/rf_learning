from object.object import Object

class Treasure(Object):
    def __init__(self):
        super().__init__()
        
if __name__=='__main__':
    treasure = Treasure()
    print(treasure.name)
    treasure.set_position(1, 2)
    print(treasure.get_position())
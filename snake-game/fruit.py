from random import randint


class Fruit():
    ''' Red square that gets eaten to increase snake size '''

    def __init__(self, rows=20):
        self.rows = rows
        self.new_fruit()

    def is_collide(self, other):
        ''' Checks if fruit collides with snake '''
        return True if self.x == other.x and self.y == other.y else False

    def new_fruit(self):
        ''' Creates a fruit at a new location '''
        self.x = randint(0, self.rows-1)
        self.y = randint(0, self.rows-1)

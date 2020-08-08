class Cube():
    ''' Green square that is one part of the snake '''

    def __init__(self, x, y, dx=0, dy=0, rows=20):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rows = rows

    def move(self):
        ''' Changes cube's x and y positions each frame '''
        if self.dx == -1 and self.x <= 0:                # Off screen to left
            self.x = self.rows - 1
        elif self.dx == 1 and self.x >= self.rows - 1:   # Off screen to right
            self.x = 0
        elif self.dy == -1 and self.y <= 0:              # Off screen upwards
            self.y = self.rows - 1
        elif self.dy == 1 and self.y >= self.rows - 1:   # Off screen downwards
            self.y = 0
        else:
            self.x += self.dx
            self.y += self.dy

        # Added to double-check the work
        if self.x < 0:
            self.x = self.rows - 1
        if self.x > self.rows - 1:
            self.x = 0
        if self.y < 0:
            self.y = self.rows - 1
        if self.y > self.rows - 1:
            self.y = 0

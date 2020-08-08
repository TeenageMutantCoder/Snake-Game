from .cube import Cube


class Snake():
    ''' The snake. Basically a list of green cubes '''

    def __init__(self, body=[], rows=20):
        self.body = body
        self.rows = rows
        self.body.append(Cube(self.rows//2-1, self.rows//2-1, rows=self.rows))
        self.head = self.body[0]
        self.turns = {}

    def extend(self):
        ''' Makes the snake body longer '''
        lastCube = self.body[-1]
        self.body.append(Cube(lastCube.x - lastCube.dx,
                              lastCube.y - lastCube.dy,
                              dx=lastCube.dx, dy=lastCube.dy, rows=self.rows))

    def move(self, direction):
        ''' Moves the snake head, lets body follow '''
        if direction == "up":
            if len(self.body) > 1:
                if (self.body[1].x, self.body[1].y) != (self.head.x,
                                                        self.head.y - 1):
                    self.head.dy = -1
                    self.head.dx = 0
                    self.add_turn()
            else:
                self.head.dy = -1
                self.head.dx = 0

        elif direction == "down":
            if len(self.body) > 1:
                if (self.body[1].x, self.body[1].y) != (self.head.x,
                                                        self.head.y + 1):
                    self.head.dy = 1
                    self.head.dx = 0
                    self.add_turn()
            else:
                self.head.dy = 1
                self.head.dx = 0

        elif direction == "left":
            if len(self.body) > 1:
                if (self.body[1].x, self.body[1].y) != (self.head.x - 1,
                                                        self.head.y):
                    self.head.dx = -1
                    self.head.dy = 0
                    self.add_turn()
            else:
                self.head.dx = -1
                self.head.dy = 0

        elif direction == "right":
            if len(self.body) > 1:
                if (self.body[1].x, self.body[1].y) != (self.head.x + 1,
                                                        self.head.y):
                    self.head.dx = 1
                    self.head.dy = 0
                    self.add_turn()
            else:
                self.head.dx = 1
                self.head.dy = 0

        elif direction == "":
            for cube in self.body:
                cube.move()

        self.move_tail()

    def move_tail(self):
        for index, cube in enumerate(self.body):
            pos = (cube.x, cube.y)
            if pos in self.turns:
                turn = self.turns[pos]
                cube.dx = turn[0]
                cube.dy = turn[1]
                if index == len(self.body) - 1:
                    self.turns.pop(pos)

    def add_turn(self):
        ''' Records change in direction at a x, y position '''
        self.turns[(self.head.x, self.head.y)] = [self.head.dx, self.head.dy]

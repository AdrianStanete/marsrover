class Rover:
    directions = ['N', 'E', 'S', 'W']

    def __init__(self, x=0, y=0, direction='N'):
        self.x = x
        self.y = y

        if direction not in self.directions:
            raise DirectionNotFound("Invalid direction given. Only N,W,E,S valid.")
        self.direction = direction

    def move(self, commands):
        for command in commands:
            if command == 'F':
                if self.direction == 'N':
                    self.y = +1
                if self.direction == 'E':
                    self.x = +1
                if self.direction == 'S':
                    self.y = -1
                if self.direction == 'W':
                    self.x = -1

            if command == 'B':
                if self.direction == 'N':
                    self.y = -1
                if self.direction == 'E':
                    self.x = -1
                if self.direction == 'S':
                    self.y = +1
                if self.direction == 'W':
                    self.x = +1

            if self.x == -1:
                self.x = 5
            if self.x == 6:
                self.x = 0
            if self.y == -1:
                self.y = 5
            if self.y == 6:
                self.y = 0

            if command == 'R':
                index = self.directions.index(self.direction) + 1
                self.direction = self.directions[index]
            if command == 'L':
                index = self.directions.index(self.direction) - 1
                self.direction = self.directions[index]


class DirectionNotFound(Exception):
    pass

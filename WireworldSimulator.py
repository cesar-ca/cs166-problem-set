from itertools import product
from enum import Enum
import itertools

class Color(Enum):
    yellow = '.'    # wire
    blue = 'H'      # head
    red = 't'       # tail

    @staticmethod
    def char_to_color(c):
        if c == '.': return Color.yellow
        if c == 't': return Color.red
        if c == 'H': return Color.blue
        if c == 'b' or c == ' ': return None
        raise Exception('Unknown char: ' + c)


class WireworldSimulator:

    def __init__(self, world):
        self.world = world

        self.dd = list(product([-1, 0, 1], repeat= 2))
        self.dd.remove((0, 0))

        values = world.values()
        points = list(itertools.chain(*values))
        self.size_x = max(points, key=lambda x: x[0])[0] + 1
        self.size_y = max(points, key=lambda x: x[1])[1] + 1

    def state(self):
        return self.world

    def dimensions(self):
        return (self.size_x, self.size_y)

    def step(self):
        new_world = WireworldSimulator.__new_world()

        for x, y in self.world[Color.yellow]:
            n = sum((x+dx, y+dy) in self.world[Color.blue] for dx, dy in self.dd)
            if n == 1 or n == 2:
                color = Color.blue
            else:
                color = Color.yellow
            new_world[color].append((x, y))

        new_world[Color.red] = self.world[Color.blue]       # head -> tail
        new_world[Color.yellow] += self.world[Color.red]    # tail -> conductor

        self.world = new_world
        return self.world

    @staticmethod
    def __new_world():
        world = dict()
        for color in Color:
            world[color] = []
        return world

    @staticmethod
    def load(file_name):
        world = WireworldSimulator.__new_world()

        with open(file_name, 'r') as f:
            for line_number, line in enumerate(f):
                line = line.rstrip('\n\r ')
                for char_index, c in enumerate(line):
                    color = Color.char_to_color(c)
                    if color != None:
                        world[color].append((char_index, line_number))

        print(world)
        return world
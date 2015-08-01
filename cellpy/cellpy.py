__author__ = 'Victor'

from random import randint

class Cell(object):
    """Represents a single cell on the grid"""
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def neighbours(self, include_self=False):
        """returns a list of all neighbouring cells"""
        neighbours = []
        #TODO - implement
        if include_self:
            neighbours.append(self)
        return neighbours

    def occupants(self):
        """returns a list of all occupants of this cell"""
        pass


class Grid(object):
    """Represents the whole grid"""
    def __init__(self, width=32, height=24):
        self.height = height
        self.width = width
        self.cells = {}
        for x in range(width):
            for y in range(height):
                self.cells[x, y] = Cell((x, y))

    def get_cell_at(self, coordinates):
        return self.cells[coordinates]


class Agent(object):
    """Base class for an agent

    Attributes:
        grid (Grid): the Grid object this agent lives on
        coordinates (Tuple[int]): current coordinates of the agent on grid
        direction (int): direction the agent is pointing, in degrees
    """
    def __init__(self, grid, start_coordinates=None, start_direction=None):
        if start_coordinates:
            self.coordinates = start_coordinates
        else:
            self.coordinates = (randint(0, grid.width), randint(0, grid.height))
        if start_direction:
            self.direction = start_direction
        else:
            self.direction = randint(0, 359)

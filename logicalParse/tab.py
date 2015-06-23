from logicalParse.case import Case
from logicalParse.text import Text
from server import Grid

__author__ = 'claraberard'


class Tab(Grid):
    tab = {}

    def __init__(self, grid):
        Grid.__init__(self, grid)
        self.tab = {}

    def add_tab(self, case):
        """
        :type case: Case
        """
        self.tab[(case.coordinates[0], case.coordinates[1])] = case

    def get_inside(self, coordinates):
        return self.get_cell(coordinates[0], coordinates[1])

    def make_a_case(self, coordinates):
        return Case(coordinates[0], coordinates[1], Text(self.get_inside(coordinates)))

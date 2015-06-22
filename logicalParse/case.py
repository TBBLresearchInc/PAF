from logicalParse.coordinates import Coordinates
from server import GridPos
from server import Tab



__author__ = 'claraberard'


class Case(Tab):


    def getText(self):
        return self.get_cell(self.pos[0],self.pos[1])

    def eval(self):
        if self.get_Text[0] == "&" :





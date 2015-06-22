from logicalParse.coordinates import Coordinates
from logicalParse.text import Text
from server import Grid



__author__ = 'claraberard'


class Case(Grid):

    coordinates = Coordinates(0,0)
    nature = 0

    def __init__(self, row, column):
        self.coordinates[0]=row
        self.coordinates[1]=column
        self.nature = 0

    def set_nature(self,nature):
        self.nature=nature

    def get_inside(self):
        return self.get_cell(self.coordinates[0], self.coordinates[1])

    def get_text_in_a_case(self):
       t = Text(self.get_inside())

    def is_a_formula(self):
        if self.get_inside()[0] == "=" :
            self.set_nature(4)
            return True
        else :
            self.set_nature(1)
            return False






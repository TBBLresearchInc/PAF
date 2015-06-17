from logicalParse.coordinates import Coordinates

__author__ = 'claraberard'


class Case:
    coordinates = Coordinates(1, 'A')
    sentence = ""

    def __init__(self, coordinates, sentence):
        self.coordinates = coordinates
        self.sentence = sentence

    def whatCase(self):
        print( case.coordinates.getColumn() + str(case.coordinates.getLine()))

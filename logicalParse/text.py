from logicalParse.coordinates import Coordinates
from logicalParse.case import Case

__author__ = 'claraberard'

class Text:

    sentence = ""

    def __init__(self, sentence, coordinates):
        self.sentence = sentence
        self.coordinates = coordinates


from logicalParse.coordinates import Coordinates
from logicalParse.case import Case

'classe qui va etre utilisée lorsque le contenu dune case est  du texte (style prédicat) '

__author__ = 'claraberard'


class Text:

    sentence = ""

    def __init__(self, sentence):
        self.sentence = sentence

    def __init__(self, sentence, coordinates):
        self.sentence = sentence
        self.coordinates = coordinates


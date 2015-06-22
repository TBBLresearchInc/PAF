from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Predicate(Text):

    weight = Weight(1)

    def __init__(self, weight):
        if weight != 1 | weight != -1:
            print("ce prédicat est un attribut, attention à la definition")
        else:
            self.weight = weight


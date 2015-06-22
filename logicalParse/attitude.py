from logicalParse.coordinates import Coordinates
from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Attitude():

    coordinates = Coordinates(0,'A')
    predicate = Predicate("",Coordinates(0, 'A'))
    weight = Weight(0)

    def __init__(self, coordinates, predicate, weight):
        self.coordinates = coordinates
        self.predicate = predicate
        self.weight = weight

from logicalParse.coordinates import Coordinates
from logicalParse.formula import Formula
from logicalParse.predicate import Predicate

__author__ = 'claraberard'

class Case():

    #une case correspond a une case du tableau. Elle a comme attribut ses coordonnees et un text

    coordinates = Coordinates(0,0)
    sentence = ""
    ref_predicate = coordinates  #utile lorsquon definit une attribut a partir dun predicat pour connaitre les coordonnees du predicat
    ref_non = coordinates       #lorsque la case definit le predicat contraire on obtient grace a cette reference la case ou est ecrit le predicat contraire

    def __init__(self, coordinates, sentence):
        self.coordinates = coordinates
        self.sentence = sentence
        self.ref_predicate = self.coordinates
        self.ref_non = self.coordinates

    def get_weight(self):
        return self.sentence.have_weight()

    def is_in_relation(self):
        return (self.ref_predicate != self.coordinates) | (self.ref_non != self.coordinates)

    def case_solve(self, tab):
        if self.sentence[0] == "=":
            Formula(self.sentence).fsolve(tab, self)
        else:
            tab[self.coordinates] = Predicate(self.sentence, 1)





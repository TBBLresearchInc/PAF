from logicalParse.formula import Formula
from logicalParse.predicate import Predicate
from logicalParse.text import Text

__author__ = 'claraberard'

class Case():

    #une case correspond a une case du tableau. Elle a comme attribut ses coordonnees et un text

    coordinates = (0,0)
    text = Text("")
    ref_predicate = coordinates  #utile lorsquon definit une attribut a partir dun predicat pour connaitre les coordonnees du predicat
    ref_non = coordinates       #lorsque la case definit le predicat contraire on obtient grace a cette reference la case ou est ecrit le predicat contraire

    def __init__(self, coordinates, text):
        self.coordinates = coordinates
        self.text = text
        self.ref_predicate = (-1, -1)
        self.ref_non = (-1, -1)

    def is_in_relation(self):
        return (self.ref_predicate != self.coordinates) | (self.ref_non != self.coordinates)

    def case_solve(self, tabu):
        print self.text
        if self.text.sentence[0] == "=":
            Formula(self.text.sentence[1:]).fsolve(tabu, self.coordinates)
        else:
            tabu.tab[self.coordinates] = Predicate(self.text.sentence, 1)
            print(tabu.tab[self.coordinates].tostring())





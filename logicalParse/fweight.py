from logicalParse.attitude import Attitude
from logicalParse.weight import Weight

__author__ = 'claraberard'


class FWeight():  #pour resoudre une formule du type $90A2

    weight = Weight(0)
    coordinates = (0, 0)

    def __init__(self, coordinates, weight):
        self.coordinates = coordinates
        self.weight = weight

    def weight_solve(self, tab, coordinates):
        s = tab.tab[self.coordinates].text.sentence # on recupere le predicat dans la case appelee
        a = Attitude(s, self.weight, self.coordinates,1)  #on en cree une attitude avec ce predicat
        tab.tab[coordinates].text = a               # mise a jour de la case
        tab.tab[coordinates].ref_predicate = self.coordinates #mise a jour de la reference sur predicat de la case contenant l attribut
        tab.tab[self.coordinates].ref_predicate = coordinates #mise a jour de la reference sur predicat de la case contenant le predicat

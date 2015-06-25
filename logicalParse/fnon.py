from logicalParse.attitude import Attitude
from logicalParse.predicate import Predicate

__author__ = 'claraberard'

#cette classe sert a definir les predicats opposes donnes par l'utilisateur par une formule du type =NONB2 ecrit dans C3 par exemple

class FNon():
    coordinates = (0, 0)  #pour definir les coordonnees de la case reference ecrite dans la formule (dans le cas de l'exemple nous aurions (2,2) qui correspond de B2

    def __init__(self, coordinates):
        self.coordinates=coordinates

    #en donnant en attribut tab et coordonnates de la case dans laquelle est ecrite la formule, on cree dans cette meme case le predicat oppose (dans le cas de l'exemple (3,3) qui correspond a C3)
    def non_solve(self, tab, coordinates):
        """
        :rtype : object
        """
        t = tab.tab[self.coordinates].text.sentence #on prend la phrase ecrite dans B2
        tab.tab[coordinates].text = Predicate(t, -1) #on cree le predicat associe contraire dans C3
        a = Predicate(t, 1)
        tab.tab[self.coordinates].text = a #on met a jour dans la case B2
        tab.tab[coordinates].ref_non = self.coordinates
        tab.tab[self.coordinates].ref_non = coordinates
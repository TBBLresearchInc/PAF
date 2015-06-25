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
        if self.text.sentence[0] == "=":   #test si on est dans le cas d'une formule
            if self.text.sentence[0:2]== "=$": #dans le cas d'une formule creant une attitude
                bin=True
            else:
                bin =False

            Formula(self.text.sentence[1:]).fsolve(tabu, self.coordinates) #quelque soit le cas il faut resoudre la formule

            if bin: #si cas formule creant un attribut
                tabu.attitude_caselist.append(tabu.tab[self.coordinates]) #si de plus on a une formule creant une attitude il faut ajouter la case dans la liste des attributs du tableau

        else: #pas de signe egal
            tabu.tab[self.coordinates] = Case(self.coordinates,Predicate(self.text.sentence, 1)) #si la case ne commence pas par le signe = il faut convertir le text en predicat
            tabu.predicate_caselist.append(tabu.tab[self.coordinates]) #puis il faut ajouter la case dans la liste des predicats du tableau

    def tostring(self):
        return "case : "+str(self.coordinates)+", "+self.text.sentence



from logicalParse.weight import Weight
from logicalParse.predicate import Predicate
__author__ = 'Yannick'



class PredicateRow:

    row=[]
    def __init__(self,row):
        self.row=row


    '''prend des coordonnees et renvoie le predicat qui les detient'''

    def sentence_to_predicate(self,sentence):
        for predicate in self.row:
            assert isinstance(predicate, Predicate)
            if predicate.sentence == sentence:
                return predicate


    '''sert a generer l'ensemble de toutes les propositions : a une liste de predicats (qui represente un entier n en binaire),
    on renvoie n+1 en binaire'''
    def bplus(self):
        i=0
        while (self.row[i]).yesno == 1:
                self.row[i].yesno = 0
                i += 1
        self.row[i].yesno=(1)


    '''renvoie le poids total d'une liste de predicats en fonction des attitudes representees'''

    def totalweight(self, attrow):
        weight=Weight(0)
        for i in range(0,len(self.row)):
            weight.value += attrow.row[i].weight.value * self.row[i].yesno
        return weight


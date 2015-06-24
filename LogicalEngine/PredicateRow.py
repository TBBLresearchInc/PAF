from LogicalEngine.RuleRow import RuleRow
from logicalParse.weight import Weight
from logicalParse.predicate import Predicate
__author__ = 'Yannick'



class PredicateRow:

    row=[]
    def __init__(self,row):
        self.row=row

    def tostring(self):
        s="predicaterow :("
        for predicate in self.row:
            s+= predicate.tostring()+", "
        return s+")"

    '''prend des coordonnees et renvoie le predicat qui les detient'''

    def sentence_to_predicate(self,sentence):
        for predicate in self.row:
            if predicate.sentence == sentence:
                return predicate

    def coordinate_to_predicate(self,coordinate):
        for predicate in self.row:
            if predicate.coordinate == coordinate :
                return predicate

    '''sert a generer l'ensemble de toutes les propositions : a une liste de predicats (qui represente un entier n en binaire),
    on renvoie n+1 en binaire'''
    def bplus(self):
        res=PredicateRow([Predicate(self.row[i].sentence,self.row[i].yesno) for i in range(len(self.row))])
        i=0
        while (self.row[i]).yesno == 1:
                res.row[i].yesno = -1
                i += 1
        res.row[i].yesno=(1)
        return res


    '''renvoie le poids total d'une liste de predicats en fonction des attitudes representees'''

    def totalweight(self, attrow):
        weight=Weight(0)
        for i in range(0,len(self.row)):
            weight.value += attrow.row[i].weight.value * self.row[i].yesno
        return weight

    '''prend une liste de predicats et renvoie la liste des regles qu'elle ne respecte pas'''
    def check(self, rulerow):
        res = RuleRow([])
        for i in range(0, len(rulerow.row)):
            rule=rulerow.row[i]
            for j in range(0, len(rule.list)):
                predicate= rule.list[j]
                predicatefromrow = self.coordinate_to_predicate(predicate.coordinaten )
                if predicate.yesno != predicatefromrow.yesno:
                    break
                elif j==(len(rule.list)-1):
                    res.row.append(rule)

        return res

    def issatisfied(self,rulerow):
        if self.check(rulerow).row == []:
            return True
        else:
            return False
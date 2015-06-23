from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from LogicalEngine.Solutions import Solutions
from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'Yannick'




class AttitudeRow:
    row=[]

    def __init__(self,row):
        self.row=row




    '''prend une liste d'attitudes et renvoie la liste des predicats correspondants'''
    def attrow_to_predrow(self):
        res= PredicateRow([])
        for attitude in self.row:
            res.row.append(attitude.predicate)
        return res


    '''prend une liste d'attitudes et renvoie la liste des regles qu'elle ne respecte pas'''
    def check(self, rulerow):
        predrow=self.attrow_to_predrow()
        res = RuleRow([])
        for i in range(0, len(rulerow.row)):
            rule=rulerow.row[i]
            for j in range(0, len(rule.list)):
                predicate= rule.list[j]
                predicatefromattitude = predrow.sentence_to_predicate(predicate.sentence)
                if predicate.yesno != 1:
                    break
                elif j==(len(rule.list)-1):
                    res.row.append(rule)

        return res





    '''appelee si les attitudes de l'utilisateur sont incompatibles, renvoie
    un PredicateRow respectant les regles'''



    def bestsolve(self,rulerow):
        msol=Solutions([[]])
        predlist=self.attrow_to_predrow()
        predrow=PredicateRow([ (predlist.row[i].sentence,0) for i in range(len(self.row))])

        wmax=Weight(0)

        for i in range(0,(2**(len(self.row)))-1):
            if self.issatisfied(rulerow):
                wtot=predrow.totalweight(self)
                msol.insert(wtot,wmax,predrow)
            print predrow
            predrow.bplus()
        return msol.matrix[0]



    '''la combinaison d'attitudes est-elle autorisee par les regles?'''
    def issatisfied(self,rulerow):
        if self.check(rulerow) == []:
            return True
        else:
            return False


    '''si attitudes insatisfaites : renvoie les regles qui posent probleme sous forme d'une liste de coordonnees'''
    def unsatisfiedrules(self,rulerow):
        badrules=RuleRow([])
        if not(self.issatisfied(rulerow)):
            badrules.row.append(self.check(rulerow))

        coordrow={}
        coordrow['rouge']=[]
        for rule in badrules.row:
            coordrow['rouge'].append(rule.coordinate)

        return coordrow



    '''renvoie les attitudes insatisfaites par la solution optimisee
    sous la forme d'un dictionnaire contenant 2 listes dict['vert']et dict['rouge'] '''

    def unsatisfiedattitudes(self,firstattituderow):
        color = {}
        color['vert']=[]
        color['rouge']=[]
        optimizedpredicaterow=self.attrow_to_predrow()
        firstpredicaterow= firstattituderow.attrow_to_predrow()

        for i in range(0,len(self.row)):
            if optimizedpredicaterow.row[i].weight.value==firstpredicaterow[i].weight.value:
                color['green'].append(optimizedpredicaterow.row[i].coordinate)
            else:
                color['red'].append(optimizedpredicaterow.row[i].coordinate)

        return color
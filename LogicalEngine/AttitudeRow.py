from LogicalEngine.BinaryRow import BinaryRow
from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from LogicalEngine.Solutions import Solution

__author__ = 'Yannick'




class AttitudeRow:

    def __init__(self,row):
        self.row=row

    def attrow_to_predrow(self):
        res= PredicateRow([])
        for attitude in self.row:
            res.row.append(attitude.predicate())
        return res

    def check(self, ruleRow):
        res= RuleRow([])
        for i in range(0,len(ruleRow.row)):
            rule=ruleRow[i]
            for j in range(0, len(rule)):
                predicate= rule[j]
                if (predicate.weight != predicate.coordinates.getPredicate(predicate.coordinates,self).weight):
                    break
                elif(j==len(rule)-1):
                    res.row.append(rule)

        return res





    '''appelee si les attitudes de l'utilisateur sont incompatibles, renvoie
    un PredicateRow respectant les regles'''

    def bestsolve(self,rulerow):
        msol=Solution([[]])
        binrow=BinaryRow([ (0) for i in range(len(self.row))])
        predlist= self.attrow_to_predrow()

        predrow=binrow.row.brow_to_predrow(predlist)
        wmax=predlist.row[0].weight

        for i in range(0,2^(len(self.row))):
            if self.issatisfied(rulerow):
                wtot=predrow.weight
                msol.insert(wtot,wmax,binrow)

            binrow.bplus()
        return (msol.matrix[0])



    '''la combinaison d'attitudes est-elle autorisee par les regles?'''
    def issatisfied(self,rulerow):
        if self.check(rulerow) == []:
            return True
        else:
            return False


    '''si attitudes insatisfaites : renvoie les regles qui posent probleme'''
    def unsatisfiedrules(self,rulerow):
        res=RuleRow([])
        if not(self.issatisfied(rulerow)):
            res.row.append(self.check(rulerow))

        return res



    '''renvoie les attitudes insatisfaites par la solution optimisee
    sous la forme d'un dictionnaire contenant 2 listes dict['vert']et dict['rouge'] '''

    def unsatisfiedattitudes(self,firstattituderow):
        color = {}
        color['vert']=[]
        color['rouge']=[]
        optimizedpredicaterow=self.attrow_to_predrow()
        firstpredicaterow= firstattituderow.attrow_to_predrow()

        for i in range(0,len(self.row)):
            if optimizedpredicaterow.row[i].weight==firstpredicaterow[i].weight:
                color['green'].append(optimizedpredicaterow.row[i].coordinate)
            else:
                color['red'].append(optimizedpredicaterow.row[i].coordinate)

        return color
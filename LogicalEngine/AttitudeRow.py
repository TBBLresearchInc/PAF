from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from LogicalEngine.Solutions import Solutions
from logicalParse.attitude import Attitude
from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'Yannick'




class AttitudeRow:
    row=[]

    def __init__(self,row):
        self.row=row


    def tostring(self):
        s="attituderow :("
        for attitude in self.row:
            s+= attitude.tostring()+", "
        return s+")"

    '''prend une liste d'attitudes et renvoie la liste des predicats correspondants'''
    def attrow_to_predrow(self):
        """

        :rtype : PredicateRow
        """
        res = PredicateRow([])

        for attitude in self.row:
            assert isinstance(attitude,Attitude)
            if attitude.weight.value < 0:
                res.row.append(Predicate(attitude.sentence,-attitude.yesno))
            else:
                res.row.append(Predicate(attitude.sentence,attitude.yesno))


        return res







    '''appelee si les attitudes de l'utilisateur sont incompatibles, renvoie
    un PredicateRow respectant les regles'''


    def bestsolve(self,rulerow):
        msol=Solutions([[]])
        predlist=self.attrow_to_predrow()
        predrow=PredicateRow([Predicate(predlist.row[i].sentence,-1) for i in range(len(self.row))])
        wmax=predrow.totalweight(self)

        for i in range(0,(2**(len(self.row)))-1):
            if predrow.issatisfied(rulerow):
                wtot=predrow.totalweight(self)
                msol.insert(wtot,wmax,predrow)
            predrow=predrow.bplus()
        return msol.matrix[0]



    '''la combinaison d'attitudes est-elle autorisee par les regles?'''
    def issatisfiable(self,rulerow):
        return self.attrow_to_predrow().issatisfied(rulerow)


    '''si attitudes insatisfaites : renvoie les regles qui posent probleme sous forme d'une liste de coordonnees'''
    def unsatisfiedrules(self,rulerow):
        badrules=RuleRow([])

        for rule in self.attrow_to_predrow().check(rulerow).row:
            badrules.row.append(rule)

        return badrules



    '''renvoie les attitudes insatisfaites par la solution optimisee
    sous la forme d'un dictionnaire contenant 2 listes dict['vert']et dict['rouge'] '''

    def unsatisfiedattitudes(self,firstattituderow):
        color = {}
        color['vert']=[]
        color['rouge']=[]
        optimizedpredicaterow=self.attrow_to_predrow()
        firstpredicaterow= firstattituderow.attrow_to_predrow()

        for i in range(0,len(self.row)):
            if optimizedpredicaterow.row[i].yesno == firstpredicaterow[i].yesno:
                color['green'].append(optimizedpredicaterow.row[i])
            else:
                color['red'].append(optimizedpredicaterow.row[i])

        return color
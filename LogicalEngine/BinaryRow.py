from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'Yannick'


class BinaryRow:

    def __init__(self,row):
        self.row=row

    def bplus(self):
        n = len(self.row)
        i=0
        while(self.row[i]==(1)):
                self.row[i]=(0)
                i+=1
        self.row[i]=(1)

    def brow_to_predrow(self, predlist):
        predRow = []
        for i in range(0,len(predlist)):
            if (self.row[i]==0):
                pred=predlist[i]
    '''              predRow.append(Predicate(pred.sentence, pred.coordinates,Weight(-1)))
            else:
                predRow.append(Predicate(pred.sentence, pred.coordinates,Weight(1)))
    '''

    def totalweight(self, attRow):
        weight=0
        for i in range(0,len(self.row)):
            weight+= attRow[i].weight*self.row[i]
        return weight

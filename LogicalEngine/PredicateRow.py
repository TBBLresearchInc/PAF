__author__ = 'Yannick'


class PredicateRow:

    def __init__(self,row):
        self.row=row

    def predrow_to_binrow(self):
        binRow=[]
        for pred in self.row:
            if (pred.weight==1):
                binRow.append(1)
            else:
                binRow.append(0)

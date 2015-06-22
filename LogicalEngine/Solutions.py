__author__ = 'Yannick'


class Solution:

    def __init__(self,matrix):
        self.matrix=matrix

    def insert(self, wtot, wmax, binRow):
        if (wtot==wmax):
            self.matrix.append(binRow.bRow_to_predRow(binRow))
        elif(wtot>wmax):
            self.matrix=[[]]
            self.matrix.append(binRow)
            wmax=wtot

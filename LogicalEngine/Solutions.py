__author__ = 'Yannick'


class Solutions:

    def __init__(self,matrix):
        self.matrix=matrix

    '''prend un ensemble de solution et insere une liste binaire ou non en fonction du poids total
    de la liste de predicats correspondant'''
    def insert(self, wtot, wmax, predrow):
        if wtot.value == wmax.value:
            self.matrix.append(predrow)
        elif wtot.value>wmax.value:
            self.matrix=[[]]
            self.matrix.append(predrow)
            wmax.value=wtot.value


__author__ = 'claraberard'

#cette classe permet de prendre en entree des coordonnees ecrites par l'utilisateur du type A2 a des coordonnees simples (1,2)
class Coordinates_tab:

    row = 0
    column = 'A'

    def __init__(self, row, column):
        self.column = column
        self.row = row

    #pour faire la conversion
    def coordinates_to_int(self):
        return (self.row, (ord(self.column[0]))-64)

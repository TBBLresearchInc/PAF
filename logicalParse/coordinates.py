__author__ = 'claraberard'
"donne les coordonnées de la classe"

class Coordinates:
    "classe des coordonnées"
    line = 0
    column = 'A'

    def __init__(self, line, column):
        "constructeur"
        self.line = line
        self.column = column

    def setLine(self, newline):
        "changer la ligne"
        self.line = newline

    def setColumn(self, newcolumn):
        "changer la colonne"
        self.column = newcolumn

    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column



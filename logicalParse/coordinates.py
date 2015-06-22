__author__ = 'claraberard'

class Coordinates:

    line = 0
    column = 0

    def __init__(self, line, column):
        self.line = line
        self.column = column

    def setLine(self, newline):
        self.line = newline

    def setColumn(self, newcolumn):
        self.column = newcolumn

    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column

    def toString(self):
        return '('+ str(self.line) + ',' + str(self.column) + ')'









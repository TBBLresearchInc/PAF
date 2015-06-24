__author__ = 'claraberard'

class Coordinates_tab:

    row = 0
    column = 'A'

    def __init__(self, row, column):
        self.column = column
        self.row = row

    def coordinates_to_int(self):
        return (self.row, (ord(self.column[0]))-64)

__author__ = 'claraberard'

class tab:

    tab = {}

    def __init__(self):
        self.tab={}

    def add_tab(self, coordinates, text):
        tab[(coordinates[0],coordinates[1])] = text



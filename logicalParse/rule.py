__author__ = 'claraberard'


class Rule:

    list = []

    def __init__(self, list):
        self.list = list

    def add_incompatibility(self, tab, coordinates):
        self.list.append(tab[coordinates])













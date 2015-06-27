__author__ = 'claraberard'

class FRule:    #attribut d un tableau qui donne toutes les listes ecrites dans le tableau

    list = []

    def __init__(self, list):
        self.list = list

    def __addRule__(self, rule):
        self.list.append(rule)
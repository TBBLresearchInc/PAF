from grid import Grid
from logicalParse import Coordinates
from logicalParse.case import Case
from logicalParse.text import Text

__author__ = 'claraberard'


class Tab():
    # dictionnaire de case (a un attribut coordonnees associe la case correspondante)

    tab = {}
    rule_list = []

    def __init__(self, tab, rule_list):
        self.tab = tab
        self.rule_list = rule_list

    #pour ajouter une case dans le dictionnaire
    def add_tab(self, case):
        """
        :type case: Case
        """
        self.tab[case.coordinates] = case

    #pour remplir le dictionnaire a partir du grid fourni par Quentin
    def fill_tab(self, grid):
        for i in range(1, len(grid)):
            #on parcourt l'ensemble du dictionnaire de quentin et on ajoute l element sous forme de case
            assert isinstance(grid, Grid)
            row = grid.pos.getRow()
            column = grid.pos.getColumn()
            coordinates = Coordinates(row, column)
            text = Text(grid.get_cell(row, column))
            self.add_tab(Case(coordinates, text))

    #pour recuperer le Text de la case
    def get_inside(self, coordinates):
        assert isinstance(coordinates, Coordinates)
        return self.tab[coordinates].text

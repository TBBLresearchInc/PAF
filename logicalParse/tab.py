from grid import Grid
from logicalParse import Coordinates
from logicalParse.case import Case

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
        """

        :type grid: Grid
        """
        for i in range(0, len(grid.grid)):
            #on parcourt l'ensemble du dictionnaire de quentin et on ajoute l element sous forme de case
            row = grid.pos.getRow()
            column = grid.pos.getColumn()
            coordinates = Coordinates(row, column)
            sentence = grid.get_cell(row, column)
            self.add_tab(Case(coordinates, sentence))

    #pour recuperer le Text de la case
    def get_inside(self, coordinates):
        assert isinstance(coordinates, Coordinates)
        return self.tab[coordinates].text

    def solve(self):
        for case in self.tab:
            case.case_solve(self)

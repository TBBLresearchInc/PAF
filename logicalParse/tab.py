from LogicalEngine.AttitudeRow import AttitudeRow
from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from grid import Grid
from logicalParse.case import Case
from logicalParse.predicate import Predicate

__author__ = 'claraberard'


class Tab():
    # dictionnaire de case (a un attribut coordonnees associe la case correspondante)

    tab = {}
    predicate_caselist=[]
    attitude_caselist=[]
    rule_list = RuleRow([])

    def __init__(self, tab,rule_list, predicate_caselist, attitude_caselist):
        self.predicate_caselist=predicate_caselist
        self.attitude_caselist=attitude_caselist
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
            coordinates = (row, column)
            sentence = grid.get_cell(row, column)
            self.add_tab(Case(coordinates, sentence))

    #pour recuperer le Text de la case
    def get_inside(self, coordinates):
        return self.tab[coordinates].text


    "prend un tableau tab et le convertit en un tableau. Les cases de predicats se voient attribues un predicat en attribut." \
    "Les regles sont ajoutees a l'attribut rule_list de tab"
    def solve(self):
        for coord in self.tab:
            if self.tab[coord].text.sentence[0] != "=":
                self.tab[coord].case_solve(self)

        for coord in self.tab:
            if self.tab[coord].text.sentence[0:4] == "=NON":
                self.tab[coord].case_solve(self)

        for coord in self.tab:
            if self.tab[coord].text.sentence[0:2] == "=$":
                self.tab[coord].case_solve(self)

        for coord in self.tab:

            if (self.tab[coord].text.sentence[0] == "=") & (self.tab[coord].text.sentence[0:4] != "=NON") & (self.tab[coord].text.sentence[0:2] != "=$"):
                self.tab[coord].case_solve(self)

    "prend un tableau, convertit sa liste de case contenue dans tab et renvoie la liste des predicats contenus"
    def get_predrow(self):
        res=PredicateRow([])
        for case in self.predicate_caselist:
            res.row.append(case.text)
        return res

    def get_attrow(self):
        res=AttitudeRow([])
        for case in self.attitude_caselist:
                res.row.append(case.text)
        return res

    def clash(self):
        self.solve()
        attrow=self.get_attrow()
        rulerow=self.rule_list

        badrules=attrow.unsatisfiedrules(rulerow)
        res={}
        res["cells"]=[]
        for rule in rulerow.row:
                print rule.tostring()
                (a,b)=rule.coordinates
                cell={}
                cell["row"]=a
                cell["column"]=b
                if badrules.row.__contains__(rule):
                    cell["result"]="error"
                else:
                    cell["result"]="valid"
                res["cells"].append(cell)
        return res

    print


    def optimize(self):
        self.solve()
        attrow=self.get_attrow()
        rulerow=self.rule_list

        predrow= attrow.bestsolve(rulerow)

        res={}
        res["cells"]=[]

        for pred in predrow.row:
            (a,b)=pred.get_coordinates()
            cell={}
            cell["row"]=a
            cell["column"]=b
            if pred.yesno==1:
                cell["result"]="valid"
            else:
                cell["result"]="error"
            res["cells"].append(cell)
        return res
# coding=utf-8
from LogicalEngine.AttitudeRow import AttitudeRow
from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from logicalParse.case import Case
from logicalParse.tab import Tab
from logicalParse.text import Text

__author__ = 'Quentin Leroy'
# Quentin Leroy
# quentin.leroy@telecom-paristech.fr

""" Cette application web.py fait l'interface entre les inputs du client dans les cellules du tableau
 et l'intelligence de calcul du tableur (interpretation des inputs en terme d'expressions logiques puis
 divers calculs logiques), l'application renvoie aussi aux clients les resultats de la partie calcul
 (il y a t il des cases a colorier ? En quelles couleurs ? Il y a t il des cellules a completer-modifier ?
  Il y a t il un message a donner a l utilisateur ?)"""

import web, json, os.path


from grid import Grid

urls = ("/(.*)/", "Index",
        "/py/json", "Json",
        "/py/action", "Action")

class Index:
    def GET(self, name):
        if not name:
            name = "World"
        return "Home Page"

class Json:
    def GET(self):
        user_data = web.input(id = "no data")
        return user_data.id

    def POST(self):
        data = web.input() #retrieve input data from client

        content = str(data["content"])
        row = int(data["row"])
        column = int(data["column"])
        grid.update(row, column, content)

        tab_serv = Tab({}, RuleRow([]), [], [])



        for i in range(0, grid.nb_of_cells()):
            cur_coords = grid.get_coords(i)

            case_serv = Case(cur_coords, Text(grid.get_cell(cur_coords[0], cur_coords[1])))

            tab_serv.add_tab(case_serv)

        ####################################
        # data process from logical engine #
        ####################################

        # En fonction des calculs effectues, il faudra appeler set_color(row, column)

        # print(str(grid.get_colors()))

        print(str(json.dumps(grid.get_colors())))
        return str(json.dumps(grid.get_colors()))  # return colors to fill the cells after some data process (not yet)

class Action:
    def GET(self):
        user_data = web.input(id = "no data")
        return user_data.id

    def POST(self):
        data = web.input() #retrieve input data from client

        if data["action"] == "conflict":
            print(tab_serv.clash())
            return json.dumps(tab_serv.clash())


grid = Grid({})

tab_serv = Tab({}, RuleRow([]), [], [])

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()


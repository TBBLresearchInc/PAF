# coding=utf-8
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
 """

import web, json, os.path

from grid import Grid

urls = ("/(.*)/", "Index",
        "/py/json", "Json",
        "/py/action", "Action")

grid = Grid()

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
        data = web.input() # retrieve input data from client

        content = str(data["content"])
        row = int(data["row"])
        column = int(data["column"])
        grid.update(row, column, content)  # fill the grid with a new cell or replace the content of an existing one

        print(str(json.dumps(grid.toStr())))
        return str(json.dumps(grid.toStr()))

class Action:
    def GET(self):
        user_data = web.input(id = "no data")
        return user_data.id

    def POST(self):
        data = web.input()  # retrieve input data from client

        tab_serv = Tab({}, RuleRow([]), [], [])

        for i in range(0, grid.nb_of_cells()):
            cur_coords = grid.get_coords(i)
            case_serv = Case(cur_coords, Text(grid.get_cell_content(cur_coords[0], cur_coords[1])))
            if (grid.get_cell_content(cur_coords[0], cur_coords[1])) != "":
                tab_serv.add_tab(case_serv)

        if data["action"] == "conflict":
            print("CLASH : ")
            return str(json.dumps(tab_serv.clash()))

        if data["action"] =="solution":
            print("OPTIMIZE : ")
            return str(json.dumps(tab_serv.optimize()))

        if data["action"] == "reset":
            print("RESET : ")
            print(grid.toStr())
            grid.reset()




if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()


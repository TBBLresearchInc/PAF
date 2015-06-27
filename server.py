# coding=utf-8
from LogicalEngine.RuleRow import RuleRow
from logicalParse.case import Case
from logicalParse.tab import Tab
from logicalParse.text import Text

__author__ = 'Quentin Leroy'
# Quentin Leroy
# Pour le Tableur Logique, outil d'élucidation des conflits logiques
# quentin.leroy@telecom-paristech.fr

""" Cette application web.py fait l'interface entre les inputs du client dans les cellules du tableau
 et l'intelligence de calcul du tableur (interpretation des inputs en terme d'expressions logiques puis
 divers calculs logiques), l'application renvoie aussi au client les resultats de la partie calcul
"""

import web, json

from grid import Grid

# Structure des URLs
urls = ("/(.*)/", "Index",
        "/py/json", "Json",
        "/py/action", "Action")

grid = Grid()

class Index:
    def GET(self, name):
        if not name:
            name = "World"
        return "Home Page"

# Classe gerant les mises a jour du tableau
class Json:

    def GET(self):
        user_data = web.input(id = "no data")
        return user_data.id

    def POST(self):
        data = web.input() # On recupere les parametres de la requete POST, c'est un objet JSON

        content = str(data["content"])
        row = int(data["row"])
        column = int(data["column"])
        grid.update(row, column, content)  # on ajoute une cellule ou modifie une cellule deja existante

        print(str(json.dumps(grid.toStr())))
        return str(json.dumps(grid.toStr()))

# Classe reagissant aux clicks de l'utilisateur sur les boutons
class Action:
    def GET(self):
        user_data = web.input(id = "no data")
        return user_data.id

    def POST(self):
        data = web.input()  # On recupere les parametres de la requete POST

        tab_serv = Tab({}, RuleRow([]), [], [])  # On cree l'objet comprehensible par le moteur logique

        for i in range(0, grid.nb_of_cells()):  #  On parcourt grid et on remplit l'objet pour le moteur logique
            cur_coords = grid.get_coords(i)
            case_serv = Case(cur_coords, Text(grid.get_cell_content(cur_coords[0], cur_coords[1])))
            # Le moteur logique ne doit pas recupere les cellules correspondant a un commentaire ou les cellules qui
            # ont ete remplies puis effacees
            if (grid.get_cell_content(cur_coords[0], cur_coords[1])) != "":
                tab_serv.add_tab(case_serv)

        # Si l'utilisateur a demande la resolution de conflits
        if data["action"] == "conflict":
            print("CLASH : ")
            return str(json.dumps(tab_serv.clash()))  # appel du moteur logique

        # Si l'utilisateur a demande l'optimisation
        if data["action"] =="solution":
            print("OPTIMIZE : ")
            return str(json.dumps(tab_serv.optimize()))  # appel du moteur logique

        # Si l'utilisateur a recharge la page web
        if data["action"] == "reset":
            print("RESET : ")
            grid.reset()  # on nettoie grid a chaque nouvelle connexion
            print(grid.toStr())




# Lancement de l'application
if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()


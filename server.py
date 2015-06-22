__author__ = 'Quentin Leroy'
# Quentin Leroy
# quentin.leroy@telecom-paristech.fr

""" Cette application web.py fait l'interface entre les inputs du client dans les cellules du tableau
 et l'intelligence de calcul du tableur (interpretation des inputs en terme d'expressions logiques puis
 divers calculs logiques), l'application renvoie aussi aux clients les resultats de la partie calcul
 (il y a t il des cases a colorier ? En quelles couleurs ? Il y a t il des cellules a completer-modifier ?
  Il y a t il un message a donner a l utilisateur ?)"""

import web, json

from grid import Grid

urls = ("/(.*)/", "Index",
        "/py/json", "Json",)

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
        cell = {'content': content, 'row': row, 'column': column}
        grid.update(row, column, content) #update the grid with the propered-formatted input
        ####################################
        # data process from logical engine #
        ####################################
        print(grid) # debug purpose
        print(str(grid.get_colors())) #debug purpose
        return str(json.dumps(grid.get_colors())) # return colors to fill the cells after some data process (not yet)



grid = Grid({})

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
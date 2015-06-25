# coding=utf-8
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

        grid = Grid({})

        nb_data = len(data["cells"])

        for i in range(0, len[data["cells"]]):
            content = str(data["cells"][i]["content"])
            row = int(data["cells"][i]["row"])
            column = int(data["cells"][i]["column"])
            grid.update(row, column, content)

        # Filename to write
        filename = "data.txt"

        # Open the file with writing permission
        myfile = open(filename, 'w')

        # Write a line to the file
        myfile.write(json.dumps(data))

        # Close the file
        myfile.close()

        ####################################
        # data process from logical engine #
        ####################################

        # En fonction des calculs effectues, il faudra appeler set_color(row, column)

        print(grid) # debug purpose
        print(str(grid.get_colors())) #debug purpose
        return str(json.dumps(grid.get_colors())) # return colors to fill the cells after some data process (not yet)

grid = Grid({})

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
__author__ = 'Quentin Leroy'
# Quentin Leroy
# quentin.leroy@telecom-paristech.fr

""" Cette application web.py fait l'interface entre les inputs du client dans les cellules du tableau
 et l'intelligence de calcul du tableur (interpretation des inputs en terme d'expressions logiques puis
 divers calculs logiques), l'application renvoie aussi aux clients les resultats de la partie calcul
 (il y a t il des cases a colorier ? En quelles couleurs ? Il y a t il des cellules a completer-modifier ?
  Il y a t il un message a donner a l utilisateur ?)"""

import web, json

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
        tab.update(row, column, content) #update the grid with the propered-formatted input
        ####################################
        # data process from logical engine #
        ####################################
        print(tab) # debug purpose
        print(str(tab.get_colors())) #debug purpose
        return json.dumps(tab.get_colors()) # return colors to fill the cells after some data process (not yet)


class GridPos:
    pos = []

    def __init__(self, row, column):
        self.pos = [row, column]

    def toStr(self):
        return "["+str(self.pos[0])+","+str(self.pos[1])+"]"

    def get_row(self):
        return self.pos[0]

    def get_column(self):
        return self.pos[1]



class Tab:

    tab = {}

    tab_pos = []

    colors = []

    pos = GridPos(1,1)

    def __init__(self, tab):
        self.tab = tab
        self.pos = GridPos(1,1)

    def update(self, row, column, content, color="wrong"):
        self.pos = GridPos(row, column)
        self.tab[self.pos.toStr()] = {"content": content, "row": row, "column": column, "color": color}
        if not([row, column] in self.tab_pos):
            self.tab_pos.append([row, column])

    def __str__(self):
        return str(self.tab)

    def get_cell(self, row, column):
        self.pos = GridPos(row, column)
        return self.tab[self.pos.toStr()]["content"]

    def get_color(self, row, column):
        self.pos = GridPos(row, column)
        return self.tab[self.pos.toStr()]["color"]

    def get_pos(self):
        return self.tab_pos

    def set_color(self, row, column, color):
        self.pos = GridPos(row, column)
        self.tab[self.pos.toStr()]["color"] = color

    def get_colors(self):
        colors = {}
        colors["cells"] = []
        for i in range(0, len(self.tab_pos)):
            self.pos = GridPos(self.tab_pos[i][0], self.tab_pos[i][1])
            colors["cells"].append({"row": self.tab_pos[i][0], "column": self.tab_pos[i][1], "result": self.tab[self.pos.toStr()]["color"]})
        return colors


tab = Tab({})

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()
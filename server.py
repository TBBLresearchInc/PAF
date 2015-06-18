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
        data = web.input()
        #print(data["row"])
        #print(data["column"])
        #print(data["content"])
        content = str(data["content"])
        row = int(data["row"])
        column = int(data["column"])
        cell = {'content': content, 'row': row, 'column': column}
        grid.update(row, column, content)
        print(grid)

        return grid.get_colors()





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

    pos = GridPos(1,1)

    def __init__(self, tab):
        self.tab = tab
        self.pos = GridPos(1,1)

    def update(self, row, column, content):
        self.pos = GridPos(row, column)
        self.tab[self.pos.toStr()] = [content, row, column]
        if not([row, column] in self.tab_pos):
            self.tab_pos.append([row, column])

    def __str__(self):
        return str(self.tab)

    def get_cell(self, row, column):
        self.pos = GridPos(row, column)
        return self.tab[GridPos.toStr()][0]

    def get_colors(self):
        colors = {}

        colors["cells"] = []

        for i in range(0, len(self.tab_pos)):

            colors["cells"].append({"row": self.tab_pos[i][0], "column": self.tab_pos[i][1], "result": "wrong"})



grid = Tab({})












if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()

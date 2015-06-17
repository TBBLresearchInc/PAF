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
        grid.update(cell)
        for i in range(0, len(grid)):
            print(grid.get(i))

        return { "cells": [ {"row":1, "column":1, "class":"wrong"},
                {"row":1, "column": 2, "class":"wrong"} ] }

class Grid:

    grid = []

    def __init__(self, grid):
        self.grid = grid

    def update(self, cell):
        cpt = 0
        for i in range(0, len(self.grid)):
            if self.grid[i]["row"] == cell["row"] and self.grid[i]["column"] == cell["column"]:
                self.grid[i] = cell
                print("replace")
                cpt = cpt + 1
                print(cpt)
                return
            else:
                print("add")
                self.grid.append(cell)
                return
        self.grid.append(cell)

    def get(self, pos):
        return self.grid[pos]

    def __len__(self):
        return len(self.grid)

grid = Grid([])










if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()

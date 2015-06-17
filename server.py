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

        return { "cells": [ {"row":1, "column":1, "class":"wrong"},
                {"row":1, "column": 2, "class":"wrong"} ] }








class GridPos:
    pos = []

    def __init__(self, row, column):
        self.pos = [row, column]

    def toStr(self):
        return "["+str(self.pos[0])+","+str(self.pos[1])+"]"



class Tab:

    tab = {}

    pos = GridPos(1,1)

    def __init__(self, tab):
        self.tab = tab
        self.pos = GridPos(1,1)

    def update(self, row, column, content):
        self.pos = GridPos(row, column)
        self.tab[self.pos.toStr()] = content

    def __str__(self):
        print(self.tab)



grid = Tab({})










if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()

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
        return "row : " + data["row"] + " , column : " + data["column"] + ", content : " + data["content"]

class Grid:

    grid = []

    def __init__(self, grid):
        self.grid = grid

    def update(self, cell):
        for i in range(0, len(self.grid)):
            if int(self.grid[i]["row"]) == int(cell["row"]) & int(self.grid[i]["column"]) == int(cell["column"]):
                self.grid[i] = cell
                print("F")
                return
            else:
                self.grid.append(cell)

    def get(self, pos):
        return self.grid[pos]

    def __len__(self):
        return len(self.grid)

grid = Grid([{"content": "Arnaud", "row": 10, "column": 1}])










if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()

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
        cell = {"content": data["content"], "row": data["row"], "column": data["column"]}
        grid.update(cell)
        print(data["row"])
        print(data)
        for i in range(0, len(grid)):
            print(grid.get(i))
        return "row : " + data["row"] + " , column : " + data["column"] + ", content : " + data["content"]

class Grid:

    grid = []

    def __init__(self, grid):
        self.grid = grid

    def update(self, cell):
        for i in range(0, len(self.grid)):
            if self.grid[i]["row"] == cell["row"] & self.grid[i]["column"] == cell["column"]:
                self.grid[i] = cell
                return
            else:
                self.grid.append(cell)

    def get(self, pos):
        return self.grid[pos]

    def __len__(self):
        return len(self.grid)

grid = Grid([])










if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()

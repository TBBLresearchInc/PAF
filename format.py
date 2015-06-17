__author__ = 'quentinleroy'

class Grid:

    grid = []

    def __init__(self, grid):
        self.grid = grid

    def update(self, cell):
        for i in range(0, len(self.grid)):
            if self.grid[i]["row"] == cell["row"] and self.grid[i]["column"] == cell["column"]:
                self.grid[i] = cell
                print("replace")
                return
            else:
                print("add")
                self.grid.append(cell)

    def get(self, pos):
        return self.grid[pos]

    def __len__(self):
        return len(self.grid)

grid = Grid([{"content": "Arnaud", "row": 10, "column": 1}])

grid.update({"content": "Quentin", "row": 10, "column": 1})


for i in range(0, len(grid)):
    print(grid.get(i))

class GridPos:
    pos = []

    def __init__(self, row, column):
        self.pos = [row, column]

    def toStr(self):
        return "["+str(self.pos[0])+","+str(self.pos[1])+"]"

pos = GridPos([1,1])

print(pos.toStr())

tab = {}

tab["[1,1]"] = "contenu"

print(tab)

class Tab:

    tab = {}

    pos

    def __init__(self, tab):
        self.tab = tab
        self.pos = GridPos(1,1)

    def update(self, row, column, content):
        self.tab[self.pos.toStr()] = content


grid = Tab({})



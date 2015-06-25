from LogicalEngine.RuleRow import RuleRow
from logicalParse.case import Case
from logicalParse.tab import Tab
from logicalParse.text import Text

import json

__author__ = 'quentinleroy'

# Quentin Leroy
# quentin.leroy@telecom-paristech.fr

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



class Grid:

    """ Classe decrivant le tableau
    """

    grid = {}

    grid_pos = []

    colors = []

    pos = GridPos(1, 1)

    def __init__(self, grid = {}):
        self.grid = grid
        self.pos = GridPos(1,1)

    def update(self, row, column, content, color="wrong"):
        self.pos = GridPos(row, column)
        self.grid[self.pos.toStr()] = {"content": content, "row": row, "column": column, "color": color}
        if not([row, column] in self.grid_pos):
            self.grid_pos.append([row, column])

    def get_cell(self, row, column):
        self.pos = GridPos(row, column)
        return self.grid[self.pos.toStr()]["content"]

    def get_coords(self, index):
        self.pos = GridPos(self.grid_pos[index][0], self.grid_pos[index][1])
        return (self.grid[self.pos.toStr()]["row"], self.grid[self.pos.toStr()]["column"])

    def delete_cell(self, row, column):
        self.pos = GridPos(row, column)
        self.grid.__delitem__(self.pos.toStr())
        self.grid_pos

    def get_color(self, row, column):
        self.pos = GridPos(row, column)
        return self.grid[self.pos.toStr()]["color"]

    def get_pos(self):
        return self.grid_pos

    def set_color(self, row, column, color):
        self.pos = GridPos(row, column)
        self.grid[self.pos.toStr()]["color"] = color

    def get_colors(self):
        colors = {}
        colors["cells"] = []
        for i in range(0, len(self.grid_pos)):
            self.pos = GridPos(self.grid_pos[i][0], self.grid_pos[i][1])
            colors["cells"].append({"row": self.grid_pos[i][0], "column": self.grid_pos[i][1], "result": self.grid[self.pos.toStr()]["color"]})
        return colors

    def get_grid(self):
        return self.grid

    def get_grid_pos(self):
        return self.grid_pos

    def nb_of_cells(self):
        return len(self.grid_pos)




tabu = Tab({}, RuleRow([]),[] , [])


case = Case((1,1), Text("p1"))
tabu.add_tab(case)

case = Case((1,2), Text("p2"))
tabu.add_tab(case)

case = Case((2,1), Text("p3"))
tabu.add_tab(case)

case = Case((3,1), Text("=$90A1"))
tabu.add_tab(case)

case = Case((1,0), Text("=$10A2"))
tabu.add_tab(case)

case = Case((3,3),Text("=$10B1"))
tabu.add_tab(case)

case = Case((5,9), Text("=R(A1,-A2)"))
tabu.add_tab(case)

case = Case((5,8), Text("=R(A1,-B1)"))
tabu.add_tab(case)



print(tabu.clash())







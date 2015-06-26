__author__ = "quentinleroy"

# Quentin Leroy
# quentin.leroy@telecom-paristech.fr

class Grid:

    """ Classe decrivant le tableau
    """
    grid = {}
    grid_coords = []

    def __init__(self):
        self.grid = {}
        self.grid_coords = []

    def update(self, row, column, content, color="wrong"):
        coords = (row, column)
        self.grid[coords] = {"content": content, "row": row, "column": column, "color": color}
        if not((row, column) in self.grid_coords):
            self.grid_coords.append(coords)

    def get_cell_content(self, row, column):
        coords = (row, column)
        return self.grid[coords]["content"]

    def get_coords(self, index):
        return self.grid_coords[index]

    def delete_cell(self, row, column):
        coords = row, column
        self.grid.__delitem__(coords)
        index = 0
        for i in range(0, len(self.grid_coords)):
            if self.grid_coords[i] == (row, column):
                index = i
        self.grid_coords.pop(index)

    def get_color(self, row, column):
        coords = (row, column)
        return self.grid[coords]["color"]

    def set_color(self, row, column, color):
        coords = (row, column)
        self.grid[coords]["color"] = color

    def nb_of_cells(self):
        return len(self.grid_coords)

    def toStr(self):
        return str(self.grid)

    def reset(self):
        self.grid = {}
        self.grid_coords = []

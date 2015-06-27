__author__ = "quentinleroy"

# Quentin Leroy
# Pour le Tableur Logique, outil d'elucidation de conflits logiques
# quentin.leroy@telecom-paristech.fr

class Grid:

    """ Classe decrivant le tableau du point de vue de l'application web
    """
    grid = {}

    grid_coords = []

    def __init__(self):
        self.grid = {}
        self.grid_coords = []

    # Ajoute ou edite une cellule
    # Appelee a chaque requete POST sur l'URL /py/json
    def update(self, row, column, content, color="wrong"):
        """
        :param row: ligne de la cellule
        :param column: colonne de la cellule
        :param content: chaine de caractere que contient la cellule
        """
        coords = (row, column)
        self.grid[coords] = {"content": content, "row": row, "column": column, "color": color}
        if not((row, column) in self.grid_coords):
            self.grid_coords.append(coords)

    # Renvoie le contenu d'une cellule en specifiant en arguments la ligne et la colonne
    def get_cell_content(self, row, column):
        coords = (row, column)
        return self.grid[coords]["content"]

    # Renvoie les coordonnes de la cellule placee a l'adresse index
    # Utilse quand on parcourt le tableau dans l'ordre chronologique de saisie des cellules
    def get_coords(self, index):
        return self.grid_coords[index]

    # Permet de supprimer une cellule du tableau en specifiant en arguments la ligne et la colonne
    # Utile quand l'utilisateur a rentre du texte dans une cellule mais qu'il a par la suite decide de la laisser vide
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

    # Renvoie le nombre de cellules saisies
    def nb_of_cells(self):
        return len(self.grid_coords)

    def toStr(self):
        return str(self.grid)

    # Appelee lors du chargement de la page web cote client
    def reset(self):
        self.grid = {}
        self.grid_coords = []


from logicalParse.text import Text

__author__ = 'claraberard'


class Predicate(Text):
    yesno = 1

    def __init__(self, sentence,yesno):
        Text.__init__(self,sentence)
        self.yesno = yesno

    def tostring(self):
        return "pred:[" + self.sentence + "," + str(self.yesno) + "]"

    def get_coordinate(self,tab):
        for coord in tab.tab:
            if tab.tab[coord].tostring()[0:5] != "regle":
                if (tab.tab[coord].text.sentence==self.sentence) & (tab.tab[coord].text.__name__() == "predicate"):
                         return coord
        raise Exception('erreur dans get_coordinate : aucune coordonnee trouvee')


    def __name__(self):
        return "predicate"

from logicalParse.text import Text

__author__ = 'claraberard'


class Predicate(Text):
    yesno = 1

    def __init__(self, sentence, yesno):
        Text.__init__(self,sentence)
        self.yesno = yesno

    def tostring(self):
        return "pred:[" + self.sentence + "," + str(self.yesno) + "]"

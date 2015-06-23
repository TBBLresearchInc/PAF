from logicalParse.text import Text

__author__ = 'claraberard'


class Predicate(Text):
    def __init__(self, sentence, yesno):
        Text.__init__(self, sentence)
        self.yesno=yesno

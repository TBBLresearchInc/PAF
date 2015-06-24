__author__ = 'claraberard'


class Predicate():
    sentence = ""
    yesno = 1

    def __init__(self, sentence, yesno):
        self.sentence = sentence
        self.yesno = yesno

    def tostring(self):
        return "pred:[" + self.sentence + "," + str(self.yesno) + "]"

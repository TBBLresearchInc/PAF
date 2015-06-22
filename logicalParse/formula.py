from logicalParse.coordinates_tab import Coordinates_tab
from logicalParse.fnon import FNon
from logicalParse.fweight import FWeight
from logicalParse.rule import Rule
from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Formula(Text):
    sentence = "="

    def __init__(self, sentence):
        self.sentence = sentence
        self.nature = 4

    def isFormulaWeight(self):
        return self.get_inside()[0] == '&'

    def isFormulaNon(self):
        return self.get_inside()[0:2] == "NON"

    def isFormulaResult(self):
        return self.get_inside()[0] == "("

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def to_logical_rule(self, tab):
        """
        :type tab: Tab
        """
        R = Rule([])
        s = self.sentence[2:(len(self.sentence) - 2)]
        while len(s) != 0:
            i = 0
            while s[i].isalpha():
                i += 1
            l = s[0:i]
            j = i + 1
            while s[j].is_number():
                j += 1
            n = float(s[(i + 1): j])
            c = Coordinates_tab(n, l).coordinates_to_string()
            R.list.add_incompability(tab, c)
            s = s[(j + 1):]
        return R

    def to_fweight_formula(self):
        s = self.sentence[2:(len(self.sentence) - 1)]
        i = 0
        while s[i].is_number():
            i += 1
        l = float(s[0:i])
        j = i + 1
        while s[j].is_alpha():
            j += 1
        m = s[(i + 1): j]
        k = j + 1
        while s[k].is_number():
            k += 1
        n = float(s[(j+1):k])
        weight = Weight(l)
        c = Coordinates_tab(n, m).coordinates_to_string()

        f= FWeight(c,weight)
        return f

    def to_fnon_formula(self):
        s = self.sentence[4:(len(self.sentence) - 1)]
        i = 0
        while s[i].is_alpha():
            i += 1
        m = s[0: i]
        j = i + 1
        while s[j].is_number():
            j += 1
        n = float(s[(i+1):j])
        c = Coordinates_tab(n, m).coordinates_to_string()
        f= FNon(c)
        return f










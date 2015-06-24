from logicalParse.coordinates_tab import Coordinates_tab
from logicalParse.fnon import FNon
from logicalParse.fweight import FWeight
from logicalParse.rule import Rule
from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Formula(Text):

    def __init__(self, sentence):
        Text.__init__(self, sentence)

    def isFormulaWeight(self):
        print self.sentence[0]

        return self.sentence[0] == "$"

    def isFormulaNon(self):
        return self.sentence[0:2] == "NON"

    def isFormulaResult(self):
        return self.sentence[0] == "("

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def is_alpha(self,s):
        return not(self.is_number(s))

    def to_logical_rule(self, tab, coordinates):
        """
        :type tab: Tab
        """
        R = Rule([], coordinates)
        s = self.sentence[2:(len(self.sentence) -1)]
        while len(s) != 0:
            i = 0
            while self.is_alpha(s[i]):
                i += 1
            l = s[0:i]
            j = i
            while self.is_number(s[j]):
                j += 1
            n = float(s[i: j])
            c = Coordinates_tab(n, l).coordinates_to_int()
            R.list.add_incompability(tab, c)
            s = s[(j + 1):]
        tab.rule_list.append(R)


    def to_fweight_formula(self):
        s = self.sentence[1:(len(self.sentence))]
        print s
        i = 0
        while self.is_number(s[i]):
            i += 1
        l = float(s[0:i])
        j = i
        print "i=" + str(i)
        print "s[j]=" + str(s[j])
        while self.is_alpha(s[j]):
            print "yolo"
            j += 1
        m = s[i:j]
        print m
        k = j
        while k < len(s) and self.is_number(s[k]):
            print "yola"
            k += 1
        print s[j:k]
        n = float(s[j:k])
        print n
        weight = Weight(l)
        c = Coordinates_tab(n, m).coordinates_to_int()
        f = FWeight(c, weight)
        return f

    def to_fnon_formula(self):
        s = self.sentence[4:(len(self.sentence))]
        i = 0
        while self.is_alpha(s[i]):
            i += 1
        m = s[0: i]
        j = i
        while j<len(s) and self.is_number(s[j]):
            j += 1
        n = float(s[i:j])
        c = Coordinates_tab(n, m).coordinates_to_int()
        f= FNon(c)
        return f

    def fsolve(self, tab, coordinates):
        if self.isFormulaWeight():
            self.to_fweight_formula().weight_solve(tab, coordinates)
        else:
            if self.isFormulaNon():
                self.to_fnon_formula().non_solve(tab, coordinates)
            else:
                pass

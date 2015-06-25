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
        return self.sentence[0] == "$"

    def isFormulaNon(self):
        return self.sentence[0:3] == "NON"

    def isFormulaResult(self):
        return self.sentence[0] == "("

    def isFormulaRule(self):
        return self.sentence[0:1] == "R"

    def is_number(self, s): #pour tester si un caractere est un nombre
        try:
            float(s)
            return True
        except ValueError:
            return False

    def is_alpha(self,s): #si un caractere est une lettre
        return not(self.is_number(s)) #sous supposition que l'utilisateur necrit que des lettres et des nombres


    def to_logical_rule(self, tab, coordinates):  #permet de traduire une phrase du type =R(-A1,A2,A3) en une regle
        R = Rule([], coordinates)
        s = self.sentence[2:(len(self.sentence)-1)] #s=A1,A2,A3)
        while len(s) != 0: #on va diminuer la sequence a chaque fois en ajoutant les cases dans lattribut liste de cases de la classe rule
            i = 0
            if s[i]=="-": #permet de distinguer non p1 de p1
                yesno=-1
                s= s[1:]
            else:
                yesno=1
            while self.is_alpha(s[i]): #on va chercher a detacher le A du 1 dans l adresse case
                i += 1
                                        # dans l'exemple a la fin de la premiere boucle i = 1
            l = s[0:i]                  # l = 'A'

            j = i                       # j = 1
            while j<len(s) and self.is_number(s[j]):  #on cherche maintenant a detacher le 1
                j += 1                                #fin de la premiere boucle j = 2
            n = int(s[i: j])                           #n = 1

            c = Coordinates_tab(n, l).coordinates_to_int()      # on convertit A1 en (1,1)
            R.add_incompatibility(tab, c, yesno)                # on ajoute la case dans la liste des incompabilites
            s = s[(j + 1):]                                     # s = A2,A3)
        tab.tab[coordinates]=R
        tab.rule_list.row.append(R)                             #on ajoute la regle a la liste des regles du tableau


    def to_fweight_formula(self):           #traduction de =$90A2 en attitudes de Fweight((2,1),90) (meme methode que pour to_logical rule)
        s = self.sentence[1:(len(self.sentence))]
        i = 0
        if s[i]=="-":
                sign=-1
                s= s[1:]
        else:
                sign=1
        while self.is_number(s[i]):
            i += 1
        l = float(s[0:i])
        j = i
        while self.is_alpha(s[j]):
            j += 1
        m = s[i:j]
        k = j
        while k < len(s) and self.is_number(s[k]):
            k += 1
        n = float(s[j:k])
        weight = Weight(l*sign)
        c = Coordinates_tab(n, m).coordinates_to_int()
        f = FWeight(c, weight)
        return f

    def to_fnon_formula(self):   #traduction de = NONA1 en FNON(1,1)
        s = self.sentence[3:(len(self.sentence))]
        i = 0
        while self.is_alpha(s[i]):
            i += 1
        m = s[0: i]
        j = i
        while j < len(s) and self.is_number(s[j]):
            j += 1
        n = float(s[i:j])
        c = Coordinates_tab(n, m).coordinates_to_int()
        f= FNon(c)
        return f

    def fsolve(self, tab, coordinates):   #pour resoudre n'importe quelle formule si dessus
        if self.isFormulaWeight():
            self.to_fweight_formula().weight_solve(tab, coordinates)
        elif self.isFormulaNon():
                self.to_fnon_formula().non_solve(tab, coordinates)
        elif self.isFormulaRule():
            self.to_logical_rule(tab,coordinates)
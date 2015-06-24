from logicalParse.case import Case
from logicalParse.formula import Formula
from logicalParse.rule import Rule
from logicalParse.tab import Tab
from logicalParse.text import Text

__author__ = 'claraberard'

t = {}
table_rule = []
tabu = Tab(t, table_rule)

case = Case((1,1), Text("p1"))
case2 = Case((2,1), Text("p2"))
case3 = Case((3,1), Text("=$90A1"))
case4 = Case((1,0), Text("=$10A2"))
case5 = Case((4,0), Text("=NONA1"))


tabu.add_tab(case)
tabu.add_tab(case2)
tabu.add_tab(case3)
tabu.add_tab(case4)
tabu.add_tab(case5)

print case5.text.sentence[1:4]

print(tabu.tab[(4,0)].case_solve(tabu))

rule1 = Rule([case, case2], (5,7))
print str(rule1.list[1].text.sentence)

case6 = Case((5,9), Text("=R(A1,A2"))
tabu.add_tab(case6)

f = Formula("=R(A1,A2)")
f.to_logical_rule(tabu, (5,9))

print tabu.rule_list[0].list

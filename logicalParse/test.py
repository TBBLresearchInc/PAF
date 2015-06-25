from LogicalEngine.RuleRow import RuleRow
from logicalParse.case import Case
from logicalParse.predicate import Predicate
from logicalParse.tab import Tab
from logicalParse.text import Text

__author__ = 'claraberard'

t = {}
table_rule = RuleRow([])
tabu = Tab(t, table_rule,[], [])

case1 = Case((1,1), Text("p1"))
case2 = Case((1,2), Text("p2"))
case3 = Case((2,1), Text("p3"))
case4 = Case((3,1), Text("=$90A1"))
case5 = Case((1,0), Text("=$10A2"))
case7 = Case((5,9), Text("=R(A1,A2)"))
case8 = Case((5,8), Text("=R(A1,-B1)"))


tabu.add_tab(case1)
tabu.add_tab(case2)
tabu.add_tab(case2)
tabu.add_tab(case3)
tabu.add_tab(case4)
tabu.add_tab(case5)
tabu.add_tab(case7)
tabu.add_tab(case8)






tabu.solve()
"""
print tabu.rule_list[1].list[1].text.sentence

print tabu.rule_list[0].list[1].tostring()
"""

print tabu.rule_list.row
print tabu.attitude_caselist
print tabu.predicate_caselist

p=Predicate("yolo",1)
print p
p.yesno=-1
print p
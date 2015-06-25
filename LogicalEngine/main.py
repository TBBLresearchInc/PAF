from LogicalEngine.AttitudeRow import AttitudeRow
from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from LogicalEngine.Solutions import Solutions
from logicalParse.attitude import Attitude
from logicalParse.case import Case
from logicalParse.predicate import Predicate
from logicalParse.rule import Rule
from logicalParse.tab import Tab
from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'Yannick'

t = {}
table_rule = RuleRow([])
tabu = Tab(t, table_rule,[], [])

case1 = Case((1,1), Text("p1"))
case2 = Case((1,2), Text("p2"))
case3 = Case((2,1), Text("p3"))
case4 = Case((3,1), Text("=$90A1"))
case5 = Case((1,0), Text("=$10A2"))
case6 = Case((3,3),Text("=$10B1"))
case7 = Case((5,9), Text("=R(A1,A2)"))
case8 = Case((5,8), Text("=R(A1,-B1)"))


tabu.add_tab(case1)
tabu.add_tab(case2)
tabu.add_tab(case2)
tabu.add_tab(case3)
tabu.add_tab(case4)
tabu.add_tab(case5)
tabu.add_tab(case6)
tabu.add_tab(case7)
tabu.add_tab(case8)

"""
pr1=Predicate("p1",1)
pr2=Predicate("p2",1)
pr3=Predicate("p3",1)
pr4=Predicate("p4",1)

p1=Predicate("p1",1)
p2=Predicate("p2",1)
p3=Predicate("p3",1)
p4=Predicate("p4",1)

a1=Attitude("p1",Weight(50),1)
a2=Attitude("p2",Weight(30),1)
a3=Attitude("p3",Weight(20),1)
a4=Attitude("p4",Weight(- 10),1)

r1=Rule([pr1,pr2,pr3],(2,2))
r2=Rule([pr1,pr4],(1,1))

attrow= AttitudeRow([a1,a2,a3,a4])
predrow=PredicateRow([p1,p2,p3,p4])
rulerow=RuleRow([r1,r2])
"""


tabu.solve()


attrow=tabu.get_attrow()
predrow=tabu.get_predrow()
rulerow=tabu.rule_list

print predrow
print rulerow.tostring()
print attrow.attrow_to_predrow().tostring()

print attrow.issatisfiable(rulerow)

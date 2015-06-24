from LogicalEngine.AttitudeRow import AttitudeRow
from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from LogicalEngine.Solutions import Solutions
from logicalParse.attitude import Attitude
from logicalParse.predicate import Predicate
from logicalParse.rule import Rule
from logicalParse.weight import Weight

__author__ = 'Yannick'


pr1=Predicate("p1",1)
pr2=Predicate("p2",1)
pr3=Predicate("p3",1)
pr4=Predicate("p4",1)

p1=Predicate("p1",1)
p2=Predicate("p2",1)
p3=Predicate("p3",1)
p4=Predicate("p4",1)

a1=Attitude("p1",1,Weight(50))
a2=Attitude("p2",1,Weight(30))
a3=Attitude("p3",1,Weight(20))
a4=Attitude("p4",1,Weight(- 10))

r1=Rule([pr1,pr2,pr3])
r2=Rule([pr1,pr4])

attrow= AttitudeRow([a1,a2,a3,a4])
predrow=PredicateRow([p1,p2,p3,p4])
rulerow=RuleRow([r1,r2])



print attrow.issatisfiable(rulerow)

print attrow.bestsolve(rulerow).tostring()
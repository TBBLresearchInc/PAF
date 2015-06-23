from LogicalEngine.AttitudeRow import AttitudeRow
from LogicalEngine.PredicateRow import PredicateRow
from LogicalEngine.RuleRow import RuleRow
from LogicalEngine.Solutions import Solutions
from logicalParse.attitude import Attitude
from logicalParse.predicate import Predicate
from logicalParse.rule import Rule
from logicalParse.weight import Weight

__author__ = 'Yannick'


p1=Predicate("p1",1)
p2=Predicate("p2",1)
p3=Predicate("p3",1)
p4=Predicate("p4",1)

a1=Attitude(p1,Weight(50),1)
a2=Attitude(p2,Weight(30),1)
a3=Attitude(p3,Weight(20),1)
a4=Attitude(p4,Weight(-10),1)

r1=Rule([p1,p2,p3])
r2=Rule([p1,p4])

attrow= AttitudeRow([a1,a2,a3,a4])
predrow=PredicateRow([p1,p2,p3,p4])
rulerow=RuleRow([r1,r2])


print attrow.bestsolve(rulerow)

sol= Solutions([])

sol.insert(Weight(5),Weight(3),predrow)

print sol.matrix[1].row
__author__ = 'Yannick'



class RuleRow:


   def __init__(self, row):
       self.row=row

   row=[]

   def tostring(self):
        s="rulerow :("
        for rule in self.row:
            s+= rule.tostring()+", "
        return s+")"
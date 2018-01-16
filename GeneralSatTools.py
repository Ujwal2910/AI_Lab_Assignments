import random
import copy
random.seed()

"""
returns the number of clauses which are satisfiable
"""
def testAssignments(cnf, myAssign):
    goodClause = 0
    for clause in cnf:
        for i in range(len(myAssign)):
            if myAssign[i]*clause[i]>0:
                goodClause+=1
                break
    return goodClause
"""
nbvar is the number of variables in real expressions
returns an array of length nbvar that has the value -1(false) or 1(true) (Work as boolean)
"""
def GenerateRandomAssignment(nbvar):
    boolvec = []
    for i in range(nbvar):
        boolvec.append(random.randrange(-1,2,2))
    return boolvec

def DeepCopy(CopyFrom):
    return copy.deepcopy(CopyFrom)
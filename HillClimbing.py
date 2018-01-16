import GeneralSatTools as GST

"""
Convert Expression in Conjucntion Normal Form
cnf is the 2d array containing the cnf that is to be solved
The highest valued node will be given
returns the best possible next herustic
"""
def GetBestHerustic(cnf, assignment):
    BestAssign = GST.DeepCopy(assignment)
    BestC = GST.testAssignments(cnf,assignment)
    for i in range(len(assignment)):
        #node change
        assignment[i] *= -1
        tempC = GST.testAssignments(cnf,assignment)
        if(tempC > BestC):
            BestC = tempC
            BestAssign = GST.DeepCopy(assignment)
        assignment[i] *= -1 #reverse node change and continue loop with next node

    return BestAssign, BestC
"""
HillClimbing(cnf, assign)
assign is the assignment which will expand until a local maximum is reached
"""
def HillClimbing(cnf, assignment):
    CurrentEval = GST.testAssignments(cnf, assignment)
    NextAssignment, NextEval = GetBestHerustic(cnf, assignment)
    if(NextEval<=CurrentEval):
        return CurrentEval
    else:
        return HillClimbing(cnf, NextAssignment)
"""
Solve(cnf,s)
s is the number of local searches to perform until returning the highest found c value
"""
def Solve(cnf, s):
    AveC=[]
    HighC = -1
    for i in range(s):
        Best = -1
        MyAssignment = GST.GenerateRandomAssignment(len(cnf[0]))
        newC = HillClimbing(cnf, MyAssignment)
        if newC > Best:
            Best = newC
            if Best > HighC:
                HighC = Best
            if(Best == len(cnf)):
                print("It is Satisfiable")
                AveC.append(Best)
                return sum(AveC)/len(AveC), HighC
            else:
                print("It is Unsatisfiable")
        AveC.append(Best)
    return sum(AveC)/len(AveC), HighC
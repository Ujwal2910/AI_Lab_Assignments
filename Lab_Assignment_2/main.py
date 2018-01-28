import HillClimbing
import time
import glob

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
"""Read Converted Input to from an expression to CNF form
Calls hill climbing while timing each call and printing the most clauses satisfied
"""
if __name__ == '__main__':
    for filename in glob.glob("*.cnf"):
        cnf = []
        nbclauses = -1
        nbvar = -1
        with open(filename) as file:
            content = file.readlines()
            curClause = -1
            for line in content:
                splitLine = line.split(' ')
                if splitLine[0] == 'p' and splitLine[1] == 'cnf':
                    nbvar = int(splitLine[2])
                    nbclauses = int(splitLine[3])

                    cnf = [[0 for i in range(nbvar)] for j in range(nbclauses)]
                elif nbvar > 0 and nbclauses > 0 and splitLine[0] != 'c':
                    curClause += 1
                    for variable in splitLine:
                        if is_int(variable):
                            if int(variable) != 0:
                                cnf[curClause][abs(int(variable))-1] = int(variable)


        s = 10 #number of iterations

        HillStart = time.time()
        cHillAve, HighHillc = HillClimbing.Solve(cnf, s)
        HillEnd = time.time()
        print("Highest:", HighHillc)
        print("Run time:", HillEnd - HillStart, "seconds")


print('')
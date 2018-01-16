import random
#import numpy as np
#import ArrayList as alist
import string

def generate_values(k, m, n):

    #defining variables list array for storing all upper case alphabets
    variables = [i for i in string.ascii_uppercase[:n]]
    clause_list = []
    symbols = [' v ', ' ! ']
    #or and negation symbol
    #empty clause list for manipulation
    for loop_variable in range(m):
        random.shuffle(variables)
        variable_list = variables[0:k]
        symbol_list = []
        for loop_variable in range(1, k):
            random_symbol = random.choice(symbols)
            if random_symbol == ' ! ':
                random_symbol = ' v !'
            symbol_list.append(random_symbol)
        clause = []
        #the negation before a variable is added by a .5 probabilty
        if random.choice([True, False]):
            clause.append('!')
        for loop_variable in range(k-1):
            clause.append(variable_list[loop_variable])
            clause.append(symbol_list[loop_variable])
        clause.append(variable_list[-1])
        clause_list.append(clause)
    return variables, symbols,  clause_list

def display_result(variables_receive, symbols_receive, clause_list_receive):
    #displaying the variable ,symbols and clauses used and generated later
    print('Symbols to be used-  ' + str(symbols_receive))
    print('Variables to be used - ' + str(variables_receive))
    final_string = ""
    #the symbol checking
    for clauses in clause_list_receive:
        final_string += "("
        for variables_receive in clauses:
            final_string += variables_receive
        final_string += ") ^ "
    final_string = final_string[:-2]
    #calculate the final string and display it
    print("final Result-")
    print(final_string)



if __name__ == "__main__":
    #supply the values for k,m and n

    '''
    k - no. of elements in each clause to randomly picked up from the given list
    m - no. of clauses in each formula
    n - no. of Variables

    '''
    print("k chosen should be less than or equal to the number of varibles n")
    k = 5
    m = 6
    n = 8
    #print(n)
    variables, symbols, clause_list = generate_values(k, m, n)
    #call in the display function to display the final values
    display_result(variables, symbols,  clause_list)

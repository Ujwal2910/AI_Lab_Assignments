from operator import add, sub, mul, div
import itertools
ops = ['+', '-', '*', '/']
op_map = {'+': add, '-': sub, '/': div, '*': mul}
# iterate operator combinations
def iter_combinations(seq):
    if len(seq) == 1:
        yield seq[0], str(seq[0])
    else:
        for i in range(len(seq)):
            left, right = seq[:i], seq[i:]  # split input list at i`th place
            # generate product
            for l, l_str in iter_combinations(left):
                for r, r_str in iter_combinations(right):
                    for op in ops:
                        if op_map[op] is div and r == 0:  # Constraint '/' zero
                            continue
                        else:
                            yield op_map[op](float(l), r), \
                                  ( l_str + op + r_str )

print " Enter those 6 magical numbers "
a = input('Enter a1 value: ')
b = input('Enter a2 value: ')
c = input('Enter a3 value: ')
d = input('Enter a4 value: ')
e = input('Enter a5 value: ')
f = input('Enter a6 value: ')

print " Enter Target Value"
target = input()

num_list = [a,b,c,d,e,f]
best_value = target 
final = None

for i in range(len(num_list)):
    for current in itertools.permutations(num_list, i+1): # permutations
        for value, item in iter_combinations(list(current)):
            if value < 0:
                continue

            if abs(target - value) < best_value:
                best_value = abs(target - value)
                final = item

print final
from sympy import symbols
from sympy.logic.boolalg import Or, And, Implies, Not
from sympy.abc import a, b, c
from sympy.abc import X, Y, Z
from sympy.abc import A, B, C
from sympy.logic import satisfiable

def is_satisfiable(formula):
    return satisfiable(formula)

# Define the given SAT problem
# clause1 = Or(X, Y, Z)
# clause2 = Or(X, Not(Y), Not(Z))
# clause3 = Or(Not(X), Y, Z)
# clause4 = Or(Not(X), Not(Y), Not(Z))
# clause5 = Or(Not(Y), Z)
# clause6 = Or(Y, Not(Z))

# clause1 = Or(a, b, c)
# clause2 = Or(a, Not(b))
# clause3 = Or(a, Not(c))
# clause4 = Or(Not(a), c)

clause1 = Or(A, B)
clause2 = Or(A, Not(B), C)
clause3 = Or(Not(A), B)
clause4 = Or(Not(A), Not(B), C)
clause5 = Or(Not(B), Not(C))

# Combine all clauses with 'And'
boolean_formula = And(clause1, clause2, clause3, clause4) #, clause5, clause6

# Check if the formula is satisfiable
satisfiable = is_satisfiable(boolean_formula)

a, b, c = symbols('a b c')

# clause1 = Or(a, b, c)
# clause2 = Or(a, Not(b))
# clause3 = Or(a, Not(c))
# clause4 = Or(Not(a), c)





if satisfiable:
    print("The formula is satisfiable.")
    print("Satisfying assignment:", satisfiable)
else:
    print("The formula is not satisfiable.")

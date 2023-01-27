
from sympy import *
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

#initialize first equation
original_equation = sympify(parse_expr(input("Enter the starting equation: \n"), transformations=(standard_transformations+(implicit_multiplication_application,))));

abort = False

while not(abort):
    
    #get subsequent equation
    try:
        next_equation = sympify(parse_expr(input("=      "), transformations=(standard_transformations + (implicit_multiplication_application,))));

    
            #check if original and next equation are equivalent
        if expand(original_equation) == expand(next_equation):
            print("Correct.")
        else:
            print("You just made a mistake. Try again.")
    except:
        print("Formatting error.")
        if (input("Enter Y to abort") == 'Y'):
            abort = True


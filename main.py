
from sympy import *

#initialize first equation
original_equation = sympify(parsing.parse_expr(input("Enter the starting equation: \n")));

while True:
    #get subsequent equation
    try:
        next_equation = sympify(parsing.parse_expr(input("=      ")));

    
            #check if original and next equation are equivalent
        if expand(original_equation) == expand(next_equation):
            print("Correct.")
        else:
            print("You just made a mistake. Try again.")
    except:
        print("Formatting error.")


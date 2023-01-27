import sympy

#initialize first equation
original_equation = input("Enter the starting equation");

while True:
    #get subsequent equation
    next_equation = input("Enter the next equality");

    #check if original and next equation are equivalent
    if sympy.simplify(original_equation) == sympy.simplify(next_equation):
        print("Correct.")
    else:
        print("You just made a mistake. Try again.")


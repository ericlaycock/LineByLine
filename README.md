Example of usage:

Enter the starting equation: 
summation(4i**3 -6i**2 + 4i - 1, (i, 1, n)) -n**4 
=      4*summation(i**3, (i, 1, n)) -6*summation(i**2, (i, 1, n)) + 4*summation(i, (i, 1, n)) - summation(1, (i, 1, n)) -n**4
Correct.
=      4*summation(i**3, (i, 1, n)) -6*summation(i**2, (i, 1, n)) + 4*summation(i, (i, 1, n)) - n -n**4                       
Correct.
=      4*summation(i**3, (i, 1, n)) -6*summation(i**2, (i, 1, n)) + 2*(n)(n+1) - n -n**4                
Correct.
=      4*summation(i**3, (i, 1, n)) -n(n+1)(2n+1) + 2*(n)(n+1) - n -n**4                       
Correct.
=      4*summation(i**3, (i, 1, n)) (-n**2 -n)(2n+1) + (2n)(n+1) - n -n**4  
You just made a mistake. Try again.
=      4*summation(i**3, (i, 1, n)) + (-n**2 -n)(2n+1) + (2n)(n+1) - n -n**4
Correct.
=      4*summation(i**3, (i, 1, n)) + (-2n**3 -n**2 -2n**2 -n) + (2n)(n+1) - n -n**4
Correct.
=      4*summation(i**3, (i, 1, n)) + -2n**3 -n**2 -2n**2 -n + 2n**2 +2n - n -n**4          
Correct.
=      4*summation(i**3, (i, 1, n)) + -2n**3 -n**2 -n +2n - n -n**4                
Correct.
=      4*summation(i**3, (i, 1, n)) + -2n**3 -n**2 -n**4            
=      4*summation(i**3, (i, 1, n))  - n(2n**2 -n -n**3)
Correct.
=      summation(i**3, (i, 1, n))
You just made a mistake. Try again.
=      Formatting error.
Enter Y to abortY
PS C:\Users\ericl\Desktop\js_html\LineByLine> py main.py
Enter the starting equation:
summation(i**3, (i, 1, n))
=      (n^2(n+1)^2)/4
Formatting error.
Enter Y to abort(n^2(n+1)^2)/4
=      (n**2 * (n+1)**2)/4
Correct.
=
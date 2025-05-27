import math

def sum_of_factorial_digits(n):
    factorial = math.factorial(n)         
    digits = str(factorial)              
    total = sum(int(d) for d in digits)   
    return total

print(sum_of_factorial_digits(100))       

import math

def answer():
    champernowne = ""
    n = 1
    while len(champernowne) <= 1000000:
        champernowne += str(n)
        n += 1
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000] #CHANGE TO TEST OTHERS INDICES
    digits = [int(champernowne[i-1]) for i in indices]
    print(digits) #OPTIONAL
    return math.prod(digits)

print(answer())

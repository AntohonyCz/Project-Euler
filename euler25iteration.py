import math

a, b = 1, 1
gen = 2

while True:
    a, b = b, a + b
    gen +=1

    if math.log10(b) >= 999:
        print(gen)
        break

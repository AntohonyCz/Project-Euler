import math

phi = (1 + math.sqrt(5)) / 2
digits = 1000

n = math.ceil((digits - 1 + math.log10(5)/2) / math.log10(phi))
print(n)

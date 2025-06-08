import math

def numtosearch(n):
    digit_length = 1
    count = 9
    start = 1

    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    number = start + (n - 1) // digit_length
    digit_index = (n - 1) % digit_length
    return int(str(number)[digit_index])

def answer():
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    sols = [numtosearch(i) for i in indices]
    return math.prod(sols)

print(answer())
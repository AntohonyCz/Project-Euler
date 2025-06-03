def main():
    result = 1
    for i in range(1,21):
        result = lcm(result, i)
    print(int(result))

def lcm(a, b):
    return a * b // gcd(a,b)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

main()

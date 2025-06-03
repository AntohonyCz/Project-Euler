results = []

def limit(n):
    d = 1
    while True:
        if d * 9**n < 10**(d - 1):
            return (d - 1) * 9**n
        d += 1


def answer(n):
    limitval = limit(n)

    return sum( 
        i for i in range(2, limitval + 1)
        if i == sum(int(digit**n) for digit in str(i)) 
    )
    


print(answer(5)) #CHANGE BY THE POWER THAT YOU WANT TO TRY
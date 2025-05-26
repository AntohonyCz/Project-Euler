def SieveOfEratosthenes(limit):
    prime = [True] * limit
    prime[0:2] = [False, False]  

    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, limit, p):
                prime[i] = False

    return sum(p for p, is_prime in enumerate(prime) if is_prime)

result = SieveOfEratosthenes(2_000_000)
print(result)




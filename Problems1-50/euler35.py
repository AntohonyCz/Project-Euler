import math

def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
    return prime

def get_rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_valid_digitwise(n):
    return all(d in '1379' for d in str(n))

def count_circular_primes(limit):
    prime_flags = sieve(limit)
    primes = {i for i, is_p in enumerate(prime_flags) if is_p}
    
    circular_primes = set()

    for p in primes:
        if p in circular_primes:
            continue
        if p > 10 and not is_valid_digitwise(p):
            continue
        rotations = get_rotations(p)
        if all(rot in primes for rot in rotations):
            circular_primes.update(rotations)
    
    return len(circular_primes)

print(count_circular_primes(1000000))

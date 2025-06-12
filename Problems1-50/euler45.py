import math

def is_pentagonal(x):
    discriminant = 24 * x + 1
    root = math.isqrt(discriminant) # Use integer square root to avoid float rounding issues

    return root * root == discriminant and (1 + root) % 6 == 0

def answer(n):
    """Find the next number after hexagonal index n that is also pentagonal."""
    h = n + 1
    while True:
        hex_num = h * (2 * h - 1)
        if is_pentagonal(hex_num):
            return hex_num
        h += 1

if __name__ == '__main__':
    print(answer(143))





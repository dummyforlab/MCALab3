def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def print_mersenne_primes(limit):
    print(f"Mersenne primes less than {limit}:")
    for p in range(2, limit):
        if is_prime(p):
            m = 2**p - 1
            if is_prime(m):
                print(f"2^{p} - 1 = {m}")

# Example usage
limit = int(input("Find Mersenne primes with p less than: "))
print_mersenne_primes(limit)

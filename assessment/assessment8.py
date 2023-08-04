def checkPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def twinPrime():
    twin_primes = []
    for num in range(3, 1000, 2):
        if checkPrime(num) and checkPrime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

twin_prime_list = twinPrime()

print("Twin Primes less than 1000:")
for twin_prime in twin_prime_list:
    print(twin_prime[0], twin_prime[1])


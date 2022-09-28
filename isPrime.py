def isPrime(num):
    for number in range(2, num):
        if num % number == 0:
            return False
    return True

print(isPrime(8))    
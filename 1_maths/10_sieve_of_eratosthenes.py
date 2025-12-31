# print all prime numbers upto n

# naive: go from 2 to n+1 and see which is prime and print it

# create a boolean mask(True) of len n+1 and start putting false for multiples of primes

def sieve(n):
    if n <= 1:
        return
    
    isPrime = [True] * (n+1)

    i = 2

    while i*i <= n:
        if isPrime[i]:
            for j in range(2*i, n+1, i):
                isPrime[j] = False
        i+=1

    for i in range(2,n+1):
        if isPrime[i]:
            print(i, end=" ")
            
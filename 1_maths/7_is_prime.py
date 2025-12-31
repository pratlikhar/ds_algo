def naive_is_prime(n): #T(n) = O(n)
    if n==1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

# divisors always appear in pair

def is_prime(n): #T(n) = O(sqrt(n))
    if n==1:
        return False
    
    i = 2

    while i ** 2 <= n:
        if n%i == 0:
            return False
        
        i+=1

    return True
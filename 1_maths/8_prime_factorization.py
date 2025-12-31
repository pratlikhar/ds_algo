def is_prime(n):
    if n==1:
        return False
    
    i = 2

    while i**2 <= n:
        if n%i == 0:
            return False
        i+=1

    return True

def print_factors(n):

    for i in range(2,n):
        if is_prime(i):
            x = i
            while n%x == 0:
                print(i)
                x = x*i




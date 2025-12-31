# naive: run a loop from 1 to n+1 and print if n%i == 0, Theta(n)

# divisors always appear in pairs, so we only need to check till sqrt(n)

def print_divisors(n): # Theta(sqrt(n)), but not printed in sorted order
    i = 1
    while i*i <= n:
        if n%i == 0:
            print(i)
            if i != (n//i):
                print(n//i)
        i+=1

def print_divisors_sorted(n):
    i = 1
    while i*i <=n:
        if n%i == 0:
            print(i)
        i+=1
    while i >= 1:
        if n%(i) == 0: # or n%(n//i) == 0 , eitherway is fine
            print(n//i)
        i-=1
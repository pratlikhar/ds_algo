def naive_lcm(a,b): # T(a,b) = Theta(a*b-max(a,b))
    res = max(a,b)

    while True:
        if res%a == 0 and res %b == 0:
            return res
        
        res += 1

    return res

def gcd(a,b):
    if b==0:
        return a
    
    return gcd(b, a%b)

def efficient_lcm(a,b):

    return (a*b) // gcd(a,b)
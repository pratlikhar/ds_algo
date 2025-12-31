def eucledian_gcd_hcf(a, b):
    while a != b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a # we can return either a or b

def optimized_euclidean_gcd_hcf(a, b):
    if b == 0:
        return a
    
    return optimized_euclidean_gcd_hcf(b, a%b)

print(eucledian_gcd_hcf(12,15))
print(optimized_euclidean_gcd_hcf(12,15))
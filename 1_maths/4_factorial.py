def factorial(num: int) -> int: # T(n) = Theta(n), S(n) = Theta(1)
    factorial = 1

    while num > 0:
        factorial = factorial * num
        num -= 1

    return factorial

def recursive_factorial(num): # T(n) = T(n-1) + Theta(1), S(n) = Theta(n)
    if num == 0:
        return 1
    
    return num * recursive_factorial(num-1)

print(factorial(4))
print(factorial(2))
print(factorial(5))

print(recursive_factorial(4))
print(recursive_factorial(2))
print(recursive_factorial(5))
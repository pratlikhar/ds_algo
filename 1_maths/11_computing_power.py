# naive: go from 1 to n and multiply x each time

# for O(log(n)) for both time and space

def power(x, n):
    if n == 0:
        return 1
    
    temp = power(x, n//2)
    temp = temp * temp

    if n%2 == 0:
        return temp
    else:
        return temp*x
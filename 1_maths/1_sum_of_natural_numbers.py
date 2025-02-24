def sum_of_first_n_natural_numbers(n: int) -> int:
    """
    Computes sum of first n natural numbers

    Args:
        n: input
    """

    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum

def sum_of_first_n_natural_numbers_2(n: int) -> int:
    """
    Computes sum of first n natural numbers

    Args:
        n: input
    """

    return (n*(n+1))/2

print(sum_of_first_n_natural_numbers(5))
print(sum_of_first_n_natural_numbers_2(5))
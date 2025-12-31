def count_digits(num: int) -> int:
    digits = 0

    while num > 0:
        digits += 1
        num = num // 10

    return digits

print(count_digits(3000))
print(count_digits(200))
print(count_digits(143562))
print(count_digits(7))
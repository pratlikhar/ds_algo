def is_pal(num: int) -> bool:
    rev_num = 0
    temp = num

    while temp != 0:
        ld = temp % 10

        rev_num = rev_num * 10 + ld

        temp = temp // 10

    return rev_num == num

print(is_pal(12321))
print(is_pal(7))
print(is_pal(1243))
    
def left_rotate_by_d(lst, d):
    return lst[d:] + lst[:d]

def left_rotate_by_d_2(l, d):
    for i in range(d):
        l.append(l.pop(0))
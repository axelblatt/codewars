def last_digit(n1, n2):
    if n2 == 0:
        return 1
    md = n2 % 4
    if md == 1:
        return n1 % 10
    if md == 2:
        return (n1 ** 2) % 10
    if md == 3:
        return (n1 ** 3) % 10
    if md == 0:
        if n1 % 10 == 5:
            return 5
        if n1 % 10 == 6:
            return 6
        if n1 % 10 == 0:
            return 0
        if n1 % 2 != 0:
            return 1
        else:
            return 6
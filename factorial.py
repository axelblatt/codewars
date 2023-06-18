def factorial(n):
    if 12 >= n >= 0:
        f = 1;
        for i in range(1, n + 1): f = f * i;
        return f;
    else:
        raise ValueError;
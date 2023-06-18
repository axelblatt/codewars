def count_bits(n):
    b = '';
    summary = 0;
    while n != 0:
        b += str(n % 2);
        n = n // 2;
    b = b[::-1];
    for i in range(len(b)):
        if b[i] == '1':
            summary += 1;
    return summary;
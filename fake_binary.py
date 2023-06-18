def fake_bin(x):
    a = list(str(x));
    r = '';
    for i in range(len(a)):
        if int(a[i]) < 5: r += '0';
        else: r += '1';
    return r;
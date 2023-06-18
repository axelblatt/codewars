def flip(d, a):
    # Do some magic
    if d == 'R':
       a.sort();
    if d == 'L':
       a.sort(reverse=True);
    return a;
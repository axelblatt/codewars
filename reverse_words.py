def reverse_words(s):
    f = s.split(' ')[::-1];
    s = '';
    for i in f: s += i + ' ';
    return s[0:-1];
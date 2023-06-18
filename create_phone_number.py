def create_phone_number(n):
    o = [(0, '('), (4, ') '), (8, '-')];
    for i in o: n.insert(i[0], i[1]);
    number = '';
    for i in n: number += str(i);
    return number;
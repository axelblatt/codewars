def pig_it(text):
    words = text.split(' ');
    result = '';
    for i in words:
        if len(i) > 1 or i == 'O' or i == 'o':
            i1 = i[1:];
            last_letter = i[0];
            result += i1 + last_letter + 'ay' + ' ';
        else:
            result += i;
    if result[-1] == ' ':
        result = result[0:-1];
    return result;
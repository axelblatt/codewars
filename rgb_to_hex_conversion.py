def rgb(r, g, b):
    array = [r, g, b];
    res = '';
    for i in range(len(array)):
        if array[i] <= 0:
            array[i] = hex(0);
        elif array[i] >= 255:
            array[i] = hex(255);
        else:
            array[i] = hex(array[i]);
        array[i] = array[i].replace('0x', '');
        if len(array[i]) < 2: array[i] = '0' + array[i];
        res += array[i];
    return res.upper();
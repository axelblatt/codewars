def to_camel_case(text):
    txt = '';
    i = 0;
    while i < len(text):
        if text[i] == '-' or text[i] == '_':
            txt += text[i + 1].upper();
            i += 2;
        else:
            txt += text[i];
            i += 1;
    return txt;
def generate_hashtag(s):
    s = '#' + s.title().replace(' ', '');
    return False if (len(s) == 1 or len(s) >= 140) else s;
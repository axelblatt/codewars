def likes(names):
    if len(names) > 3:
        likes = names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this';
        return likes;
    if len(names) == 3:
        likes = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this';
        return likes;
    if len(names) == 2:
        likes = names[0] + ' and ' + names[1] + ' like this';
        return likes;
    if len(names) == 1:
        likes = names[0] + ' likes this';
        return likes;
    else:
        likes = 'no one likes this';
        return likes;
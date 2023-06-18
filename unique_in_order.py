from itertools import groupby;
def unique_in_order(iterable):
    return [el for el, _ in groupby(iterable)];
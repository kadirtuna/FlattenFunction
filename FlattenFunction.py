from collections.abc import Iterable

def flatten(list):
    for x in list:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

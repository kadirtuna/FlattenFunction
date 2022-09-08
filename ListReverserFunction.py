from collections.abc import Iterable

def listReverserFunc(list):
    list.reverse()

    for x in list:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from listReverserFunc(x)
        else:
            yield x


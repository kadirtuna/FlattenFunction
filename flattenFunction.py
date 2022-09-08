from collections.abc import Iterable

def flatten(list):
    for x in list:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


#An example ragged nested list to be converted to a flatten list.

"""
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(list(flatten(list1)))
"""
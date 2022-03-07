def descending_order(num):
    if isinstance(num, int) and num >= 0:
        listed = str(num)
        descend = sorted(listed, reverse=True)
        return int("".join(descend))
    else:
        raise ValueError('Non-negative integer expected')


result = descending_order(12875)
print(result)

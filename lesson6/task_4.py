def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


print(get_nod(10, 15))

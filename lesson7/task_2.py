def even(x: int):
    if x > 0:
        return True
    return False


numbers = [-1, 0, 1, 2, 3]


print(list(filter(even, numbers)))

print(list(filter(lambda x: x > 0, numbers)))

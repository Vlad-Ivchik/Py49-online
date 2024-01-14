from functools import reduce


def square(x):
    return x["length"] * x["width"]


def summary(a, b):
    return a + b


rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

print(reduce(summary, list(map(square, rooms))))

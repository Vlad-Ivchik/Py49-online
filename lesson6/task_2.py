def function(x, y):
    while x > 0:
        z = x % 2
        y = str(z) + y
        x = x // 2

    print(y)


function(27, '')

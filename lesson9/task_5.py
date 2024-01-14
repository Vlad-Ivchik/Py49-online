with open("class.txt") as file:
    summary = 0
    counter = 0
    for i in file:
        i = i.split()
        y = int(i[2])
        summary += y
        counter += 1
        if y < 3:
            print(*i)

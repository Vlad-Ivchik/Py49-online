# string = 'Привет как дела, привет отлично, привет отлично'
with open("123.txt") as string:
    string = string.read()


def finder(string):
    words = string.lower().split()
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    print(max(counter.values()))

    return max(counter, key=counter.get)


print(finder(string))

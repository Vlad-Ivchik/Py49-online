with open("primer.txt") as s:
    s = s.read()

    length = len(s)
    integers = []
    i = 0  # индекс текущего символа

    while i < length:
        s_int = ''  # строка для нового числа
        while i < length and '0' <= s[i] <= '9':
            s_int += s[i]
            i += 1
        i += 1
        if s_int != '':
            integers.append(int(s_int))

    print(sum(integers))

har_at(str, n):
    new = []
    for i in range(len(str)):
        if i != n:
            new.append(str[i])
    return ''.join(new)

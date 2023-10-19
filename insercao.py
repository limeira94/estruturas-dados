def insercao(v):
    for j in range(1, len(v)):
        x = v[j]
        i = j -1
        while i >= 0 and v[i] > x:
            v[i + 1] = v[i]
            i = i - 1
            v[i + 1] = x
    return v

if __name__ == '__main__':
    v = [1, 0, 2, 6, 3, 4, 7, 5]
    insercao(v)
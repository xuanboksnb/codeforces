#Vanya and cubes


if __name__ == '__main__':
    n = int(raw_input())
    h = 0
    x = 1
    t = 1
    while n >= 0:
        n = n - x
        if n >= 0:
            h += 1
            t += 1
            x += t
        else:
            break
    print h

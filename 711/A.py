"""
Bus to Udayland
"""


def check(a):
    b = [i.split('|') for i in a]
    check_v = "NO"
    for i in range(len(b)):
        if b[i][0] == 'OO':
            b[i] = ("++", b[i][1])
            check_v = "YES"
            break
        if b[i][1] == 'OO':
            b[i] = (b[i][0], "++")
            check_v = "YES"
            break
    if check_v == "NO":
        return check_v
    x = ["%s|%s"%(i[0], i[1]) for i in b]
    return check_v + '\n' + '\n'.join(x)


if __name__ == '__main__':
    n = int(raw_input())
    a = list()
    for i in range(n):
        a.append(raw_input())
    print check(a)

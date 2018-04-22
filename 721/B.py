

if __name__ == '__main__':
    s = raw_input().split()
    n = int(s[0])
    k = int(s[1])
    passwords = dict()
    for i in range(n):
        s = raw_input()
        if len(s) in passwords:
            passwords[len(s)].append(s)
        else:
            passwords[len(s)] = [s]
    passw = raw_input()
    keys = sorted(passwords.keys())
    i = 0
    ky = keys[0]
    it = 0
    while ky < len(passw):
        it += len(passwords[ky])
        i += 1
        ky = keys[i]
    min_x = it + 1 + 5 * ((it) / k)
    it += len(passwords[ky])
    # print it
    # print k
    max_x = it + 5 * ((it - 1) / k)
    print min_x, max_x
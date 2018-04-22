"""

"""


def print_matrix(a):
    for a1 in a:
        s = [str(i) for i in a1]
        print ' '.join(s)


def find_matrix(n):
    result = [[0 for i in range(n)] for j in range(n)]
    p = n/2
    # result[p][p] = 1
    l = 1
    c = 2
    for i in range(p + 1):
        x = p - i
        y = p + i
        if i % 2 == 0:
            for t in range(n):
                if result[x][t] == 0:

                    result[x][t] = l
                    l += 2
                if result[t][x] == 0:
                    result[t][x] = l
                    l += 2

                if result[y][t] == 0:
                    result[y][t] = l
                    l += 2
                if result[t][y] == 0:
                    result[t][y] = l
                    l += 2
        else:
            for t in range(n):
                if result[x][t] == 0:
                    result[x][t] = c
                    c += 2
                if result[t][x] == 0:
                    result[t][x] = c
                    c += 2

                if result[y][t] == 0:
                    result[y][t] = c
                    c += 2
                if result[t][y] == 0:
                    result[t][y] = c
                    c += 2
        # print_matrix(result)
        # print "======================"
    return result


if __name__ == '__main__':
    # a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(find_matrix(int(raw_input())))

# Batch Sort
import pprint

def check_number_wrong(a):
    count = 0
    for i in range(len(a)):
        if a[i] != (i + 1):
            count += 1
    return count


def check(matrix):
    for row in matrix:
        count = check_number_wrong(row)
        # print count
        if count > 2:
            return False
    return True


def main(matrix, n, m):
    if check(matrix):
        return True
    for i in range(m - 1):
        for j in range(i + 1, m):
            # pprint.pprint(matrix)
            # print "swap %s to %s" % (i, j)
            for row in matrix:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp
            # pprint.pprint(matrix)
            if check(matrix):
                return True
            for row in matrix:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp
            # print "==================="
    return False


if __name__ == '__main__':
    s = raw_input().split()
    n = int(s[0])
    m = int(s[1])
    matr = list()
    for i in range(n):
        row = raw_input().split()
        row = [int(it) for it in row]
        matr.append(row)
    if main(matr, n, m):
        print "YES"
    else:
        print "NO"

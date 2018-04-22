"""

"""


def check_power_2(number):
    # print "=============  %s  ============" % number
    while number > 1:
        # print number
        if number & 1:
            return False
        number >>= 1
    return True


def count_pair(a):
    result = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            s = a[i] + a[j]
            if check_power_2(s):
                result += 1
    return result


if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input().split()
    a = [int(i) for i in s]
    print count_pair(a)
    pass
    # print 11 >> 1

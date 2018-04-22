# Transformation: from A to B


def transform(a, b):
    result = [b]
    while b > a:
        if b % 2 == 0:
            b /= 2
        elif (b - 1) % 10 == 0:
            b = (b - 1) / 10
        else:
            return None
        result.append(b)
        # print b
    if b == a:
        result.reverse()
        return result
    else:
        return None


if __name__ == '__main__':
    s = raw_input().split()
    a = int(s[0])
    b = int(s[1])
    result = transform(a, b)
    if result is None:
        print "NO"
    else:
        print "YES"
        print len(result)
        print " ".join(str(i) for i in result)
        # print s

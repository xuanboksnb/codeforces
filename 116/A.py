# Tram


if __name__ == '__main__':
    n = int(raw_input())
    result = 0
    current = 0
    for i in range(n):
        s = raw_input().split()
        a = int(s[0])
        b = int(s[1])
        current = current - a + b
        if current > result:
            result = current
    print result
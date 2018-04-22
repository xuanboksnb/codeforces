if __name__ == '__main__':
    n = int(raw_input())
    result = 0
    for i in range(n):
        s = raw_input().split()
        if int(s[1]) - int(s[0]) >= 2:
            result += 1
    print result

if __name__ == '__main__':
    n = int(raw_input())
    c = 0
    for i in xrange(n):
        s = raw_input().split(" ")
        x = int(s[0])
        y = int(s[1])
        if x > 0:
            c += 1
    if c <= 1 or n - c <= 1:
        print "Yes"
    else:
        print "No"

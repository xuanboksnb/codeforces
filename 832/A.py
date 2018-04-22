n, k = raw_input().split()
n, k = int(n), int(k)

s = n / k

if s % 2 == 1:
    print "YES"
else:
    print "NO"

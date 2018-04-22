# coding=utf-8
"""
D. Two Arithmetic Progressions
You are given two arithmetic progressions: a1k + b1 and a2l + b2. Find the number of integers x such that L ≤ x ≤ R and x = a1k' + b1 = a2l' + b2, for some integers k', l' ≥ 0.

Input
The only line contains six integers a1, b1, a2, b2, L, R (0 < a1, a2 ≤ 2·109,  - 2·109 ≤ b1, b2, L, R ≤ 2·109, L ≤ R).

Output
Print the desired number of integers x.
"""


def uscln(a, b):
    if b > a:
        b = a + b
        a = b - a
        b = b - a
    while b > 0:
        q = a / b
        r = a % b
        a = b
        b = r
        # print a, b
    return a


def count_x(a1, b1, a2, b2, L, R):
    x = max(b1, b2)
    if L < x:
        L = x

    b1 = b1 % a1
    b2 = b2 % a2
    s = a1 * a2 / uscln(a1, a2)
    x = max(b1, b2)
    if L < x:
        L = x
    p = 0
    for i in range(s):
        t = i + x
        if (t - b1) % a1 == 0 and (t - b2) % a2 == 0:
            p = i
            break
        pass
    # print s
    # print p
    min_x = ((L - 1 - p) / s + 1) * s + p
    # print L
    # print min_x
    d = R - min_x
    result = d / s + 1
    if result < 0:
        return 0
    return result


if __name__ == '__main__':
    s = raw_input().split()
    a1 = int(s[0])
    b1 = int(s[1])
    a2 = int(s[2])
    b2 = int(s[3])
    L = int(s[4])
    R = int(s[5])
    print count_x(a1, b1, a2, b2, L, R)

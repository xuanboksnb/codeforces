"""

"""


def timer_count(n, x, y):
    p = n / 2
    if (n - p) * x <= y:
        return n * x
    return x * (n % 2) + y + timer_count(n / 2, x, y)


if __name__ == '__main__':
    s = raw_input().split()
    print timer_count(int(s[0]), int(s[1]), int(s[2]))
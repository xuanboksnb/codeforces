"""
Optimal Point on a Line
"""


def get_optimal(a):
    a = sorted(a)
    p = (len(a) - 1) / 2
    return a[p]


if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input().split()
    s = [int(i) for i in s]
    print get_optimal(s)

# Anton and Digits


def max_compose(num2, num3, num5, num6):
    num256 = min(num2, num5, num6)
    num2 -= num256
    num32 = min(num2, num3)
    return num256 * 256 + num32 * 32


if __name__ == '__main__':
    s = raw_input().split()
    num2 = int(s[0])
    num3 = int(s[1])
    num5 = int(s[2])
    num6 = int(s[3])
    print max_compose(num2, num3, num5, num6)
    
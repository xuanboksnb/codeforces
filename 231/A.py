# Team


if __name__ == '__main__':
    n = int(raw_input())
    result = 0
    for i in range(n):
        s = raw_input().split()
        if len([it for it in s if it == "1"]) >= 2:
            result += 1
    print result

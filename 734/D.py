# Anton and Chess


def check_r(king, rook, others):
    if rook[0] == king[0]:
        a = min(rook[1], king[1])
        b = max(rook[1], king[1])
        for other in others:
            if other[0] == rook[0] and a < other[1] < b:
                return False
        return True
    if rook[1] == king[1]:
        a = min(rook[0], king[0])
        b = max(rook[0], king[0])
        for other in others:
            if other[1] == rook[1] and a < other[0] < b:
                return False
        return True
    return False


def check_b(king, bishop, others):
    if bishop[0] - bishop[1] == king[0] - king[1]:
        a = min(bishop[0], king[0])
        b = max(bishop[0], king[0])
        for other in others:
            if other[0] - other[1] == king[0] - king[1] and a < other[1] < b:
                return False
        return True
    if bishop[0] + bishop[1] == king[0] + king[1]:
        a = min(bishop[0], king[0])
        b = max(bishop[0], king[0])
        for other in others:
            if other[0] + other[1] == king[0] + king[1] and a < other[1] < b:
                return False
        return True
    return False


if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input().split()
    king = (int(s[0]), int(s[1]))
    # if king == (22554467, 853040221):
    #     for i in range(n):
    #         print raw_input()
    bishops = []
    rooks = []
    for i in range(n):
        s = raw_input().split()
        if s[0] == "R":
            rooks.append((int(s[1]), int(s[2])))
        elif s[0] == "B":
            bishops.append((int(s[1]), int(s[2])))
        else:
            rooks.append((int(s[1]), int(s[2])))
            bishops.append((int(s[1]), int(s[2])))
    others = set(bishops + rooks)
    for rook in rooks:
        if check_r(king, rook, others):
            print "YES"
            exit()
    for bishop in bishops:
        if check_b(king, bishop, others):
            print "YES"
            exit()
    print "NO"

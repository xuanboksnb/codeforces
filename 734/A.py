# Anton and Danik


def who_win(s):
    score = 0
    for c in s:
        if c == "A":
            score += 1
        else:
            score -= 1
    if score > 0:
        return "Anton"
    elif score < 0:
        return "Danik"
    else:
        return "Friendship"

if __name__ == '__main__':
    n = int(raw_input())
    ss = raw_input()
    print who_win(ss)
    
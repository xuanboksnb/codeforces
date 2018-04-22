"""
King Moves
"""


# map_col = {'a':1, 'b':2, 'c':3, }

def num_move(x, y):
    x -= 1
    y = ord(y) - ord('a')
    c = 0
    if 0 < x < 7:
        c += 1
    if 0 < y < 7:
        c += 1
    if c == 0:
        return 3
    if c == 1:
        return 5
    return 8


if __name__ == '__main__':
    s = raw_input()
    print num_move(int(s[1]), s[0])
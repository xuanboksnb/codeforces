"""

"""


def find_maximum_increase(a):
    max_len = 1
    prev_value = a[0]
    current_len = 1
    # if len(a) == 1:
    #     return 1
    for i in range(1, len(a)):
        # print current_len, '\t', prev_value
        if a[i] > prev_value:
            current_len += 1
            prev_value = a[i]
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1
            prev_value = a[i]
    if current_len > max_len:
        max_len = current_len
    # print max_len
    return max_len


if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input().split()
    a = [int(i) for i in s]
    print find_maximum_increase(a)
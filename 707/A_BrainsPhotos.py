"""

"""


def check_color_photo(a):
    color_choose = {'C', 'M', 'Y'}
    for row in a:
        for cell in row:
            if cell in color_choose:
                return True
    return False


if __name__ == '__main__':
    size_str = raw_input().split()
    no_row = int(size_str[0])
    no_col = int(size_str[1])
    color_matrix = list()
    for i in range(no_row):
        colors_row = raw_input().split()
        color_matrix.append(colors_row)
    if check_color_photo(color_matrix):
        print "#Color"
    else:
        print "#Black&White"
        
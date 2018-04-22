# Petya and String


if __name__ == '__main__':
    first_str = raw_input()
    second_str = raw_input()
    if first_str.lower() < second_str.lower():
        print "-1"
    elif first_str.lower() == second_str.lower():
        print "0"
    else:
        print "1"
        
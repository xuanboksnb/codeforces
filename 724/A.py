# Checking the Calendar


# month_day = [31, 28, 31, 30, 31, ]
candidate = [3, 0, 2]
day_to_int = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}


def check(x, y):
    if (x > y):
        y += 7
    if y - x in candidate:
        return True
    return False


if __name__ == '__main__':
    day_1 = raw_input()
    day_2 = raw_input()
    if check(day_to_int[day_1], day_to_int[day_2]):
        print "YES"
    else:
        print "NO"

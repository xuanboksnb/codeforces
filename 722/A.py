

if __name__ == '__main__':
    # s = "12"
    # print s[1]
    time_format = int(raw_input())
    hour_minute = raw_input().split(":")
    hour = hour_minute[0]
    minute = hour_minute[1]
    if time_format == 12:
        if hour[0] == "0":
            if hour[1] == "0":
                hour = "01"
        elif hour[0] == "1":
            if hour[1] > "2":
                hour = hour[0] + "0"
        else:
            if hour[1] == "0":
                hour = "10"
            else:
                hour = "0" + hour[1]
    else:
        if hour[0] == "2":
            if hour[1] > "3":
                hour = hour[0] + "0"
        elif hour[0] > "2":
                hour = "1" + hour[1]
    if minute[0] > "5":
        minute = "0" + minute[1]
    print "%s:%s" % (hour, minute)

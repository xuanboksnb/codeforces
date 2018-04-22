# import re

_s = raw_input()
chs = set(_s)
pattern = raw_input()
# pattern = pattern.replace("?", "[%s]" % _s)
# pattern = pattern.replace("*", "[^%s]*" % _s)
# print pattern
q = int(raw_input())
for i in xrange(q):
    s = raw_input()
    check = True
    _is = 0
    _ip = 0
    while _ip < len(pattern):
        if pattern[_ip] == "?":
            # print pattern[_ip], s[_is]
            if _is >= len(s):
                check = False
                break
            if s[_is] not in chs:
                check = False
                break
        elif pattern[_ip] == "*":
            _ch = True
            for _it in range(len(s) - len(pattern)):
                # print pattern[_ip], s[_is]
                if _is < len(s):
                    if s[_is] in chs:
                        _ch = False
                        break
                _is += 1
            if not _ch:
                check = False
                break
        else:
            if _is >= len(s):
                check = False
                break
            # print pattern[_ip], s[_is]
            if s[_is] != pattern[_ip]:
                check = False
                break
        _is += 1
        _ip += 1
    if check:
        print "YES"
    else:
        print "NO"
    # for it in xrange(len(s)):
    #
    # t = s.find()
    # head =
    # m = re.match(pattern, s)
    # if not m:
    #     print "YES"
    # else:
    #     print "NO"

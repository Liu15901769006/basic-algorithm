# coding=utf-8
def longestcommonprefix(strs):
    y = strs[0]
    length = len(y)
    for x in strs:
        if len(x) < length:
            length = len(x)
    i = 1
    flag = 0
    loca = 1
    while i <= length:
        ex = y[:i]
        for x in strs:
            if x[:i] != ex:
                flag = 1
                loca = i - 1
                break
        if flag == 1:
            break
        else:
            i = i + 1

    if loca < 1:
        return ''
    else:
        return y[:loca]


strs = ["adbcf"]
print(longestcommonprefix(strs))

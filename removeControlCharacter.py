def removeControlCharacter(s):

    ret = ''
    for c in s:
        ord_num = ord(c)

        if(ord_num <= 31):
            a = 1234

        else:
            ret += c

    return ret


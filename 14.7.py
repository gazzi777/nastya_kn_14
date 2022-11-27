for x in '012345678':
    for y in '0123456':
        t = int(y + x + '320', 7) + int('1' + x + '3' + y + '3', 9)
        if t % 181 == 0:
            print(t // 181)
            break

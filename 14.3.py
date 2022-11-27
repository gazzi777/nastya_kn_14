for x in '0123456789ABCDEFGHIK':
    t = int('2' + x + '84', 19) + int('2B3' + x, 16)
    if t % 88 == 0:
        print(t // 88)
        break

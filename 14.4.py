for x in '0123456789ABCDEFGKL':
    t = int('4C' + x + '4', 15) + int(x + '62A', 13)
    if t % 121 == 0:
        print(t // 121)
        break

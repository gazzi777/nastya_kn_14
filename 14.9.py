for x in '0123456789ABCD':
    for y in '0123456789AB':
        t = int(y + 'AA'+x, 12) + int(x + '02' + y, 14)
        if t % 80 == 0:
            print(t // 80)
            break

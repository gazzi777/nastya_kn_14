for x in '0123456789AB':
    t = int('95' + x + '2', 11) + int(x + '458', 12)
    if t % 136 == 0:
        print(t // 136)
        break

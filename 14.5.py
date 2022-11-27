for x in '0123456789ABCDEFGH':
    t = int(x + 'B09', 17) + int(x + '8E8', 15)
    if t % 155 == 0:
        print(t // 155)
        break

for x in '0123456789ABCDE':
    t = int('28' + x + '2', 18) + int('93' + x + '5', 12)
    if t % 133 == 0:
        print(t // 133)
        break

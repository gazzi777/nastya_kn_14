for x in '012345678':
    for y in '01234567':
        t = int(x + '01' + y + '4', 9) + int(x + y + '544', 8)
        if t % 89 == 0:
            print(t // 89)
            break
        

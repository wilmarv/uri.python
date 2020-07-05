a, b, c = map(int, input().split())
ab = (a+b+abs(a-b))/2
ac = (a+c+abs(a-c))/2
bc = (b+c+abs(b-c))/2

if ab > ac:
    if ab > bc:
        print('{:.0f} eh o maior'.format(ab))
    else:
        print('{:.0f} eh o maior'.format(bc))
else:
    if ac > bc:
        print('{:.0f} eh o maior'.format(ac))
    else:
        print('{:.0f} eh o maior'.format(bc))
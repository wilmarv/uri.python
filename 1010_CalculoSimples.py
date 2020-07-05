t = 0
for p in range(0, 2):
    c, n, v = map(float, input().split())
    t += n*v
print('VALOR A PAGAR: R$ {:.2f}'.format(t))

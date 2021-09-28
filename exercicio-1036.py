a, b, c = [float(x) for x in input().split()]

delta = (b ** 2) - (4 * a * c)

if delta > 0 and a != 0:
    print('R1 = {:.5f}'.format((-b + delta**0.5)/(2 * a)))
    print('R2 = {:.5f}'.format((-b - delta**0.5)/(2 * a)))
else: 
    print('Impossivel calcular')
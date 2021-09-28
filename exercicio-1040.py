n1, n2, n3, n4 = [float(x) for x in input().split()]

m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1) ) / 10

print('Media: {:.1f}'.format(m))

if (m >= 7.0): 
    print('Aluno aprovado.')
elif (m < 5.0): 
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nexame = float(input())
    print('Nota do exame: {:.1f}'.format(nexame))
    m = (m + nexame)/2.0
    if (m >= 5.0): 
        print('Aluno aprovado.')
    else: 
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(m))
#Números sequenciais
a = int(input('Entre com um número: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1           #" += 1 " é o código simplificado ou seja, estou afirmando que ele recebe o 1 mais ele mesmo.
                           #div + 1
if div == 2:
    print('O número {} é primo'.format(a))
else:
    print('O número {} não é primo'.format(a))

# for x in range(101):
#     print(x)

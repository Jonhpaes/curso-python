a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado!'
                  '\nDigite novamente, primeiro bimestre: '))
b = int(input('Segundo bimestre'))
if b > 10:
    b = int(input('Você digitou errado!'
                  '\nDigite novamente, segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado!'
                  '\nDigite novamente, terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado!'
                  '\nDigite novamente, quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))



# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Sua média é de: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada!')
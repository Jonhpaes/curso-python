# Usando WHILE para forçar o usuário a digitar correto no campo exigido.


a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado!'
                  '\nDigite novamente, primeiro bimestre: '))
b = int(input('Segundo bimestre'))
while b > 10:
    b = int(input('Você digitou errado!'
                  '\nDigite novamente, segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado!'
                  '\nDigite novamente, terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado!'
                  '\nDigite novamente, quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))



# nota = int(input('Entre com uma nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida.Entre com a nota correta: '))
# a = 0
# while a <= 10:
#     print(a)
#     a += 1
# Usando WHILE para forçar o usuário a digitar correto no campo exigido.


a = float(input('Primeiro bimestre: '))
while a > 10:
    a = float(input('Você digitou errado!'
                  '\nDigite novamente, primeiro bimestre: '))
b = float(input('Segundo bimestre'))
while b > 10:
    b = float(input('Você digitou errado!'
                  '\nDigite novamente, segundo bimestre: '))
c = float(input('Terceiro bimestre: '))
while c > 10:
    c = float(input('Você digitou errado!'
                  '\nDigite novamente, terceiro bimestre: '))
d = float(input('Quarto bimestre: '))
while d > 10:
    d = float(input('Você digitou errado!'
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


# usamos " Float " para podermos usar qualquer número, ou seja número com virgula ou número real
# usamos " Int " para podermos usar apenas números inteiros
i = float(input('Qual foi o seu investimento inicial na sua empresa? '))
a = float(input('qual foi o lucro da sua empresa no ano de 2020? '))
b = float(input('Qual foi o lucro da sua empresa no ano de 2021? '))

soma = a + b
total = i + soma

faturamento = ('O seu lucro dos anos de 2020 e 2021 é de: {soma}.'
               '\nO valor total do investimento mais o lucro dos dois anos, da no valor de: {total}.'
               .format(soma=soma,
                       total=total))
print(faturamento)
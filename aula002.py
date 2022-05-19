print('O número das contas abaixo usado foi 10 e 5.'
      '\n')
a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('soma: {soma}.'
      '\nSubtração: {sub}.'
      '\nMultiplicação: {multiplicacao}.'
      '\nDivisão: {divisao}.'
      '\nResto da divisao: {resto}.'
      .format(soma=soma,
              sub=subtracao,
              multiplicacao=multiplicacao,
              divisao=divisao,
              resto=resto))
# print('soma: '+ str (soma))
# também posso usar a virgúla dpois das aspas, ex: print('soma: ',+ soma)
#
# print('subtracao: ' + str(subtracao))
# print(multiplicacao)
# print(int(divisao))
# print(divisao)
# print(resto)
# x = 1
# soma2 = int(x) + 1
# print(soma2)
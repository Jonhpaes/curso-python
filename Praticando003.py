a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = (
      'soma: {soma}.'
      '\nSubtração: {sub}.'
      '\nMultiplicação: {multiplicacao}.'
      '\nDivisão: {divisao}.'
      '\nResto: {resto}.'
      .format(soma=soma,
              sub=subtracao,
              multiplicacao=multiplicacao,
              divisao=divisao,
              resto=resto))
print(resultado)
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or resto_b == 0: #Para reverter podemos usar desse jeito " if resto_a == 0 or not resto_b > 0: "
                                # podemos ver que foi alterado o código, foi adicionado um " not " e " == " foi
                                # trocado para " > ", ou seja fica como se fosse falso e não verdadeiro.
    print('foi digitado um número par')
else:
    print('nenhum número par foi digitado')
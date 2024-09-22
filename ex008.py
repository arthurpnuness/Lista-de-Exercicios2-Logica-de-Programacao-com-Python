'''Divisores de um Número:

Escreva um programa que solicite um número inteiro positivo n do usuário e mostre todos os divisores de n.'''

def divisoresNumero():
    
    # Laço que verifica se o numero é inteiro e positivo
    while True:
            # Solicita um número inteiro positivo do usuário
            num = int(input('Digite um número inteiro positivo: '))
            if num >= 0:
                  break
            else:
                print('Por favor digite um numero maior que ZERO !!!!!')

    # Lista vazia para armazenar divisores
    divisores = []

    # Verifica cada número entre 1 e o número fornecido
    for i in range(1, num + 1):
        if num % i == 0:  # Se num for divisível por i, é divisor
            divisores.append(i)

    # Exibe a lista de divisores
    print(f'Os divisores de {num} são: {divisores}')

divisoresNumero()

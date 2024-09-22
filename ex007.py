'''Números Primos:

Desenvolva um programa que receba um número inteiro positivo do usuário e verifique se ele é um número primo.'''

def numeroPrimo():
    
    # Laço que verifica se o numero é inteiro e positivo
    while True:
            
        # Solicita um número inteiro positivo do usuário
        num = int(input('Digite um número inteiro positivo: '))

        if num > 0:
                break
        else:
                print('Por favor digite um numero maior que ZERO !!!!!')

    # Se o número for menor que 2, não pode ser primo
    if num < 2:
        print(f'{num} não é primo.')
        return

    # Laço que verifica divisores entre 2 e o número-1
    for i in range(2, num):
        if num % i == 0:  # Se num for divisível por i, não é primo
            print(f'{num} não é primo.')
            return
    
    # Se o laço não encontrar divisores, o número é primo
    print(f'{num} é primo.')

numeroPrimo()

'''Contagem Regressiva:

Crie um programa que solicite um número inteiro positivo e exiba uma contagem regressiva desse número até zero.'''


def contagemRegressiva():
    
    # Laço que verifica se o numero é inteiro e positivo
    while True:
                # Solicita um número inteiro positivo do usuário
            num = int(input('Digite um numero inteiro positivo: '))
            if num > 0:
                  break
            else:
                print('Por favor digite um numero maior que ZERO !!!!!')
                
    # Laço que conta regressivamente de num até 0
    for i in range(num, -1, -1):
        print(i)

contagemRegressiva()

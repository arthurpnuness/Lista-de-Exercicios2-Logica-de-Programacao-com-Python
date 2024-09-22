'''Multiplicação Sucessiva:

Crie um programa que solicite dois números inteiros a e b e calcule a multiplicação de a por b utilizando apenas somas sucessivas.'''

def multiplicacaoSucessiva():
    # Solicita dois números inteiros do usuário

    while True:

        a = int(input('Digite o primeiro número (a): '))
        b = int(input('Digite o segundo número (b): '))
        
        if a > 0 and b > 0:
            break
        else:
            print('Insira numeros maiores que ZERO !!!')
    
    resultado = 0  # Inicializa o resultado da multiplicação

    # Laço para somar o valor de a, b vezes
    for _ in range(b):
        resultado += a

    # Exibe o resultado da multiplicação
    print(f'{a} multiplicado por {b} é {resultado}')

multiplicacaoSucessiva()

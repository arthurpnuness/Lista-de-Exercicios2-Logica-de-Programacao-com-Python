'''Maior e Menor em uma Lista:

Faça um programa que solicite ao usuário 5 números inteiros e os armazene em uma lista. O programa deve então exibir o maior e o menor número da lista.'''

def maiorMenorLista():
    
    # Lista vazia para armazenar os números
    numeros = []

    # Solicita 5 números do usuário
    for i in range(5):
        num = int(input(f'Digite o {i + 1}º número: '))
        numeros.append(num)  # Armazena o número na lista

    # Exibe o maior e o menor número da lista
    print(f'O maior número é: {max(numeros)}')
    print(f'O menor número é: {min(numeros)}')

maiorMenorLista()

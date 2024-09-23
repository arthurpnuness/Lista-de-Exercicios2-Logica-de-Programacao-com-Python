'''Cálculo de Média:

Desenvolva um programa que solicite ao usuário uma quantidade de notas e calcule a média das notas inseridas. O programa deve continuar solicitando as notas até que o usuário digite -1.'''


def calculoMedia():
    soma = 0  # Armazena a soma das notas
    quantidade = 0  # Conta quantas notas foram inseridas

    # Solicita notas até o usuário digitar -1
    while True:
        nota = float(input('Digite uma nota ou -1 para sair: '))
        
        if nota == -1:
            break  # Encerra o laço se o usuário digitar -1
        
        soma += nota  # Adiciona a nota à soma
        quantidade += 1  # Incrementa a quantidade de notas

    # Calcula e exibe a média
    if quantidade > 0:
        media = soma / quantidade
        print(f'A média das notas é: {media}')
    else:
        print('Nenhuma nota foi inserida.')

calculoMedia()

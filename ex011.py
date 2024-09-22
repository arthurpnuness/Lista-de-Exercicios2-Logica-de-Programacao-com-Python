import random  # Importa biblioteca para gerar números aleatórios

'''Jogo de Adivinhação:

Escreva um programa que sorteie um número aleatório entre 1 e 100. O usuário deve tentar adivinhar o número. O programa deve indicar se a tentativa é maior ou menor que o número sorteado, repetindo até que o usuário acerte.'''

def jogoAdivinhacao():
    # Gera um número aleatório entre 1 e 100
    numeroSecreto = random.randint(1, 100)

    # Solicita tentativas até o usuário acertar
    while True:
        tentativa = int(input('Adivinhe o número entre 1 e 100: '))

        if tentativa > numeroSecreto:
            print('Muito alto! Tente um número menor.')
        elif tentativa < numeroSecreto:
            print('Muito baixo! Tente um número maior.')
        else:
            print('Parabéns! Você acertou!')
            break  # Sai do laço quando o número for adivinhado

jogoAdivinhacao()

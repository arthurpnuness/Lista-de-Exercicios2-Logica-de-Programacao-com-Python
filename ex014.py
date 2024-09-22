'''Cálculo de Média:

Desenvolva um programa que solicite ao usuário uma quantidade de notas e calcule a média das notas inseridas. O programa deve continuar solicitando as notas até que o usuário digite -1.'''


## Interação com o usuario
name = input('Digite seu nome: ')
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = float(input('Digite a sua terceira nota: '))

## Calculos
cn1 = n1 * 0.5
cn2 = n2 * 0.3
cn3 = n3 * 0.2
soma = cn1 + cn2 + cn3

# Estruturas de controle e resultados
if soma >= 7.0:
    print('Parabens {} voce foi aprovado com uma media de {}'.format(name, soma))
else:
    print('Desculpe {} mas voce foi reprovado com uma media de {}'.format(name, soma))
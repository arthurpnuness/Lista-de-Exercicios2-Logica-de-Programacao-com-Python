'''Conversor de Temperatura:

Faça um programa que converta uma temperatura de graus Celsius para Fahrenheit de 10 em 10 graus, de 0 até 100. Use um laço de repetição para gerar a tabela de conversão.'''


def conversorTemperatura():
    # Laço que percorre de 0 a 100 graus Celsius em passos de 10
    for celsius in range(0, 101, 10):
        fahrenheit = (celsius * 9/5) + 32  # Fórmula de conversão para Fahrenheit
        print(f'{celsius}°C = {fahrenheit}°F')

conversorTemperatura()


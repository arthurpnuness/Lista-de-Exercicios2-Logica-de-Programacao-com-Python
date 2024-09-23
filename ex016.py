'''Função de Cálculo de Área:

Implemente uma função calcular_area_retangulo(largura, altura) que receba a largura e altura de um retângulo e retorne sua área. Teste a função solicitando os valores ao usuário.'''


def calcular_area_retangulo(largura, altura):
    # Calcula a área multiplicando a largura pela altura
    return largura * altura

# Solicita os valores ao usuário
largura = float(input('Digite a largura do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

# Chama a função e exibe o resultado
area = calcular_area_retangulo(largura, altura)
print(f'A área do retângulo é: {area}')

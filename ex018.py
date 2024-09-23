'''Função de Conversão de Temperatura:

Desenvolva uma função converter_para_fahrenheit(celsius) que receba uma temperatura em Celsius e retorne a temperatura equivalente em Fahrenheit. Teste a função com diferentes valores de temperatura fornecidos pelo usuário.'''

def converter_para_fahrenheit(celsius):
    # Fórmula de conversão de Celsius para Fahrenheit
    return (celsius * 9/5) + 32

# Solicita uma temperatura em Celsius ao usuário
celsius = float(input('Digite a temperatura em Celsius: '))

# Chama a função e exibe o resultado
fahrenheit = converter_para_fahrenheit(celsius)
print(f'A temperatura em Fahrenheit é: {fahrenheit}')

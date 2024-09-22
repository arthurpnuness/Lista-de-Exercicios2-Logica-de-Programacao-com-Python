'''Soma de Dígitos:

Crie um programa que receba um número inteiro positivo e calcule a soma de todos os seus dígitos. Exemplo: Se o usuário digitar 2514, o resultado será 12 (2 + 5 + 1 + 4).'''

# Inicializa as variáveis soma e num
soma = 0
num = 0

# Inicia um loop infinito para solicitar a entrada do usuário até que ele insira um número válido
while True: 

    # Solicita que o usuário insira um número inteiro positivo
    num = int(input('Digite um número inteiro positivo: '))

    # Verifica se o número é maior que 0
    if num > 0:
        # Inicia um loop para calcular a soma dos dígitos do número
        while num > 0:
            # Adiciona o último dígito do número à variável soma
            soma += num % 10  # O operador % obtém o último dígito do número
            # Remove o último dígito do número (dividindo-o por 10 e descartando o resto)
            num = num // 10  # O operador // faz a divisão inteira, removendo o último dígito
        
        # Após calcular a soma, imprime o resultado
        print(f'A soma dos dígitos é: {soma}')
        break  # Sai do loop externo, já que o cálculo foi concluído
    
    # Se o número for menor ou igual a 0, exibe uma mensagem de erro
    elif num <= 0:
        print('Por favor, digite um número maior que ZERO')

    # Caso algum valor inválido seja inserido, exibe uma mensagem de erro
    else:
        print('Valor Inválido')


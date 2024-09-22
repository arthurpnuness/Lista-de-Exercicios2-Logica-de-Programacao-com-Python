''''Fatorial de um Número:

Escreva um programa que solicite um número inteiro positivo n do usuário e calcule o fatorial de n utilizando um laço de repetição.'''''''''

# Definindo a função para calcular o fatorial de um número
def calculoFatorial():

    # Loop para garantir que o usuário insira um número válido
    while True:
        
        # Solicita que o usuário insira um número inteiro
        num = int(input('Digite um numero inteiro: '))

        # Verifica se o número é maior que 0
        if num > 0:
            break  # Se for maior que 0, sai do loop
        else:
            # Se o número for menor ou igual a 0, exibe uma mensagem de erro e pede novamente
            print('Por favor insira um numero maior que 0')

    # Inicializa a variável para armazenar o valor do fatorial (começa em 1)
    fatorial = 1

    # Loop para calcular o fatorial do número
    # A função range(1, num + 1) gera uma sequência de números de 1 até o valor de num
    for i in range(1, num + 1):
        # Multiplica o valor atual de fatorial pelo valor de i, acumulando o resultado
        fatorial *= i

    # Retorna o valor do fatorial calculado e o número inserido pelo usuário
    return fatorial, num

# Chama a função calculoFatorial e recebe o fatorial e o número
fatorial, num = calculoFatorial()

# Exibe o resultado final: o fatorial do número informado
print(f'O fatorial de {num} é: {fatorial}')


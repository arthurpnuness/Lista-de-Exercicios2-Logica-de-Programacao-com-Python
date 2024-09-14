'''Soma de Números Divisíveis:

Desenvolva um programa que solicite dois números inteiros positivos a e b. O programa deve somar todos os números entre a e b (inclusive) que sejam divisíveis por 3 e mostrar o resultado.'''

while True:
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero '))

    # Verifica se ambos os números são positivos
    if a > 0 and b > 0:
    # Garante que a seja o menor número e b seja o maior
        if a > b:
            a, b = b, a  # Troca os valores se a for maior que b

    soma = 0  # Variável para acumular a soma

    # Laço para percorrer os números entre a e b (inclusive)
    for i in range(a, b + 1):
        if i % 3 == 0:  # Verifica se o número é divisível por 3
            soma += i  # Adiciona o número à soma

    # Exibe o resultado
    print(f"A soma dos números entre {a} e {b} que são divisíveis por 3 é: {soma}")
else:
    print("Por favor, insira números inteiros positivos.")


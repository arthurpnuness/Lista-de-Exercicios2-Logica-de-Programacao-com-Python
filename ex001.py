'''Contagem de Números Pares e Ímpares:

Escreva um programa que receba um número inteiro positivo n do usuário e exiba todos os números pares e ímpares de 1 até n.'''

while True:
    # Solicita ao usuário que insira um número inteiro positivo
    num = int(input("Digite um número inteiro positivo: "))

    # Verifica se o número é positivo
    if num > 0:
        break # Se o número for positivo, sai do loop
    else:
        print('Por favor insira um numero maior que 0')

print('Números ímpares:')
    # Laço para verificar e exibir os números ímpares 
for num in range(1, num + 1):
    if num % 2 != 0:
       print(num)
    
print('\nNúmeros pares:')
    # Laço para verificar e exibir os números pares 
for num in range(1, num + 1):
    if num % 2 == 0:
        print(num)


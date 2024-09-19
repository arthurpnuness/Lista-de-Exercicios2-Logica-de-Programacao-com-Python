''''Fatorial de um Número:

Escreva um programa que solicite um número inteiro positivo n do usuário e calcule o fatorial de n utilizando um laço de repetição.'''''''''

def calculoFatorial():

    while True:

        num = int(input('Digite um numero inteiro: '))
        if num > 0:
            break
        else: 
            print('Por favor insira um numero maior que 0')            

    fatorial = 1

    for i in range(1, num + 1):
        fatorial *= i

    return fatorial, num

fatorial, num = calculoFatorial()
print(f'O fatorial de {num} é: {fatorial}')

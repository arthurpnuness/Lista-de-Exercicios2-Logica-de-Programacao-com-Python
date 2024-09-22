'''Série Fibonacci:

Faça um programa que peça ao usuário um número inteiro n e exiba os n primeiros números da sequência de Fibonacci.'''

# "Fn=Fn−1+Fn−2,n≥3"

num = 0 

def fibonacci(num):

    while num < 0:

        num = int(input('Digite um numero inteiro positivo: '))
        if num > 0:
            break
        else:
            print('Por favor, digite um numero maior que ZERO !!!!!')


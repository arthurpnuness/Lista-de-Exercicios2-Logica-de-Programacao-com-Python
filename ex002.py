'''Tabuada Personalizada:
Crie um programa que solicite um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.'''

while True:
        # Solicita ao usuário que insira um número inteiro positivo
    num = int(input('Digite um numero inteiro que voce queira saber a tabuada dele: '))

    # Verifica se o número é maior que zero
    if num > 0:
        break
    else:
        print('Digite um numero INTEIRO!!!!')
        
# Laço para verificar e exibir a tabuada do numero inteiro
if num > 0:
    tab1 = num * 1
    tab2 = num * 2
    tab3 = num * 3
    tab4 = num * 4
    tab5 = num * 5
    tab6 = num * 6
    tab7 = num * 7
    tab8 = num * 8
    tab9 = num * 9
    tab10 = num * 10
    print(f'A tabuada de {num} é: \n {num} x 1 = {tab1} \n {num} x 2 = {tab2} \n {num} x 3 = {tab3} \n {num} x 4 = {tab4} \n {num} x 5 = {tab5} \n {num} x 6 = {tab6} \n {num} x 7 = {tab7} \n {num} x 8 = {tab8} \n {num} x 9 = {tab9} \n {num} x 10 = {tab10}\n Obrigado por usar a aplicação. ')

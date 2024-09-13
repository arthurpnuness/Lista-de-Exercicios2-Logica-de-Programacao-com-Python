'''Aprovação de Empréstimo:
Crie um programa que simule a aprovação de um empréstimo. O usuário deve informar o valor do empréstimo, a taxa de juros mensal e o número de meses para pagar. O programa deve calcular o valor da prestação mensal e verificar se o valor é maior que 30% do salário do usuário.
'''

emprestimo = float(input('Informe o valor do empréstimo: '))
taxJuros = float(input('Digite a taxa de juros: '))
meses = int(input('Digite em quantos meses voce deseja pagar o empréstimo: '))
salario = float(input('Digite o seu salario: '))

prestMensal = (emprestimo + taxJuros) / meses
verificacao = salario * 0.30

if prestMensal > verificacao:
    print('Emprestimo não aprovado. A prestação de R$ {} , é maior que 30% do seu salario'.format(verificacao))
else:
    print('Emprestimo aprovado!')





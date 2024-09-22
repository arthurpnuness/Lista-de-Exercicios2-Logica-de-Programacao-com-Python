'''Aprovação de Empréstimo:
Crie um programa que simule a aprovação de um empréstimo. O usuário deve informar o valor do empréstimo, a taxa de juros mensal e o número de meses para pagar. O programa deve calcular o valor da prestação mensal e verificar se o valor é maior que 30% do salário do usuário.
'''

# Solicita ao usuário o valor do empréstimo e converte para float
emprestimo = float(input('Informe o valor do empréstimo: '))

# Solicita a taxa de juros e converte para float
taxJuros = float(input('Digite a taxa de juros: '))

# Solicita o número de meses para pagar o empréstimo e converte para inteiro
meses = int(input('Digite em quantos meses voce deseja pagar o empréstimo: '))

# Solicita o valor do salário do usuário e converte para float
salario = float(input('Digite o seu salario: '))

# Calcula o valor da prestação mensal do empréstimo
# A fórmula soma o valor do empréstimo com a taxa de juros e divide pelo número de meses
prestMensal = (emprestimo + taxJuros) / meses

# Calcula 30% do salário do usuário para a verificação da capacidade de pagamento
verificacao = salario * 0.30

# Verifica se a prestação mensal é maior que 30% do salário do usuário
if prestMensal > verificacao:
    # Se a prestação for maior que 30%, o empréstimo não é aprovado
    print('Empréstimo não aprovado. A prestação de R$ {} , é maior que 30% do seu salário'.format(verificacao))
else:
    # Se a prestação for menor ou igual a 30%, o empréstimo é aprovado
    print('Empréstimo aprovado!')






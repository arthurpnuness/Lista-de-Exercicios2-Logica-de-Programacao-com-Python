'''Função para Verificar Número Primo:

Crie uma função eh_primo(numero) que receba um número e retorne True se for primo e False caso contrário. Utilize esta função para verificar se um número inserido pelo usuário é primo.'''

def eh_primo(numero):
    # Verifica se o número é menor que 2, logo, não é primo
    if numero < 2:
        return False
    
    # Laço que verifica divisores do número
    for i in range(2, numero):
        if numero % i == 0:  # Se encontrar um divisor, não é primo
            return False
    
    # Se não encontrar divisores, o número é primo
    return True

# Solicita o número ao usuário
numero = int(input('Digite um número inteiro: '))

# Chama a função e exibe o resultado
if eh_primo(numero):
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')

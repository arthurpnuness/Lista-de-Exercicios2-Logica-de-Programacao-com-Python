'''Função para Contar Vogais:

Escreva uma função contar_vogais(texto) que receba uma string e retorne o número de vogais presentes no texto. Peça ao usuário para digitar uma frase e exiba o resultado.'''

def contar_vogais(texto):
    # Define as vogais (minúsculas e maiúsculas)
    vogais = 'aeiouAEIOU'
    contador = 0
    
    # Laço que percorre cada caractere do texto
    for char in texto:
        if char in vogais:  # Se o caractere for uma vogal, incrementa o contador
            contador += 1
    
    # Retorna o número de vogais
    return contador

# Solicita uma frase ao usuário
frase = input('Digite uma frase: ')

# Chama a função e exibe o resultado
numero_vogais = contar_vogais(frase)
print(f'A frase contém {numero_vogais} vogais.')

#Testar se uma palavra é um palíndromo

def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Verifica se é um palíndromo usando a função
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')
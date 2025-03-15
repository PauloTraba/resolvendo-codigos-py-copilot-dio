#Calcular a média de três notas fornecidas na entrada do usuário.


# Solicita ao usuário que insira as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado da média
print(f"A média das notas {nota1}, {nota2} e {nota3} é: {media:.2f}")
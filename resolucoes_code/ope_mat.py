# Ssolicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita ao usuário que insira o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
numero2 = float(input("Digite o segundo número: "))

# Realiza operações simples
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Verifica se o segundo número não é zero para evitar divisão por zero
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Divisão por zero não é permitida!"

# Exibe os resultados
print(f"Soma: {numero1} + {numero2} = {soma}")
print(f"Subtração: {numero1} - {numero2} = {subtracao}")
print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
print(f"Divisão: {numero1} / {numero2} = {divisao}")
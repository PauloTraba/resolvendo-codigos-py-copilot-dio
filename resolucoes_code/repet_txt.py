# Solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita ao usuário que insira o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
numero2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que escolha uma operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")
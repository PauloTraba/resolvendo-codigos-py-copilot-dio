# Receber um número inteiro e verifique se ele é par ou ímpar.

def verificar_par_impar(numero):
    return "par" if numero % 2 == 0 else "ímpar"

# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Exibe o resultado
print(f"O número {numero} é {verificar_par_impar(numero)}.")
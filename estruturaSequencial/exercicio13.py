#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("digite sua altura "))

pesoHomen = 72.7 * altura - 58
print(f"peso ideal para sexo masculino é = {pesoHomen:.1f}")

pesoMulher = 62.1 * altura - 44.7
print(f"peso ideal para sexo feminino é = {pesoMulher:.1f}")
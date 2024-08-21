# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.


num1 = int(input("informe o primeeiro valor \n"))
num2 = int(input("informe o segundo valor \n"))
numReal = float(input("informe o terceiro valor \n"))

print("o produto é: ", (num1 * 2) + (num2 / 2))
print("a soma do triplo é: ", (num1 * 3) + numReal)
print(f"o terceiro elevado ao cubo é: {numReal**3:.2f}")
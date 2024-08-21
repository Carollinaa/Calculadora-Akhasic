#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).


Fahrenheit = float(input("informe um valor em Fahrenheit: ""\n"))
Celsius = 5 *((Fahrenheit-32) / 9)

print(f"A converssão de graus Fahrenheit para graus celsius é: {Celsius:.2f}")
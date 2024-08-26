# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

print("Bem vindo úsuario, ao aplicativo da loja TINTASTIM! \nAbaixo você ira informar seus metros quadrados, "
       "sabendo que um litro de tinta do nosso departamente cobre cerca de três metros quadrados e nossa tinta é vendida em latas de 18 litros cada, "
       "que custam R$ 80,00 \nBoa compra!")
metroquadrado = float(input("Diga o tamanho em metros quadrados que você deseja pintar \n"))

quantidadeT = metroquadrado / 3
quantidedeL = math.ceil( quantidadeT / 18)
custoL = quantidedeL * 80

print("Você deve comprar",quantidedeL,"latas de tinta que ira custar",custoL,"reais")
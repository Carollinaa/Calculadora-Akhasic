# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

print("Bem-vindo, usuário, ao aplicativo da loja TINTASTIM! \n"
      "Abaixo, você irá informar seus metros quadrados. "
      "Sabendo que um litro de tinta cobre cerca de seis metros quadrados e nossa tinta é vendida em latas de 18 litros,"
      "que custam R$ 80,00, ou também em galões de 3,6 litros, que custam R$ 25,00. \n"
      "Você pode escolher entre comprar apenas latas, apenas galões, ou ambos para minimizar o desperdício.\nBoa compra!")


metroquadrado = float(input("Diga o tamanho em metros quadrados que você deseja pintar: "))

# Cálculo da quantidade de tinta necessária com 10% de folga
quantidadeT = metroquadrado / 6 * 1.1

quantidadeL = math.ceil(quantidadeT / 18)
custoL = quantidadeL * 80

print("\nOpção 1: Comprando apenas latas de 18 litros")
print(f"Você deve comprar {quantidadeL} latas de tinta que irão custar R$ {custoL:.2f}")

quantidadeG = math.ceil(quantidadeT/ 3.6)
custoG = quantidadeG * 25

print("\nOpção 2: Comprando apenas galões de 3,6 litros")
print(f"Você deve comprar {quantidadeG} galões de tinta que irão custar R$ {custoG:.2f}")

quantidadeLatasMistura = math.floor(quantidadeT / 18)
restanteTinta = quantidadeT - (quantidadeLatasMistura * 18)
quantidadeGaloesMistura = math.ceil(restanteTinta / 3.6)
custoMistura = (quantidadeLatasMistura * 80) + (quantidadeGaloesMistura * 25)

print("\nOpção 3: Mistura de latas e galões para minimizar desperdício")
print(f"Você deve comprar {quantidadeLatasMistura} latas e {quantidadeGaloesMistura} galões de tinta.")
print(f"Custo total: R$ {custoMistura:.2f}")
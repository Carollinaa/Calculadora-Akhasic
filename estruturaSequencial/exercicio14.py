# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de 
# pesca do estado de São Paulo(50 quilos)deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
# você faça um programa que leia a variável peso(peso de peixes)e calcule o excesso. Gravar na variável excesso 
# a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima 
# os dados do programa com as mensagens adequadas.

pesoMaximo = 50
pesoPeixe = float(input("João, informe o valor em quilo da pescaria de hoje \n"))

if pesoPeixe > pesoMaximo:
    excessoPeso = pesoPeixe - pesoMaximo
    multa = excessoPeso * 4 
    print("O excesso de peso que você pescou hoje João foi", excessoPeso, "e sua multa vai ser de", multa, "reais")
else:
    print("Muito bem João você não pescou peixes de mais hoje!!")
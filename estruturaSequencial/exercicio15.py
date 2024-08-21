# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


valorHora = float(input("informe quanto você ganha por hora em seu trabalho \n"))
horaMes = float(input("informe quantas horas você trabalha por mês \n"))

salarioBruto = valorHora * horaMes

ir = salarioBruto * 11 / 100 
inss = salarioBruto * 8 / 100
sindicato = salarioBruto * 5 / 100

salarioLiquido = salarioBruto - ir - inss - sindicato 

print("Seu salario bruto trabalhador, é de ", salarioBruto,"\n você pagou", inss, "reais de INSS", 
      "\n sindicato foi de", sindicato, "\n e importo de renda foi de", ir,"\n Portanto o seu valor liquido é de ", salarioLiquido)

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input("Informe o tamanho do arquivo para download em MB: "))
velocidadeInternet = float(input("Informe a velocidade da internet em Mbps: "))

tamanhoArquivomb = tamanhoArquivo * 8 
tempoSegundos = tamanhoArquivomb / velocidadeInternet 
tempoMinutos = tempoSegundos / 60 

print(f"O tempo aproximado de download é de {tempoMinutos:.2f} minutos.")

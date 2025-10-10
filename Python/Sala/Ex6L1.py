'''Calcular o valor de uma prestação em atraso, usando a fórmula: PRESTAÇÃO
<- VALOR + (VALOR * (TAXA / 100) * TEMPO).'''

taxa = float(input("Insira a taxa: "))
valor = float(input("\nInsira o valor: "))
tempo = float(input("\nInsira o tempo: "))

prestacao = valor + (valor * (taxa / 100) * tempo)

print(f"O valor da prestação é: {prestacao}")

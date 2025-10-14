'''- Faça um algoritmo que receba como entrada o mês (de 1 a 12) e retorne o nome
do respectivo mês. (Usar caso/seja – switch/case)'''

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
x = int(input("Insira o número do mês (1 a 12): "))

while x < 0 or x > 13:
    mes = int(input("Número inválido. Insira o número do mês novamente (1 a 12): "))

print(f"O mês {mes} é {meses[x-1]}")

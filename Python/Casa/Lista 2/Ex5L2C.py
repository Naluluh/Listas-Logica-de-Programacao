"""5)- Faça o programa que calcule o salário líquido dos funcionários de uma empresa. O
salário líquido é composto por descontos e adicionais, seguindo as seguintes regras:
Descontos:
Salário bruto < 800,00 – não realizar nenhum desconto;
800,00 <= Salário bruto <=1600,00 – descontar 8% de Imposto de Renda e 5
% de encargos.
>1600,00 – descontar 15% de Imposto de Renda e 7% de encargos.
Adicionais:
Caso o funcionário tenha trabalhado mais de 160 horas no mês, divida o seu salário
bruto por 160 (representa horas trabalhadas) e calcule 50% de adicional nas horas
que excederam a 160.
O usuário deverá digitar o salário bruto e o número de horas trabalhadas no mês de
cada funcionário, e deverá receber como resultado o salário líquido. O usuário poderá calcular salário para N funcionários, para finalizar o programa o usuário deverá digitar
0 no salário bruto, ao finalizar o programa exibir o total geral dos salários líquidos."""

while True:
    sBruto = float(input("Insira o valor do salário bruto: (Insira 0 para Sair.): \n"))

    if sBruto == 0:
        break
    
    hTrabalhadas = int(input("Insira o total de horas trabalhadas no mês:\n"))

    print(f"\nHoras Trabalhadas: {hTrabalhadas}\nSalário Bruto: {sBruto:.2f}")

    if sBruto < 800 :
        print("0,00\n")
        desconto = 0

    elif sBruto > 800 and sBruto < 1600:
        desconto = 8*sBruto/100 + 5*sBruto/100
        print(f"Descontos (Imposto de Renda e Encargos): {desconto:.2f}")

    else:
        desconto = 15*sBruto/100 + 7*sBruto/100
        print(f"Descontos (Imposto de Renda e Encargos): {desconto:.2f}")

    if hTrabalhadas > 160:
        adicional = sBruto/160 + (hTrabalhadas - 160)*50/100
        print(f"Adicinais (Horas Extras): {adicional:.2f}\n")
    else:
        adicional = 0
        print(f"Adicionais: {adicional:.2f}\n")

    print(f"Salário Líquido: {sBruto - desconto + adicional}\n\n")
    


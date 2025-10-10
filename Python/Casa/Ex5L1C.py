'''5) A condição física de uma pessoa pode ser medida com base no cálculo do IMC,
Índice de Massa Corporal, o qual é calculado dividindo-se a massa da pessoa ( em kg)
pela altura da mesma (h em m) elevada ao quadrado (IMC= m/h²). Escreva um
programa que leia a massa e a altura de uma pessoa, calcule e mostre o IMC.'''

print("ÍNDICE DE MASSA CORPORAL")
m = float(input("Insira a sua massa (em kg)"))
h = float(input("Insira a sua altura (em m)"))

IMC = m/h*h

print(f"IMC: {IMC}")
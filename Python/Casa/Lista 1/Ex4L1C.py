'''4) Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via
teclado, calcule a área e o perímetro de um retângulo.'''

h = float(input("Insira o valor da altura do retângulo: "))
b = float(input("\nInsira o valor da largura do retângulo: "))

A = b*h
P = 2*b + 2*h

print(f"A área deste retângulo é: {A}\nO perímetro deste retângulo é: {P}")

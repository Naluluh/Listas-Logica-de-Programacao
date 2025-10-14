'''7) Elaborar um programa para calcular e exibir o volume (V) de uma esfera e a área
(A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é
V=4/3 _ R3 e da área é A=4_ R2.'''


r = float(input("Insira o raio da circunferência: \n"))
A = 4*r*r
V = 4*3*r*r*r

print(f"Área: {A}π\nComprimento:{V}π\n")
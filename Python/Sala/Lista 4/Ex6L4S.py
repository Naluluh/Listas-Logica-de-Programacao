"""6)- Ler 8 elementos de uma matriz A do tipo vetor. Criar uma matriz B de
mesmo tipo, observando a seguinte lei de formação: “Todo elemento de B
deverá ser o quadrado do elemento de A correspondente”."""

a = []
b = []

for i in range(8):
    a.append(int(input(f"Insira o {i+1}o elemento de A: ")))
    b.append(a[i]*a[i])

print(b)
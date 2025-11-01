"""5)- Ler duas matrizes do tipo vetor A com 20 elementos e B com 30 elementos.
Criar uma matriz C, sendo essa a junção das duas outras matrizes. Assim, C
deverá ter a capacidade de armazenar 50 elementos."""

a = []
b = []
c = []

for i in range(20):
    a.append(int(input(f"Insira o {i+1}o elemento de A: ")))

for i in range(30):
    b.append(int(input(f"Insira o {i+1}o elemento de B: ")))
c.append(a+b)

print(c)
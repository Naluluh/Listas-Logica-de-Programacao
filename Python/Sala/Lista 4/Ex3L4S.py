"""3)- Ler duas matrizes A e B do tipo vetor com 5 elementos cada. Criar uma
matriz C, onde cada elemento de A é a subtração do elemento correspondente
de A com B. Exibir a matriz C."""

a = []
b = []
c = []

for i in range(5):
    a.append(int(input(f"Insira o {i+1}o elemento de A: ")))

for i in range(5):
    b.append(int(input(f"Insira o {i+1}o elemento de B: ")))
    c.append(a[i]-b[i])

print(c)
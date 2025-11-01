"""4)- Ler duas matrizes A e B do tipo vetor, com 5 elementos cada. Criar uma
matriz C, sendo essa a junção das duas outras matrizes. Assim, C deverá ter o
dobro de elementos, ou seja, 10. Exibir a matriz C."""

a = []
b = []
c = []

for i in range(5):
    a.append(int(input(f"Insira o {i+1}o elemento de A: ")))

for i in range(5):
    b.append(int(input(f"Insira o {i+1}o elemento de B: ")))
c.append(a+b)

print(c)
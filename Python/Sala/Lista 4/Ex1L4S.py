"""1)- Ler 5 elementos em uma matriz A tipo vetor. Criar uma matriz B de mesma
dimensão com os elementos da matriz A multiplicados por 3. Exibir a matriz B.
O elemento B[1] deverá ser implicado pelo elemento A [1] * 3, o elemento B[2]
pelo elemento A [2] * 3 e assim por diante, até 5."""

a = []
b = []
i = 0

for i in range (5):
    a.append(int(input(f"Insira o elemento {i+1}: ")))
    b.append(a[i]*3)

print(b)
"""2)- Ler uma matriz A do tipo vetor com 6 elementos. Criar uma matriz B de
mesmo tipo, sendo que cada elemento da matriz B seja o fatorial do elemento
correspondente da matriz A. Exibir a matriz B."""

import math

a=[]
b=[]
for i in range (6):
    a.append(int(input(f"Insira o {i+1}o elemento: ")))
    b.append(math.factorial(a[i]))

print(b)
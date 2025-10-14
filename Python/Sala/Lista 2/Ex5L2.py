'''5)- Ler 3 valores (A, B e C) e exibir os valores dispostos em ordem crescente.'''

A = float(input("Insira o primeiro número: "))
B = float(input("Insira o segundo número: "))
C = float(input("Insira o terceiro número: "))

ordem = sorted([A, B ,C])

print("\nORDEM CRESCENTE: ")
print(ordem)
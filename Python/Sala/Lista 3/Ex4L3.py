"""4)- Ler um número N qualquer menor ou igual a 50 e exibir o valor obtido da
multiplicação sucessiva de N por 3 enquanto o produto for menor que 250 (N*3,
N*3*3, N*3*3*3, etc.)"""

n = int(input("Insira o número (menor ou igual a 50): "))
mult = n
while mult < 250:
    mult = mult*3
    if mult< 250:
        print(f"Resultado: {mult:.0f}")


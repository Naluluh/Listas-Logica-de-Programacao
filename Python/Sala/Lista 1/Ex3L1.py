'''Calcular e exibir o valor do volume de uma lata de óleo, usando a fórmula:
VOLUME <- 3.14159 * R * R * ALTURA.'''


PI = 3.14159
raio = float(input("Insira o valor do raio da lata (cm): "))
altura = float(input("Insira o valor da altura (cm): "))

volume = PI * raio * raio * altura

print(f"O volume desta lata de óleo é {volume:.2f} centímetros cúbicos\n")
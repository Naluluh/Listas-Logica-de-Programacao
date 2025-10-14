'''1) Elaborar um programa em que informe se o número digitado pelo usuário é par ou 
impar.'''

x = int(input("Insira o número para consulta: "))

if x % 2 == 0:
    print(f"{x} é um número par")
else:
    print(f"{x} é um número ímpar")


'''4) Faça um programa que leia 3 números e exiba:
a) O maior número;
b) O menor número;
c) O número do meio'''

x = int(input("Insira o primeiro número: "))
y = int(input("Insira o segundo número: "))
z = int(input("Insira o terceiro número: "))

ordem = sorted(x, y, z)

print(f"Respectivamente, o maior, menor e o número do meio digitado: {ordem}")


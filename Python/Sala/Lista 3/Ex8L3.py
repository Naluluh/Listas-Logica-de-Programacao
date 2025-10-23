"""8)- Crie um programa que exiba a série de Fibonacci até o décimo quinto
termo. A série de Fibonacci é formada pela seqüência: 1, 1, 2, 3, 5, 8, 13, 21,
34....etc. Essa série se caracteriza pela soma de um termo posterior com seu
anterior subseqüente."""

print("Sequência de Fibonacci (15 termos)")
a = 1
b = 1
print(a)
print(b)
for i in range (13):
    a, b = b, a+b
    print(b)


'''6)- Ler 3 valores (A, B e C) e calcular a equação de segundo grau, exibindo as duas
raízes, se para os valores informados for possível efetuar o referido cálculo.'''

import math

a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

delta = b*b - 4*a*c

if delta>0:
 x1 = ((b*(-1)) + math.sqrt(delta))/2*a
 x2 = ((b*(-1)) - math.sqrt(delta))/2*a

 print(f"As raízes desta equação são {x1} e {x2}")

else:
 print("Essa equação não possui raízes reais")


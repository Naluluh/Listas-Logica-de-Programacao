'''8)- Ler 3 números inteiros e exibir os números que são divisíveis por 2 e 3.'''

A = int(input("Insira o primeiro número: "))
B = int(input("Insira o primeiro número: "))
C = int(input("Insira o primeiro número: "))

if A % 6 == 0:
 print(f"{A} é divisível por 2 e 3")
elif B % 6 == 0:
 print(f"{B} é divisível por 2 e 3")
elif C % 6 == 0:
 print(f"{C} é divisível por 2 e 3")
else:
 print("Nenhum dos números é divisível por 2 e 3")
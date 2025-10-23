"""3)- Exibir os resultados de uma tabuada de um número qualquer. Essa deverá
ser impressa no seguinte formato:
2 X 1 = 2
2 X 2 = 4
(...)
2 X 10 = 20"""

n = int(input("Insira o valor da tabuada: "))
print(f"TABUADA DO {n}\n")
for i in range(11):
    produto = n * i
    print(f"{n} X {i} = {produto}")
'''8) Faça um programa para calcular a média final de um aluno, supondo-se que há
quatro notas bimestrais durante o ano e que esta é calculada através de uma média
aritmética simples (todos os bimestres têm o mesmo peso).'''

print("--- CÁLCULO DA MÉDIA ---")
n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))
n4 = float(input("Insira a quarta nota: "))

m = (n1+n2+n3+n4)/4

print(f"Média: {m}")

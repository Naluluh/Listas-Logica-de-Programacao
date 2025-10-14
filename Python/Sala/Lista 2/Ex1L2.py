'''1)- Ler 3 valores referentes a 3 notas de um aluno e exibir uma mensagem dizendo que
ele foi aprovado, se o valor da média for maior ou igual a 6.0. Se o aluno não foi
aprovado, exibir mensagem informando essa condição. Exibir junto com uma das
mensagens,o valor da média para qualquer condição.'''

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))

m = (n1+n2+n3) / 3

print(f"A média deste aluno é: {m:.2f}")

if m >= 6:
 print("Aprovado!")

else:
 print("Reprovado!")
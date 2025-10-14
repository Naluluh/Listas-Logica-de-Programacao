'''2)- Ler 2 valores referentes a 2 notas de um aluno e exibir uma mensagem dizendo que
o aluno foi aprovado, se o valor da média for maior ou igual a 6.0. Se o valor da média
for menor que 6.0, solicitar a nota de exame, somar com o valor da média e obtiver
uma nova média. Se a nova média for maior ou igual a 5, exibir mensagem dizendo
que o aluno foi aprovado em exame. Se o aluno não foi aprovado, exibir uma
mensagem informando essa condição. Exibir junto com uma das mensagens, o valor
da média para qualquer condição.'''

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))

m = (n1+n2+n3) / 3

print(f"A média deste aluno é: {m:.2f}")

if m >= 6:
 print("Aprovado!")

else:
 exame = float(input("Insira a nota do exame:"))

 nm = exame+m

 print(f"A nova média do aluno é: {nm:.2f}")
 if nm >= 6:
  print("Aprovado!")

 else:
  print("Reprovado!")
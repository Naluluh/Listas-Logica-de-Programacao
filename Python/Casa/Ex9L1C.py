'''9) O critério de avaliação semestral de determinada escola segue a regra:
P1 – primeira avaliação do semestre.
P2 – segunda avaliação do semestre.
Ativ – nota atribuída pelas atividades realizadas no semestre.
Média = P1 x 4 + P2 x 4 + Ativ x 2
------------------------------------
 10
Escreva um programa que leia as notas das provas (P1 e P2) e da atividade (Ativ),
calcule e mostre a média, seguindo o cálculo acima.'''

p1 = float(input("Insira a nota da avaliação do primeiro semestre: \n"))
p2 = float(input("Insira a nota da avaliação do segundo semestre: \n"))
atv = float(input("Insira a nota da avaliação do primeiro semestre: \n"))

m = (p1*4 + p2*4 + atv*2) / 10

print(f"Média: {m}")
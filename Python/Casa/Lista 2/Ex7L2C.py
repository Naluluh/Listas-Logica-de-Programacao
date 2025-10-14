'''7)- Entrar um código de acesso a um curso. Se o código for 1, 2,3,4 e 5 exibir na tela: Engenharia, Edificações, Sistemas Elétricos, Turismo e Análise de Sistemas, respectivamente; caso contrário exibir que o código é inválido.'''

cursos = ["Engenharia","Edificações", "Sistemas Elétricos", "Turismo", "Análise de Sistemas"]

x = int(input("Escolha um curso:\n1 - Engenharia\n2 - Edificações\n3 - Sistemas Elétricos\n4 - Turismo\n5 - Análise de Sistemas\n "))

while x < 0 or x < 5:
    x = int(input("Curso inválido. Insira um número de 1 a 5: "))

print(f"O curso escolhido foi {cursos[x-1]}")
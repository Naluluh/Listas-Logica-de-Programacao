"""Extra I) Elaborar um programa que seja uma “Calculadora”, onde o usuário deverá digitar
uma das seguintes teclas: ‘+’, ‘-‘, ‘*’, ‘/’ ou ‘S’. - Caso escolha ‘S’, para sair, o programa
deverá ser encerrado; - Caso escolha ‘+’, ‘-‘, ‘*’ ou ‘/’, como operações aritméticas, o
programa
deverá solicitar a digitação de dois números quaisquer (número a e número b), um por
vez, realizar a respectiva operação aritmética (soma, subtração, multiplicação ou
divisão) entre os respectivos números (a e b, nessa ordem) e então apresentar o seu
resultado. Após isto, deverá voltar à etapa inicial de digitação das teclas ‘+’, ‘-‘, ‘*’, ‘/’
ou ‘S’ e repetir este item até a digitação da tecla ‘S’."""

print("CALCULADORA PADRÃO")

while True:
    operacao = str(input("Insira a operação desejada:\n + (adição)\n - (subtração)\n / (divisão)\n * (multiplicação)\n S (sair)\n"))

    if operacao == 'S' or operacao == 's':
        break

    a = float(input("Insira o primeiro número para a operação:"))
    b = float(input("Insira o segundo número para a operação: "))

    print("Operação selecionada:")
    if operacao == '+':
        print("Adição")
        resultado = a + b

    if operacao == '-':
        print("Subtração")
        resultado = a - b

    if operacao == '/':
        print("Divisão")
        resultado = a / b

    if operacao == '*':
        print("Multiplicação")
        resultado = a * b

    print(f"Resultado: {resultado}")
    
    

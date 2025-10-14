'''2) Digitado um número inteiro entre 0 e 100, informar o quanto ele está distante de um 
determinado número chave, carregado no próprio programa. Ex.: Número chave=20, 
número digitado=15, resposta=5. Número chave=17, número digitado=20, resposta=3 
(Obs.: a resposta deverá ser sempre um número positivo).'''

import random

y = random.randint(0, 100)

x = int(input("Digite o número misterioso: "))

while x !=y : 
    if x > y:
        print(f"{x} está {x - y} unidades distante do número misterioso")
        x = int(input("Insira um novo valor: "))

    else: 
        print(f"{x} está {y - x} unidades distante do número misterioso")
        x = int(input("Insira um novo valor: "))

if x == y:
    print(f"Parabéns! {x} é o número misterioso")

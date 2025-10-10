'''Uma loja petshop precisa de um programa para calcular os custos de criação
de coelhos. O custo é calculado com a fórmula: CUSTO <- (NR_COELHOS * 0.70)
/18 + 10. O programa deve ler o valor para a variável NR_COELHOS e exibir o
valor da variável CUSTO.'''

nrCoelhos = int(input("Insira a quantidade de coelhos: "))

custo = (nrCoelhos * 0.7) /18 + 10

print(f"O custo da criação de {nrCoelhos} coelhos é {custo} reais")
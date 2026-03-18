IDv = int(input("Digite seu ID de vendedor: "))
IDp = int(input("Digite o ID da peça: "))
Vuni = float(input("Digite o valor unitário da peça: "))
Qtd = int(input("Digite a quantidade de peças: "))

Vtotal = Vuni * Qtd
Comissao = Vtotal * (5/100)

print("O vendedor {} realizou uma venda de {} com o valor total de R$ {}. Tendo uma comissâo total de R$ {}".format(IDv, IDp, Vtotal, Comissao))
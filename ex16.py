def valor_total(a,b):
    vtotal = a * b
    return vtotal
vproduto = float(input("Digite o valor unitário do produto: "))
qtd = int(input("Digite a quantidade de produtos comprados: "))
print("O valor total da compra foi de: R$", valor_total(vproduto, qtd))
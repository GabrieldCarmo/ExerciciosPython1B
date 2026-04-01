qtd = 0
maior = 0

while True:
    nome = input("Digite um nome: ")

    if nome == "encerrar":
        break

    idade = int(input("Digite a idade: "))

    qtd += 1

    if idade > 18:
        maior += 1

print("Usuários cadastrados: {}"
      "Maiores de idade: {}".format(qtd, maior))
Vcarro = float(input("Digite o valor do carro: "))

Vimposto = Vcarro * (45/100)
Vdist = (Vcarro + Vimposto) * (12/100)
Vtotal = Vcarro + Vdist + Vimposto

print("\nValor do carro: R${} \n"
      "Valor do imposto R${} \n"
      "Valor distribuidor: R${} \n"
      "Valor total do carro: R${}".format(Vcarro, Vimposto, Vdist, Vtotal))
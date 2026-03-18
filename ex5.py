Vsalario = float(input("Digite o valor do salário: "))

if Vsalario > 0 and Vsalario <= 1000:
    aumento = 20/100
elif Vsalario > 1000.01 and Vsalario <= 5000:
    aumento = 10/100
else:
    aumento = 5/100

Nsalario = Vsalario + (Vsalario * aumento)

print("O novo salário do jogador será de R$ {}".format(Nsalario))
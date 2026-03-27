peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)

if imc < 18.5:
    classificacao = "Abaixo do peso normal"
elif imc > 18.5 and imc < 24.5:
    classificacao = "Normal" 
elif imc > 18.5 and imc < 24.5:
    classificacao = "Excesso de peso" 
elif imc > 18.5 and imc < 24.5:
    classificacao = "Obesidade grau I" 
elif imc > 18.5 and imc < 24.5:
    classificacao = "Obesidade grau II" 
else:
    classificacao = "Obesidade grau III"
    
print("\nSeu peso: {}\n"
      "Sua Altura: {}\n"
      "Seu IMC: {:.2f}\n"
      "Sua Classificação: {}".format(peso, altura, imc, classificacao))
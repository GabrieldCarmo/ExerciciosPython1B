media = 0
soma = 0
i = 0

while i < 3:
    nota = float(input("Digite sua nota: "))
    soma += nota
    i += 1
    
media = soma/3

if media >= 8:
    conceito = "A"
elif media >=5 and media < 8:
    conceito = "B"
else:
    conceito = "C"
    
print("Conceito: {}\n"
      "Média: {:.2f}".format(conceito, media))
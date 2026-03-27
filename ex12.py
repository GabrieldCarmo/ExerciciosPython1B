i = 0
c = 0
nota = 0
soma = 0
maior = 0
menor = 0

while i != -1:
    i = float(input("Digite a nota do aluno: "))
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
    soma += i
        
    c+=1
        
    media = soma/c            
print ("MAIOR: {}\n"
       "MENOR: {}\n"
       "MÉDIA: {:.2f}".format(maior,menor,media))
        

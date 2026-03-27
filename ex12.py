i = 0
c = 0
nota = 0
soma = 0
maior = 1
menor = 1


if nota != -1:
    while i != -1:
        i = float(input("Digite a nota do aluno: "))
    
        if i > maior:
            maior = nota
        elif i < menor:
            menor = nota

        
        soma += nota
        
        c+=1
        
        media = soma/c
            
    print ("MAIOR: {}\n"
           "MENOR: {}\n"
           "MÉDIA: {}".format(maior,menor,media))
        

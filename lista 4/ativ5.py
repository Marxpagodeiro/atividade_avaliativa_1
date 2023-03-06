cont_id=0
cont__id_al=0
alt_med=0
TAM=20
for i in range(TAM):
    idade=int(input(f"Digite a idade da pessoa {i+1} em anos : "))
    altura=float(input(f"Digite a altura da passoa {i+1} em metros: "))
    if(idade>20 and idade<35):
        cont_id+=1
    if(idade>=18 and altura > 1.60 and altura < 1.80):
        cont__id_al+=1
    alt_med+=altura
media=alt_med/TAM
print(f"Existem {cont_id} pessoas com a idade entre 20 e 35.")
print(f"Existem {cont__id_al} pessoas com mais de 18 anos e com a altura entre 1.60 e 1.80")
print(f"A media da aultura das pessoas é de {media}") 

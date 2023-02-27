#contador de 10 numeros
cont1=0
cont2=0
cont3=0
for i in range(10):
    num=float(input(f"Digite o {i+1}º número: "))
    if(num>=30 and num<=100):
        cont1+=1
    elif(num>=1 and num <=29):
        cont2+=1
    else:
        cont3+=1
print(f"{cont1} numeros estão no intervalo entre 30 e 100")
print(f"{cont2} numeros estão no intervalo entre 1 e 29")
print(f"{cont3} numeros são menores ou iguais a zero ou maior que 100")


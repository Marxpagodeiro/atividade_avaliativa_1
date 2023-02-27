#Aposentadoria
cont1=0#contador idade
cont2=0#conador tempo de serviço
cont3=0#contador idade e tempo
cont4=0#contador não pode se aposentar 
for i in range(5):
    sexo = int(input(f"Digite o sexo do trabalhador{i+1} (Digite 1 para feminino e 2 para masculino): "))
    idade = int(input(f"Digite a idade da trabalhador{i+1} em anos : "))
    tempo_serviço=int(input(f"Digite o tempo de serviço da trabalhador{i+1} em anos: "))
    if (sexo==1): 
        if(idade>=60 and tempo_serviço<25):
            print("Esta pessoa pode se aposentar pela idade")
            cont1+=1
        elif(tempo_serviço>=30 and idade<55):
            print("Esta pessoa pode se aposentar pelo tempo de serviço")
            cont2+=1
        elif(idade>=60 and tempo_serviço>=35):
            print("Esta pessoa pode se aposentar pela idade e pelo tempo de serviço")
            cont3+=1
        else:
            print("Esta pessoa não pode se aposentar")
            cont4+=1
    elif(sexo==2):
        if(idade>=65 and tempo_serviço<35):
            print("Esta pessoa pode se aposentar pela idade")
            cont1+=1
        elif(tempo_serviço>=35 and idade<60):
            print("Esta pessoa pode se aposentar pelo tempo de serviço")
            cont2+=1
        elif(idade>=60 and tempo_serviço>=35):
            print("Esta pessoa pode se aposentar pela idade e pelo tempo de serviço")
            cont3+=1
        else:
            print("Esta pessoa não pode se aposentar")
            cont4+=1
print(f"{cont1}trabalhadores poderão se aposentar por idade")
print(f"{cont2}trabalhadores poderão se aposentar por tempo de serviço")
print(f"{cont3}trabalhadores poderão se aposentar por idade e tempo de serviço")
print(f"{cont4}trabalhadore não poderão vão se aposentar")



        

    

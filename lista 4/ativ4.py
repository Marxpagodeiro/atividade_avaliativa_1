K=float(input("Qual é o valor de K ? "))
M=int(input("Qual é o valor de M ? "))
N=int(input("Qual é o valor de N ? "))
cont=0
if (K < M and M < N):
    for i in range(M,N):
        if (i % K==0):
            cont+=1
    print(f"Existem {cont} números múltiplos de {K} entre {M} e {N}.")
else:
    print("Valores informados não são válidos!")


#aprovação do aluno
aluno=str(input("Qual o nome do aluno? "))
nota1=float(input("Qual é a nota do aluno no primeiro bimestre(de 0 a 100)? "))
nota2=float(input("Qual é a nota do aluno no segundo bimestre(de 0 a 100)? "))
nota3=float(input("Qual é a nota do aluno no terceito bimestre(de 0 a 100)? "))

media3= (nota1+nota2+nota3)/3 #media ate o terceiro bimestre 

if (media3<70):
    print(f"O(a) aluno(a) {aluno} deverá fazer a avaliação do quarto bimestre, pois ficou com {media3}")
    nota4=float(input("Qual é a nota do aluno no quarto bimestre(de 0 a 100)? "))
    media_final=(nota1+nota2+nota3+nota4)/4
    if (media_final<50):
        print(f"O(a) aluno(a) {aluno} está reprovado(a) com media: {media_final:.2f}")
    elif(media_final>=50 and media_final<70):
       print(f"O(a) aluno(a) {aluno} está de recuperação com media: {media_final:.2f}") 
    else:
        print(f"O(a) aluno(a) {aluno} está aprovado(a) com media: {media_final:.2f}")
else:
    print(f"O(a) aluno(a) {aluno} está aprovada(a) no terceiro bimestre com media: {media3}")



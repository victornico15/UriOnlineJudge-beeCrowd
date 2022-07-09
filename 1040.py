linha1 = input().split(" ")

n1,n2,n3,n4=linha1
n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)

mediaP=(n1*2)+(n2*3)+(n3*4)+(n4*1)/10
mediaP=float(mediaP)
bol1=mediaP=>5.0
bol2=mediaP=<6.9
if bol1 and bol2:
    
    mediaP2=float(input("Aluno em exame."))
    mediaP=mediaP2+mediaP/2
    Notafinal(mediaP)
    print("Media final: %.2f"%mediaP)
    

else:
    print("Media: %.2f"%mediaP)
    Notafinal(mediaP)



def Notafinal(variavel):
    
    if variavel=>7.0:
        print("Aluno aprovado.")
    elif(variavel<5.0):
        print("Aluno reprovado.")

    ///
    
    
    x = input().split()
n1, n2, n3, n4 = x
m = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
if m < 5.0:
    print('Aluno reprovado.')
if 5.0 <= m <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {}'.format(y))
    m2 = (y + m) / 2
    if m2 >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(m2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(m2))
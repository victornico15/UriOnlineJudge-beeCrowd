x=int(input())
y=int(input())
aux=0
soma=0
if(x>y):
    aux=y
    y=x
    x=aux
for i in range(x,y,1):
    if(i%13!=0):
        soma=soma+i
print(soma)
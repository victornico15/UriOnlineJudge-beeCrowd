x=int(input())
y=int(input())
aux=0
soma=0
if(x>y):
    aux=y
    y=x
    x=aux
for i in range(x+1,y):
    if(i%5==2 or i%5==3 ):        
        print(i)
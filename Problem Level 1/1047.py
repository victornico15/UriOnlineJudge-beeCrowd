
"""a,b,c,d=list(map(int,input().split()))

if(a<c):
    time=c-a
    if(b<d):
       minutos=d-b
    else:
       minutos=b-d
        
     
else:
    time=c+24-a
    if(b<d):
       minutos=d-b
    else:
       minutos=b-d
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(time,minutos))//
"""



a,c,b,d=list(map(int,input().split()))

dif=((b*60)+d)-((a*60)+c)
if(dif<=0):
    dif+=24*60
    
time=dif//60
minute=dif%60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(time,minute))

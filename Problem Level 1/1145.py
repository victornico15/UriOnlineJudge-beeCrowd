from multiprocessing.resource_sharer import stop


X,Y = list(map(int,input().split()))

Aux1=1
Aux2=X
#indice referente aos numeros 
indice=1
#linha 
while(Aux1<Y):   
    
    
    if(indice==Y+1):
        break
    Aux2=0
    #coluna
    while(Aux2<X):
        if(Aux2==X-1):
            print(indice)
        else:
            print(indice,"",end="")
        
        Aux2+=1
        indice+=1

    
    Aux1+=1
    


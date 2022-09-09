aux=0
count=0
while(True):    
    count+=1
    Var=int(input())
    if(Var>=0):
       aux=aux+Var
    
    
    else:
        print("{:.2f}".format(aux/(count-1)))
        break
    
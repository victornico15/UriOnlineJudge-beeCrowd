S=1
Aux=2
while(True):
    
    for i in range (3,40,2):        
        S=S+(i/Aux)
        Aux=Aux*2
    if(i==39):        
        print("{:.2f}".format(S))
        break
        
    
    
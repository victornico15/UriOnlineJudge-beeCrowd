while(True):
    VarInput,VarFinal=input().split()
    
    if(VarInput=="0" and VarFinal=="0"):
        break
    VarFinal="0"+VarFinal
    Aux=int(VarFinal.replace(VarInput,""))
    print(Aux)

            

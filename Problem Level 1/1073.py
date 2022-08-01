VarInput=int(input())

for i in range(VarInput+1):
    
    if(i%2==0 and i!=0):
        print("{}^{} = {}".format(i,2,(i**2)))
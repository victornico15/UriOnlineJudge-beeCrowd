repeticao=int(input())


for i in range(repeticao):
    x,y=map(int,input().split())
    
    if(y==0):
        print("divisao impossivel")
    else:
        print((x/y))
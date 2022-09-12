"""lacoinput=int(input())
while(lacoinput):
    x,y=list(map(int,input().split()))
    count=y
    soma=0
    for i in range(x,10000):        
        if(i%2==1):
            count-=1        
            soma=soma+i
        if(count==0):
            print(soma)
            break
    lacoinput-=1"""
    
    j = 0
N = int(input())
while j < N:
    i = 0
    aux = 0
    X,Y = input().split(' ')
    X = int(X)
    Y = int(Y)
    vector = []
    if X % 2 == 0:
        X += 1
    while i < Y:
        vector.append(X)
        i+=1
        X+=2
    print(sum(vector))
    j+=1
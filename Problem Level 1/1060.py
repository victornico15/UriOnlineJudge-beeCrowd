lista1=list(map(float,input().split()))
count=0
for i in range(len(lista1)):
    if(lista1[i]>=0):
        count+=1

print(count,"valores positivos")



    
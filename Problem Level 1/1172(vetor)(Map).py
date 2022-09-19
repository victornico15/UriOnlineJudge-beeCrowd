A=[]
for l in range(10):
    valor=int(input())
    A.append(valor)
for i in range(0,len(A)):
    if(A[i]<=0):
        A[i]=1


for i in range (len(A)):
    print("X[{}] = {}".format(i,A[i]))





N=[]

for i in range(20):
    N.append(int(input()))

l=19
for i in range(10):
    aux1=N[i]    
    N[i]=N[l]
    N[l]=aux1
    l=l-1

for y in range(20):
    print("N[{}] = {}".format(y,N[y]))

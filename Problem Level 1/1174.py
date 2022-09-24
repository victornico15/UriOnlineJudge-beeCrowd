Vetor=[]
for i in range (100):
    Vetor.append(float(input()))

for i in range(len(Vetor)):
    if(Vetor[i]<=10):
        print("A[{}] = {:.1f}".format(i,Vetor[i]))

        
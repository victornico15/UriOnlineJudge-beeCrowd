VarInput=int(input())

countIn=0
countOut=0
for i in range(VarInput):
    C=int(input())
    if(C>=10 and C<=20):
        countIn=countIn+1
    else:
        countOut=countOut+1
print("{} in \n{} out".format(countIn,countOut))


#################################################################


n = int(input())
dentro = 0
fora = 0
for i in range(1,n + 1):
    x = int(input())
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print('{} in'.format(dentro))
print('{} out'.format(fora))
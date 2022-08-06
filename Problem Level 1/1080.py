Maior=0
pos=0
for i in range(1,101):
    VarInput=int(input())
    if(VarInput>=Maior):
        Maior=VarInput
        pos=i
print(Maior)
print(pos)

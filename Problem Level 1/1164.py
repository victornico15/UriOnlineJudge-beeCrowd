"""
VarIndex=int(input())

while(VarIndex):
    VarA=int(input())
    somatorio=0
    for i in range (1,VarA):
        if(VarA%i==0):
         somatorio=somatorio+i
    if(somatorio==VarA):
        print(VarA,"eh perfeito")
    else:
        print(VarA,"nao eh perfeito")


    Varindex=VarIndex-1"""


    n= int(input())

for i in range(0,n):
    num = int(input())
    j = 1
    s = 0
    while j < num:
        if num % j == 0:
            s = s + j
           
        j = j + 1
       
    if s == num:
        print('{} eh perfeito'.format(num))
    else:
        print('{} nao eh perfeito'.format(num))
"""
# Função de Conversao em Int
def conversorInt(A,B,C):
    A=int(A)
    B=int(B)
    C=int(C)
    return(A,B,C)

def verificadorCrescent(Var1,Var2,Var3):
    
    if(Var1>=Var2 and Var1>=Var3 and Var2>=Var3 or Var3>=Var2):
        if(Var2>=Var3):
         print(Var3,"\n",Var2,"\n",Var1)
        else:
         print(Var2,"\n",Var3,"\n",Var1)
    if(Var2>=Var1 and Var2>=Var3 and Var1>=Var3 or Var3>=Var1):
        if(Var1>=Var3):
         print(Var3,"\n",Var1,"\n",Var2)
        else:
         print(Var1,"\n",Var3,"\n",Var2)
    if(Var3>=Var2 and Var3>=Var1 and Var2>=Var1 or Var1>=Var2):
        if(Var2>=Var1):
         print(Var1,"\n",Var2,"\n",Var3)
        else:
         print(Var2,"\n",Var1,"\n",Var3)
       
      
        
        

#1042 receber valores e colocar em ordem 
Receber=input().split()
A,B,C=Receber
A, B, C=conversorInt(A,B,C)
verificadorCrescent(A,B,C)
print("\n",A,"\n",B,"\n",C)



"""
x = input().split()
a, b, c = x
a = int(a)
b = int(b)
c = int(c)


if a > b and a > c:
    d = a
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b
if b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
if c > a and c > b:
    d = c
    if a > b:
        e = a
        f = b
    else:
        f = a
        e = b
print(f)
print(e)
print(d)
print()
print(a)
print(b)
print(c)










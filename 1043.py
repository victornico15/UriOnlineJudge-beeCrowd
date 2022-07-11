VarInput=input().split(" ")

Var1,Var2,Var3=VarInput

Var1=float(Var1)
Var2=float(Var2)
Var3=float(Var3)


if((Var1+Var2)>Var3 and (Var2+Var3)>Var1 and (Var3+Var1)>Var2) :
    Perimeter=Var1+Var2+Var3
    print("Perimetro = %.1f"%Perimeter)
else:
    Area=0.5*(Var1+Var2)*Var3
    print("Area = %.1f"%Area)
    


Var = int(input())


contadorA = 0
ContadorM = 0
ContadorD = 0
while(Var):
    if(Var >= 365):
        Var = Var-365
        contadorA = contadorA+1
    elif (Var >= 30):
        Var = Var-30
        ContadorM = ContadorM+1
    else:
        ContadorD = Var
        Var = 0
print(contadorA,"ano (s)\n",ContadorM,"mes(es)\n",ContadorD,"dias(s)")

"""ValValido=0
B=0
Novo=0
while(ValValido!=2):
    A=float(input())
    if(A>=0.0 and A<=10):
        if(ValValido==1):
            print("media = %.2f"%((A+B)/2))
        B=A
        ValValido+=1

    else:
        print("nota invalida")
        
if(ValValido==2):
    while(Novo!=2):        
        Novo=float(input("novo calculo (1-sim 2-nao) \n"))
        if(Novo==1):
            ValValido2=0
            while(ValValido2!=2):
                 A=float(input())
                 if(A>=0.0 and A<=10):
                        if(ValValido2==1):
                            print("media = %.2f"%((A+B)/2))
                        B=A
                        ValValido2+=1

                 else:
                     print("nota invalida")
  
    """
    
    
    nota_soma = 0 
cont = 0
continuar = True

while continuar==True:
  nota = float(input())
  
  if nota>=0.0 and nota <=10:
    nota_soma += nota
    cont += 1 

    if cont == 2:
      
      print("media = %.2f"%(nota_soma/2))
      cont = 0 
      nota_soma = 0

      while True:
        print("novo calculo (1-sim 2-nao)")
        novo = int(input())
        if novo == 2:
          continuar = False
          break
        elif novo == 1:
          continuar = True
          break
      
  else:
    print("nota invalida")
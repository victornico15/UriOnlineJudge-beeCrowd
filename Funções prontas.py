
frutas = ["maçã", "banana", "laranja", "melancia"]

lista = [fruta for fruta in frutas]
print(lista)

#  METODO DE RECEBER LISTA  QND CRIADA DENTRO DE UM LACO EM UMA UNICA LINHA

# Função de Conversao em Int
###CONVERSOR MELHOR   a,c,b,d=list(map(int,input().split()))
def conversorInt(A,B,C):
    a,c,b = list(map(int,input().split()))
    A=int(A)
    B=int(B)
    C=int(C)
    return(A,B,C)





# manipulacao de lista 

#multiplicando a lista
inteiros = [1,3,4,5,7,8]
quadrados = [n*n for n in inteiros]
frutas = ["maçã", "banana", "laranja", "melancia"]

lista = [fruta for fruta in frutas]
print(lista)

#  METODO DE RECEBER LISTA  QND CRIADA DENTRO DE UM LACO EM UMA UNICA LINHA



a, b, c = list(map(float, input().split()))
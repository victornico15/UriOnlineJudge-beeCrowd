def LargestFour(arr):
  aux=[]
  lista2=[]
  [aux.append(int(p)) for p in arr.split()]
  
  
  
  
  for i in range(4):
    lista2.append(max(aux))
    aux.remove(max(aux))
    
  return sum(lista2)


print(LargestFour(input()))
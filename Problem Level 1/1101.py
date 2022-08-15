
while(True):
   soma=0
   x, y = map(int, input().split())
   if(x<=0 or y<=0):
       break
   if(x>=y):
       for i in range(y,x+1,1):
           print('%d '%(i),end="")
           soma=soma+i
           if(i==x):
               print("Sum={}".format(soma))
   if(y>=x):
       for i in range(x,y+1,1):
           print('%d '%(i),end="")
           soma=soma+i
           if(i==y):
               print("Sum={}".format(soma))
           
           
           
           
       
    
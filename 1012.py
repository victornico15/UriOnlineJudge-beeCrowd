#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = input().split(' ')
A, B, C = x
A = float(A)
B = float(B)
C = float(C)
print('TRIANGULO: {:.3f}'.format(A*C/2))
print('CIRCULO: {:.3f}'.format(3.14159*C**2))
print('TRAPEZIO: {:.3f}'.format(((A+B)*C)/2))
print('QUADRADO: {:.3f}'.format(B*B))
print('RETANGULO: {:.3f}'.format(A*B))


# In[ ]:





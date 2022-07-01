#!/usr/bin/env python
# coding: utf-8

# In[8]:


entrada = input().split(" ")
A, B, C = entrada
A = int(A)
B = int(B)
C = int(C)
maiorAB = (A+B + abs(A-B))/2
maiorABC = (maiorAB+C + abs(maiorAB-C))/2
print('{:.0f} eh o maior'.format(maiorABC))


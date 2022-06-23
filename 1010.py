#!/usr/bin/env python
# coding: utf-8

# In[7]:


l1 = input().split(' ')
l2 = input().split(' ')

cod_1, num_peca_1, valor_p_1 = l1
cod_2, num_peca_2, valor_p_2= l2

print('VALOR A PAGAR: R$ {:.2f}'.format(int(num_peca_1) * float(valor_p_1) + int(num_peca_2) * float(valor_p_2)))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
3. Напиш!ть сервер, який би отримував у користувача фразу, а пом
надсилав би пдраховану юльксть слв у вдповдь.
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
mystr = "How are you? "
sock.send(bytes(f"{mystr} ", encoding='UTF-8'))
print(mystr)
data = sock.recv(1024)
print(data)
sock.close()


# In[ ]:





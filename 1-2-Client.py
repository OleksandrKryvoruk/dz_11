#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
1. Реалзувати чат без граф/чного 1нтерфейсу, який дозволить
обмнюватися повдомленнями мж клентом та сервером. Клент повинен
отримувати повдомлення сервера.
2. Додайте до серверу з першого завдання функцю чат-боту, який би
вдсилав кленту задан! вдповд! на певн! повдомлення.
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
sock.send(bytes("Client: " + input("Client "), encoding='UTF-8'))
data = sock.recv(1024)
print(data)
sock.close()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
3. Напиш!ть сервер, який би отримував у користувача фразу, а пом
надсилав би пдраховану юльксть слв у вдповдь.
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    answer = len(data.split())
    conn.send(bytes(f"Server: You sent {answer} words", encoding='UTF-8'))  
    print(str(data))
        


# In[ ]:





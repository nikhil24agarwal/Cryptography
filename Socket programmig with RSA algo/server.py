
# coding: utf-8

# In[ ]:

import socket
import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def decrypt(ctext,p,q,e):
    try:
        n=p*q
        phi=(p-1)*(q-1)
        '''d[1] = modular inverse of e and phi'''
        d = egcd(e, phi)[1]
    
        '''make sure d is positive'''
        d = d % phi
        if(d < 0):
            d += phi
        private_key=(d,n)        
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print('hello')


server=socket.socket()  
#by default two parameters type of network working (ipv4-default or ipv6) and tcp-default udp network
print('socket bangya')


#we have to bind our socket with port number
server.bind(('localhost',9999))
key='abcd'


server.listen(10)
print('bhejo kuch bhejo')


client,addr=server.accept()
if(True):

    
    print('client agya',addr)
    rec_text=client.recv(1024).decode()
    rec_text=rec_text.split()
    rec_text=list(map(int,rec_text))
    print(rec_text)
    p=int(client.recv(1024).decode())
    q=int(client.recv(1024).decode())
    e=int(client.recv(1024).decode())

    decy=decrypt(rec_text,p,q,e)
    print(decy)


    
client.close()
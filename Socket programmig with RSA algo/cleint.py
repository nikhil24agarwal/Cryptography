
# coding: utf-8

# In[ ]:
import socket
import random
import math
import sympy

p=random.choice(list(sympy.primerange(100,1000)))    
q=random.choice(list(sympy.primerange(50,1000)))
n=p*q
phi=(p-1)*(q-1)
#condition to find e: coprime with phi and greater then 1 and less then phi
e=0
for i in range(2,phi+1):
    if(math.gcd(i,phi)==1):
        e=i
        break
    else:
        continue
public_key=(e,n)

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext



client=socket.socket()
key='abcd'


client.connect(('localhost',9999))
print("Press q for exit")


if(True):
    txt=input('enter the plaintest : ')
    ency=encrypt(txt,public_key)
    ency=list(map(str,ency))
    client.send(bytes(" ".join(ency),'utf-8'))
    print(p,q,e)
    client.send(bytes(str(p),'utf-8'))
    client.send(bytes(str(q),'utf-8'))
    client.send(bytes(str(e),'utf-8'))

    


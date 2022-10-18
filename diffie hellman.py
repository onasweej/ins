import random
'''S   R
n,g
x   y
A=g^x mod n   B=g^ymod n
B    A
k1=B^x mod n   k2=A^y mod n

k1=k2'''

n=13
g=17
def diffieHellman(r):
    return (g**r)%n
    

def key(A,B,x,y):
    print(A,B,x,y)
    k1=(B**x)%n
    k2=(A**y)%n
    print(k1,k2)
    if(k1==k2):
        print("key exchange successfully")
    else:
        print("key values are different")
    
    
x=random.randint(5,50)
y=random.randint(6,60)

A=diffieHellman(x)
B=diffieHellman(y)

key(A,B,x,y)

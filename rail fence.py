fv=[]
sv=[]

def encrypt(msg):
    strg=" "
    for v in range(0,len(msg)):
        if(v%2==0):
            fv.append(msg[v])
        else:
            sv.append(msg[v])
    print(strg)
    for v in fv:
        strg=strg+v
    for v in sv:
        strg=strg+v
    print("Encrypted message: ",strg)

def decrypt(msg):
    strg=""
    l=len(msg)//2
    print("1",1)
    if(len(msg)%2!=0):
        l=l+1
        print("len//",1)
    print("len/2=",l)
    m=l
    for i in range(0,l):
        if(m<len(msg)):
            strg=strg+msg[i]+msg[m]      
        m=m+1
        print(i,m,strg,msg)
    if len(msg)%2!=0:
        strg=strg+msg[i]
    print("Decrypted message: ",strg)



encrypt("onaswee")
decrypt("oawense")

''' piakryn
 piak
 ryn
 priyank
 
'''

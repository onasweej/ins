def encryption (PT,key):
    CT=""
    alp='abcdefghijklmnopqrstuvwxyz'
    i=0
    for a in PT:
        indPT=alp.index(a)
        indkey=alp.index(key[i])
        i=i+1
        indCT=indPT+indkey
        print(indCT)
        if indCT>=26:
            indCT=indCT%26
        CT=CT+alp[indCT]
        print("PT: "+PT+" key: "+key+" CT "+CT)
encryption("onaswee","happier")
    
def decryption (CT,key):
    PT=""
    alp='abcdefghijklmnopqrstuvwxyz'
    i=0
    for a in CT:
        indCT=alp.index(a)
        indkey=alp.index(key[i])
        i=i+1
        indPT=indCT-indkey
        print(indPT)
        if indPT>=26:
            indPT=indPT%26
        PT=PT+alp[indPT]
        print("CT: "+CT+" key: "+key+" PT "+PT)
decryption("vnpheiv","happier")

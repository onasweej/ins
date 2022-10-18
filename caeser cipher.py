def encryption(PT,key):
    CT=""
    alp='abcdefghijklmnopqrstuvwxyz'
    for a in PT:
        ind=alp.index(a)
        print(ind)

        if (ind+key)>25:
            mind=(ind+key)%26
        else:
            mind=ind+key
        CT=CT+alp[mind]
    print("Encryption:\n Plain Text:"+PT+"_Cipher Text:"+CT)
encryption("onaswee",3)

def decryption(CT,key):
    PT=""
    alp='abcdefghijklmnopqrstuvwxyz'
    for a in CT:
        ind=alp.index(a)
        print(ind)

        if (ind+key)>25:
            mind=(ind+key)%26
        else:
            mind=ind-key
        PT=PT+alp[mind]
    print("Decryption:\n Cipher Text:"+CT+"_Plain Text:"+PT)
decryption("rqdvzhh",3)

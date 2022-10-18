def encryption (PT):
    CT=""
    alp1='abcdefghijklmnopqrstuvwxyz'
    alp2='zyxwvutsrqponmlkjihgfedcba'
    for a in PT:
        ind=alp1.index(a)
        CT=CT+alp2[ind]
    print("Encryption:\Plain Text:"+PT+"Cipher Text:"+CT)
encryption("onaswee")

def decryption (CT):
    PT=""
    alp1='abcdefghijklmnopqrstuvwxyz'
    alp2='zyxwvutsrqponmlkjihgfedcba'
    for a in CT:
        ind=alp1.index(a)
        PT=PT+alp2[ind]
    print("Decryption:\Cipher Text:"+CT+"Plaon Text:"+PT)
decryption("lmzhdvv")

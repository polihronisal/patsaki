keimeno = raw_input('dwse keimeno ')

mik=["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","g","k","l","m"]

kef=["A","B","C","D","E","F","G","H","I","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","G","K","L","M"]
krypto=("")
for i in keimeno :
    if i in kef :
        krypto = krypto + kef[kef.index(i) + 13]
    elif i in mik :
        krypto = krypto + mik[mik.index(i) + 13]
    else :
        krypto = krypto + i
print {krypto}

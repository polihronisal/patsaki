arithmos = int(raw_input ('dwse aritho apo 1-1000000'))




latinikos=("")

xiliades=arithmos//1000

arithmos =arithmos - xiliades*1000

ekatodades=arithmos//100

arithmos=arithmos-ekatodades*100

dekades=arithmos//10

arithmos=arithmos-dekades*10

monades=arithmos//1

if xiliades >0 :
        latinikos=latinikos + xiliades*"M"
        
if ekatodades>0:
        
        if ekatodades <4:
                latinikos=latinikos + ekatodades*"C"
        elif ekatodades==9:
                 latinikos=latinikos +"CM"
        elif ekatodades==5:
                 latinikos=latinikos +"D"
        elif ekatodades==4:
                 latinikos=latinikos +"CD"
        else:
                 latinikos=latinikos +"D"+(ekatodades-5)*"C"
                
                
if dekades>0:
        
        if dekades <4:
                latinikos=latinikos + dekades*"X"
        elif dekades==9:
                 latinikos=latinikos +"XC"
        elif dekades==5:
                 latinikos=latinikos +"L"
        elif dekades==4:
                 latinikos=latinikos +"XL"
        else:
                 latinikos=latinikos +"L"+(dekades-5)*"X"

if monades>0:
        
        if monades <4:
                latinikos=latinikos + monades*"I"
        elif monades==4:
                 latinikos=latinikos +"IV"
        elif monades==5:
                 latinikos=latinikos +"V"
        elif monades==9:
                 latinikos=latinikos +"IX"
        else:
                 latinikos=latinikos +"V"+(monades-5)*""


                
print {latinikos}

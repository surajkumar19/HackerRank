def capitalize(string):
    string=string.capitalize()
    s=""
    i=0
    #print(len(string))
    while i<len(string):
        if ord(string[i])==32:
            s=s+" "
            i+=1
            if i==len(string):
                break

        if ord(string[i])==46:
            s=s+"."
            s=s+" "
            i+=1
            if i==len(string):
                break
        if (ord(string[i])<123)and (ord(string[i])>96)and (ord(string[i])!=32)and ord(string[i-1])==32:
            z=ord(string[i])-32
            s=s+chr(z)
            i=i+1
            if i==len(string):
                break
        if ord(string[i])!=32:
            s=s+string[i]
            i=i+1
            if i==len(string):
                break

            
    return s
s='3902'
def hasSameDigits(s):
        
        if len(s)==1:
            return False
        
        if len(s)==2:
            return s[0]==s[1] 
        a=0
        r=''
        while a<len(s)-1:
            r+=str((int(s[a])+int(s[a+1]))%10)
            a=a+1
        else:
           return hasSameDigits(r)
        

print(hasSameDigits(s))
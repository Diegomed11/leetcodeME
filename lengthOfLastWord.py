s = "luffy is still joyboy"

def lengthOfLastWord(s):
        a=0
        s=s.strip()
        z=reversed(s)
        
        for i in z:
            if i == ' ':
                break
            else:
                a+=1
                continue
        return a

print(lengthOfLastWord(s))
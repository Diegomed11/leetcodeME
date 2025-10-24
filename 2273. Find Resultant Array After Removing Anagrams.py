words=['abba','baba','bbaa','cd','cd']

def removeAnagrams(words):

    result = [words[0]]
    
    
    for i in range(1,len(words)):
        
        if sorted(words[i]) != sorted(words[i-1]):
            result.append(words[i])
    
    return result
nums=[1,2,3,4,5,6,7,8,9,10]
value=6
def findSmallestInteger(nums,value):
    
    counts = [0] * value
    for num in nums:
        counts[num % value] += 1
    print(counts)
    mex=0
    while True:

        r=mex%value
        if counts[r]>0:
            counts[r]-=1
            mex+=1
        else:
            break
    return mex

print(findSmallestInteger(nums,value)) 

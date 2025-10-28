
nums=[1,0,2,0,3]

def countValidSelections(nums):
    n = len(nums)
    a=0
    s=sum(nums)
    left,right=0,s
    for i in range(n):
        if nums[i]==0:
            if 0<=left-right<=1:
                a+=1
            if 0<=right-left<=1:
                a+=1
        else:
            left+=nums[i]
            right-=nums[i]
    return a
print(countValidSelections(nums))
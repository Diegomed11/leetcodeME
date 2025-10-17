
nums=[-1,0,1,2,-1,-4]

def threeSum(nums):
    aux=[]
    z=0
    n=len(nums)
    nums.sort()
    
       
    for i in range(n-2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
             
             z=nums[i]+nums[j]+nums[k]
             if z == 0:
                aux.append((nums[i], nums[j], nums[k]))
             z=0


    return aux

print(threeSum(nums))
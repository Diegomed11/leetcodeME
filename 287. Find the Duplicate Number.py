nums = [4,3,1,4,2]

def findDuplicate(nums):
    nums.sort()  
    l = 0
    r = len(nums)-1
    
    while l <= r:
        med = (l + r) // 2
        
        if med > 0 and nums[med] == nums[med-1]:
            return nums[med]
        if med < len(nums)-1 and nums[med] == nums[med+1]:
            return nums[med]
            

        if nums[med] > med:
            l = med + 1
        else:
            r = med - 1
            
    return nums[l]

print(findDuplicate(nums))
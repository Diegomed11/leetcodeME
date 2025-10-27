
def searchInsert(nums, target):
    x=0
    y=len(nums)-1
    while x <= y:
        mid=(x+y)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            x=mid+1
        else:
            y=mid-1
    return x

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
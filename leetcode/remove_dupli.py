def removeDuplicates(nums):
    left=0
    for right in range(1,len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left]=nums[right]
    return nums
    


list=[1,2,3,3,4]

print(removeDuplicates(list))            

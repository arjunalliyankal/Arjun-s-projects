nums1 = [1,2,3,0,0,0,0,0]
nums2= [2,5,6]
m=3
n=3
  

    
for j in nums1:
    print(j)
    if j <= 0:
        nums1.remove(j)
print(nums1)             
        
for i in nums2:
    nums1.append(i)        
nums1.sort()
        

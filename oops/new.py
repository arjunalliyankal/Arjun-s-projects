def sum(a,target):

    count1=0
    count2=0
    for i in a:
        count1 += 1
        for j in a:
         
            if i+j==target:
                 count2 += 1
                 return count2,count1

a=[1,2,3,5,6,7,8,9,3]
target=7
print(sum(a,target))
print("hello")

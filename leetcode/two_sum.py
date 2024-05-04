
def twosum(nums,target):
    i=0
    j=1
    while i<len(nums):
        while j+i<len(nums):
            i=i+1
            if nums[i]+nums[j]==target:
                 return j


nums=[2,7,11,15]
target=9
print(twosum(nums,target))


// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int arr[5]={1,2,3,45,6};
    
    int target=46;
    for(int i=0;i<4;i++){
        for(int j=i+1;j<4;j++){
            if(arr[i]+arr[j]==target){
                return i,j
            }
        }
    }
    
    return 0;
}
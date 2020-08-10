'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
'''
nums = list(map(int,input().split()))
count = 0
i = 0
for k in range(len(nums)):
    for j in range(k,len(nums),1):
        if(nums[i] == nums[j] and i!=j):
            count += 1
    i += 1
print(count)
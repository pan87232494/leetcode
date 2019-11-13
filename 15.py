"""15. 3Sum
Medium

Favorite

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """



        nums.sort()
        result=[]
    
        for start in range(0, len(nums)-2):
            if start>=1 and nums[start]==nums[start-1]:
                continue
            mid = start + 1
            end = len(nums) - 1
            
     
            while mid < end:
                s=nums[mid] + nums[end] + nums[start] 
                if s > 0:
                    end=end-1
                if s< 0 :
                    mid=mid+1
                if s == 0:
                    
                    result.append([nums[start], nums[mid], nums[end]])
                    while  mid<end and nums[mid]==nums[mid+1]:
                        mid=mid+1
                    while  mid<end and nums[end]==nums[end-1] :
                        end=end-1
                    mid = mid + 1
                    end = end - 1


  
        return result
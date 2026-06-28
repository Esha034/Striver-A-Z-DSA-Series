# Approach 
1. Assume the first element is the largest.
2. Traverse the array from the second element.
3. If the current element is greater than the largest,
    Update the largest.
4. After the loop, return the largest.

#solution

class Solution:
    def largestElement(self, nums):
        largest = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]

        return largest

#Complexity
Time: O(n) (visit each element once)
Space: O(1)

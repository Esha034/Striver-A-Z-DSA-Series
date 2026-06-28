#Approach 
1.Initialize count = 0.
2.Traverse the array.
3.Compare each element with the next element using modulo.
4.If the current element is greater than the next, increase count.
5.If count > 1, return False otherwise return True.

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1

#Complexity
Time: O(n) (one traversal)
Space: O(1)

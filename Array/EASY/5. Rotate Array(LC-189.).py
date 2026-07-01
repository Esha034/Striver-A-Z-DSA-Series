#bruteforce code

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        for i in range(k):
            t=nums[-1]
            for j in range(n-1,-1,-1):
                nums[j]=nums[j-1]
            nums[0]=t

#better

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        ans=[0]*n
        for i in range(n):
           ans[(i+k)%n]=nums[i]

        nums[:]=ans

#Approach 3 (Optimal)
At every step, we maintain the invariant:
1.largest: stores the largest value seen so far.
2.second: stores the second distinct largest value seen so far.
3.Whenever a new maximum is found, the old maximum becomes the
second largest and new maximum becomes the largest.

def secondLargest(nums):
    largest = float('-inf')
    second = float('-inf')

    for num in nums:

        if num > largest:
            second = largest
            largest = num

        elif largest > num > second:
            second = num

    if second == float('-inf'):
        return -1

    return second

#Complexity
Time:O(n)-Only one traversal.
Space:O(1)





#Approach 2 (Better)
1.Find the largest in one pass.
2.Then again traverse the array
3.find the largest element smaller than the maximum.

def secondLargest(nums):
    largest = max(nums)

    second = -1

    for num in nums:
        if num != largest:
            second = max(second, num)

    return second
#Complexity
Time:O(n) + O(n)= O(2n)≈ O(n)
Space: O(1)





# Approach 1 (Brute Force)
1.Sort the array.
2.Largest = last element
3. Now move left from end until you find a different value.

def secondLargest(nums):
    nums.sort()

    largest = nums[-1]

    for i in range(len(nums)-2, -1, -1):
        if nums[i] != largest:
            return nums[i]

    return -1

#Complexity:
Time:Sorting = O(n log n)
Space:O(1) (if sorting in-place)


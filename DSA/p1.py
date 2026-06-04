class Solution:
    def largeNum(self, nums, n):
        max = nums[0]
        for i in range(1, n):
            if nums[i] > max:
                max = nums[i]
        return max

nums = [3, 5, 2, 6, 7]
n = len(nums)

solution = Solution()
large_num = solution.largeNum(nums, n)
print(large_num)
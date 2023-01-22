class Solution(object):

    def two_sum(nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    t = 9
    print(Solution().twoSum(nums, t))

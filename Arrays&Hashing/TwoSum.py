class Solution(object):

    def twoSum(self, nums, target):

        # Create an empty dictionary
        num_dict = {}
        # Iterate through the list of integers
        for i, num in enumerate(nums):
            # Check if the target minus the current integer is in the dictionary
            if target - num in num_dict:
                # If it is, return the indices of the two integers
                return [num_dict[target - num], i]
            # If not, add the current integer and its index to the dictionary
            num_dict[num] = i
            # If no solution is found, return None
        return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    t = 9
    print(Solution().twoSum(nums, t))

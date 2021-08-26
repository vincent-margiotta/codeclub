from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is valid because:
        # 1. There is exactly one solution and
        # 2. You cannot use the same element twice
        # Therefore, the first two elements must be the solution
        if len(nums) == 2:
            return 0, 1

        for element in nums:
            difference = target - element

            if difference in nums:
                if element == difference:
                    if nums.count(difference) > 1:
                        first = nums.index(element)
                        return first, nums.index(difference, first+1)
                    else:
                        continue
                return nums.index(element), nums.index(difference)

if __name__ == '__main__':
    test = Solution()
    result = test.twoSum([-1,-2,-3,-4,-5], -8)
    print(result)
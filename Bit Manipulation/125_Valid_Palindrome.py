from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


    # Test cases for the singleNumber function
    def test_singleNumber(self):
        assert self.singleNumber([2, 2, 1]) == 1
        assert self.singleNumber([4, 1, 2, 1, 2]) == 4
        assert self.singleNumber([1]) == 1
        assert self.singleNumber([0, 1, 0, 1, 99]) == 99
        assert self.singleNumber([-1, -1, -2]) == -2
        print("All test cases passed!")


if __name__ == "__main__":
    nums = [2,2,1]
    answer = 1
    actual_answer = Solution().singleNumber(nums)
    print(actual_answer)
    print(actual_answer == answer)


    print("Next example")
    nums = [4,1,2,1,2]
    answer = 4
    actual_answer = Solution().singleNumber(nums)
    print(actual_answer)
    print(actual_answer == answer)

    print("Next example")
    nums = [1]
    answer = 1
    actual_answer = Solution().singleNumber(nums)
    print(actual_answer)
    print(actual_answer == answer)

import heapq
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    uniq_nums = set(nums)
    max_length = 0

    for num in uniq_nums:
        if num - 1 not in uniq_nums:
            cur_number = num
            cur_length = 1

            while cur_number + cur_length in uniq_nums:
                cur_length += 1

            max_length = max(max_length, cur_length)
    return max_length








if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))

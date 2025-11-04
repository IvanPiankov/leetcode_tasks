import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_numbers = {}
    for i in nums:
        freq_numbers[i] = freq_numbers.get(i, 0) + 1
    return heapq.nlargest(k, freq_numbers.keys(), key=freq_numbers.get)



if __name__ == "__main__":
    # s = "anagram"
    # t = "nagaram"
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))

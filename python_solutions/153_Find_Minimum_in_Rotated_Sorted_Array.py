from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid_idx = left + ((right - left) // 2)
        mid_elem = nums[mid_idx]
        right_elem = nums[right]

        if mid_elem > right_elem:
            left = mid_idx + 1
        elif mid_elem < right_elem:
            right = mid_idx
        else:
            left = mid_idx

    return nums[left]



if __name__ == "__main__":
    nums = [3,4,5,1,2]
    answer = 1
    actual_answer = findMin(nums)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [4,5,6,7,0,1,2]
    answer = 0
    actual_answer = findMin(nums)
    print(actual_answer)
    print(actual_answer == answer)
    nums = [11,13,15,17]
    answer = 11
    actual_answer = findMin(nums)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")

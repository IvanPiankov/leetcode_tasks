from typing import List


def search(nums: List[int], target: int) -> int:
    target_index = -1
    left_idx, right_idx = 0, len(nums) - 1

    while left_idx <= right_idx:
        mid_idx = left_idx + ((right_idx - left_idx) // 2)
        mid_elem = nums[mid_idx]
        left_elem = nums[left_idx]
        right_elem = nums[right_idx]

        if mid_elem == target:
            target_index = mid_idx
            break

        if left_elem <= mid_elem:
            if left_elem <= target <= mid_elem:
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1
        else:
            if mid_elem <= target <= right_elem:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1

    return target_index



if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    answer = 4
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [4,5,6,7,0,1,2]
    target = 3
    answer = -1
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)
    nums = [1]
    target = 0
    answer = -1
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [1]
    target = 1
    answer = 0
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [1,3]
    target = 3
    answer = 1
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [3,1]
    target = 1
    answer = 1
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")


from typing import List


def search(nums: List[int], target: int) -> int:
    target_index = -1
    l, r = 0, len(nums) - 1

    while l <= r:
        middle_index = l + ((r - l) // 2)

        if nums[middle_index] > target:
            r = middle_index - 1
        elif nums[middle_index] < target:
            l = middle_index + 1
        else:
            target_index = middle_index
            break

    return target_index


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    answer = 4
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [-1,0,3,5,9,12]
    target = 2
    answer = -1
    actual_answer = search(nums, target)
    print(actual_answer)
    print(actual_answer == answer)

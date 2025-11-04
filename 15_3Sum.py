from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        k = len(nums) - 1
        j = i + 1

        while j < k:
            three_sum = nums[i] + nums[j] + nums[k]

            if three_sum < 0:
                j += 1
            elif three_sum > 0:
                k -= 1
            else:
                results.append([nums[i], nums[j], nums[k]])
                j += 1

    return results


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    answer = [[-1,-1,2],[-1,0,1]]
    actual_answer = threeSum(nums)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [0,1,1]
    answer = []
    actual_answer = threeSum(nums)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [0,0,0]
    answer = [[0,0,0]]
    actual_answer = threeSum(nums)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [0,0,0,0]
    answer = [[0,0,0]]
    actual_answer = threeSum(nums)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [-2,0,1,1,2]
    answer = [[-2,0,2],[-2,1,1]]
    actual_answer = threeSum(nums)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    nums = [-2,0,0,2,2]
    answer = [[-2,0,2]]
    actual_answer = threeSum(nums)
    print(actual_answer)
    print(actual_answer == answer)

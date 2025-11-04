from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    start_idx, end_idx = 0, len(numbers) - 1

    while start_idx < end_idx:
        left_num = numbers[start_idx]
        right_num = numbers[end_idx]

        two_sum = left_num + right_num

        if two_sum == target:
            break
        elif two_sum > target:
            end_idx -= 1
        else:
            start_idx += 1

    return [start_idx+1, end_idx+1]


if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    answer = [1,2]
    actual_answer = twoSum(numbers, target)
    print(actual_answer)
    print(actual_answer == answer)

    print("Next example")
    numbers = [2, 3, 4]
    target = 6
    answer = [1,3]
    actual_answer = twoSum(numbers, target)
    print(actual_answer)
    print(actual_answer == answer)

    print("Next example")
    numbers = [-1,0]
    target = -1
    answer = [1,2]
    actual_answer = twoSum(numbers, target)
    print(actual_answer)
    print(actual_answer == answer)

    print("Next example")
    numbers = [5,25,75]
    target = 100
    answer = [2,3]
    actual_answer = twoSum(numbers, target)
    print(actual_answer)
    print(actual_answer == answer)

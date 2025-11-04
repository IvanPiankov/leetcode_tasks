from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    # Индекс последнего элемента
    left, right = 0, (rows * cols) - 1

    while left <= right:
        middle_index = left + ((right - left) // 2)
        row = middle_index // cols
        col = middle_index % cols

        check_value = matrix[row][col]

        if check_value > target:
            right = middle_index - 1
        elif check_value < target:
            left = middle_index + 1
        else:
            return True

    return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    answer = True
    actual_answer = searchMatrix(matrix, target)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    answer = False
    actual_answer = searchMatrix(matrix, target)
    print(actual_answer)
    print(actual_answer == answer)

from ftplib import all_errors
from typing import List



def maxArea(height: List[int]) -> int:
    max_area = 0

    left_point = 0
    right_point = len(height) - 1


    while left_point < right_point:
        width_points = right_point - left_point
        height_points = min(height[left_point], height[right_point])
        area = width_points * height_points

        if max_area < area:
            max_area = area

        if height[left_point] < height[right_point]:
            left_point += 1
        else:
            right_point -= 1


    return max_area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    answer = 49
    actual_answer = maxArea(height)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    height = [1,1]
    answer = 1
    actual_answer = maxArea(height)
    print(actual_answer)
    print(actual_answer == answer)
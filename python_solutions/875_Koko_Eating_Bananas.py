import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    def is_eat_all_piles(piles: List[int], h: int, k: int) -> bool:
        spending_time = 0
        for pile in piles:
            spending_time += math.ceil(pile / k)
        return spending_time <= h

    left, right = 1, max(piles)
    res = 0

    while left < right:
        mid_speed = left + ((right - left) // 2)
        if is_eat_all_piles(piles, h, mid_speed):
            res = mid_speed
            right = mid_speed - 1
        else:
            left = mid_speed + 1

    return res



if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    answer = 4
    actual_answer = minEatingSpeed(piles, h)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    piles = [30,11,23,4,20]
    h = 6
    answer = 23
    actual_answer = minEatingSpeed(piles, h)
    print(actual_answer)
    print(actual_answer == answer)

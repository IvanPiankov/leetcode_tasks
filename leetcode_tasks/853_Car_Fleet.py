from typing import List


# def carFleet(target: int, position: List[int], speed: List[int]) -> int:
#     cars = list(zip(position, speed))
#     cars.sort(reverse=True)
#
#     fleet = 0
#     slowest_time_to_destination = 0
#     for start, speed in cars:
#         current_time_start_to_dest = (target - start) / speed
#         print(current_time_start_to_dest)
#         if slowest_time_to_destination < current_time_start_to_dest:
#             fleet += 1
#             slowest_time_to_destination = current_time_start_to_dest
#     return fleet

# Stack solution
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = list(zip(position, speed))
    cars.sort(reverse=True)

    stack = []

    for start, speed in cars:
        current_time_start_to_dest = (target - start) / speed
        if not stack or stack[-1] < current_time_start_to_dest:
            stack.append(current_time_start_to_dest)

    return len(stack)


if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    actual_answer = carFleet(target, position, speed)
    print(actual_answer)
    print("Next example")
    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    actual_answer = carFleet(target, position, speed)
    print(actual_answer)
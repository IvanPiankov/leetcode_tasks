from typing import List

# TODO: WRONG ANSWER
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    temp_list = []
    update = temperatures[:]
    for i, t in enumerate(temperatures):
        if update:
            update.pop(0)
        max_value = next((idx + 1 for idx, v in enumerate(update) if v > t), 0)
        temp_list.append(max_value)

    return temp_list


if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    answer = [1,1,4,2,1,1,0,0]
    actual_answer = dailyTemperatures(temperatures)
    print(actual_answer)
    print(actual_answer == answer)

    temperatures = [30,40,50,60]
    answer = [1,1,1,0]
    actual_answer = dailyTemperatures(temperatures)
    print(actual_answer)
    print(actual_answer == answer)

    temperatures = [30,60,90]
    answer = [1,1,0]
    actual_answer = dailyTemperatures(temperatures)
    print(actual_answer)
    print(actual_answer == answer)
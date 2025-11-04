import heapq
from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack_numbers = []

    for elem in tokens:
        if elem.isdigit() or elem.lstrip('-').isdigit():
            stack_numbers.append(int(elem))
            continue
        match elem:
            case "+":
                stack_numbers[-2] += stack_numbers[-1]
            case "-":
                stack_numbers[-2] -= stack_numbers[-1]
            case "*":
                stack_numbers[-2] *= stack_numbers[-1]
            case _:
                stack_numbers[-2] = int(stack_numbers[-2] / stack_numbers[-1])
        stack_numbers.pop()

    return stack_numbers[0]


if __name__ == "__main__":
    tokens1 = ["2","1","+","3","*"]
    print(evalRPN(tokens1))
    tokens2 = ["4","13","5","/","+"]
    print(evalRPN(tokens2))
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens3))

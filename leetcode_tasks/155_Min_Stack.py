import heapq
from typing import List


class MinStack:

    def __init__(self):
        self.elements = []
        self.min_elements = []

    def push(self, val: int) -> None:
        self.elements.append(val)

        if not self.min_elements:
            self.min_elements.append(val)
            return

        if val < self.min_elements[-1]:
            self.min_elements.append(val)
        else:
            self.min_elements.append(self.min_elements[-1])

    def pop(self) -> None:
        self.elements.pop()
        self.min_elements.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.min_elements[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # return -3
    minStack.pop()
    print(minStack.top())  # return 0
    print(minStack.getMin())   # return -2


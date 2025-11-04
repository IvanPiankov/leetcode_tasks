from typing import List


def generateParenthesis(n: int) -> List[str]:
    combinations = []
    generate_seq(combinations, "", 0, 0, n)
    return combinations


def generate_seq(combinations, current, left, right, n):
    if len(current) == n*2:
        combinations.append(current)
    else:
        if left < n:
            generate_seq(combinations, current + "(", left + 1, right, n)

        if right < left:
            generate_seq(combinations, current + ")", left, right + 1, n)


if __name__ == "__main__":
    n = 3
    answer = ["((()))","(()())","(())()","()(())","()()()"]
    actual_answer = generateParenthesis(n)
    print(actual_answer)
    print(actual_answer == answer)
    n = 1
    answer = ["()"]
    actual_answer = generateParenthesis(n)
    print(actual_answer)
    print(actual_answer == answer)

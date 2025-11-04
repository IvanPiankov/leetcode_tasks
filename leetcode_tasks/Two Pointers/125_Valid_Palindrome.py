from typing import List


def isPalindrome(s: str) -> bool:
    s = s.lower()
    l, r = 0, len(s) - 1
    is_palindrome = True

    while l < r:
        left_value = s[l]
        right_value = s[r]

        if not left_value.isalnum():
            l += 1
            continue

        if not right_value.isalnum():
            r -= 1
            continue

        if left_value != right_value:
            is_palindrome = False
            break
        else:
            l += 1
            r -= 1

    return is_palindrome


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    answer = True
    actual_answer = isPalindrome(s)
    print(actual_answer)
    print(actual_answer == answer)

    print("Next example")
    s = "race a car"
    answer = True
    actual_answer = isPalindrome(s)
    print(actual_answer)
    print(actual_answer == answer)

    print("Next example")
    s = " "
    answer = True
    actual_answer = isPalindrome(s)
    print(actual_answer)
    print(actual_answer == answer)


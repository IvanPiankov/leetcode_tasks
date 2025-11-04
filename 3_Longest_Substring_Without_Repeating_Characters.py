from ftplib import all_errors
from typing import List



def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    slow = fast = 0
    max_long_sub_string = 1
    sub_string_char = set()
    string_len = len(s) - 1

    while slow != string_len:
        fast_elem = s[fast]

        if fast_elem in sub_string_char or fast == string_len:
            sub_string_char.add(fast_elem)
            max_long_sub_string = max(max_long_sub_string, len(sub_string_char))
            slow += 1
            fast = slow
            sub_string_char = set()
        else:
            sub_string_char.add(fast_elem)
            fast += 1

        set().remove()
    return max_long_sub_string


if __name__ == "__main__":
    s = "abcabcbb"
    answer = 3
    actual_answer = lengthOfLongestSubstring(s)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    s = "bbbbb"
    answer = 1
    actual_answer = lengthOfLongestSubstring(s)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    s = "pwwkew"
    answer = 3
    actual_answer = lengthOfLongestSubstring(s)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    s = "au"
    answer = 2
    actual_answer = lengthOfLongestSubstring(s)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
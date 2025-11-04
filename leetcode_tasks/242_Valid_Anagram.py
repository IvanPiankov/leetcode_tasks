
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_counter: dict[str, int] = {}
    t_counter: dict[str, int] = {}
    for val in s:
        s_counter[val] = s_counter.get(val, 0) + 1
    for val in t:
        t_counter[val] = t_counter.get(val, 0) + 1
    return s_counter == t_counter


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

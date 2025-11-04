from typing import List, Dict


def containsDuplicate(nums: List[int]) -> bool:
    set_of_numbers = set()
    for num in nums:
        if num not in set_of_numbers:
            set_of_numbers.add(num)
        else:
            return True
    return False

if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    

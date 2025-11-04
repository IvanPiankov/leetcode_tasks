from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""

        searching_list = self.storage[key]
        target_value = ""
        left, right = 0, len(searching_list) - 1
        while left <= right:
            mid_idx = left + ((right - left) // 2)
            elem = searching_list[mid_idx]
            elem_timestamp = elem[1]

            if elem_timestamp > timestamp:
                right = mid_idx - 1
            elif elem_timestamp < timestamp:
                left = mid_idx + 1
                target_value = elem[0]
            else:
                target_value = elem[0]
                break

        return target_value

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == "__main__":
    timeMap = TimeMap()
    print(timeMap.set("foo", "bar", 1))
    print(timeMap.get("foo", 1))
    print(timeMap.get("foo", 3))
    print(timeMap.set("foo", "bar2", 4))
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))

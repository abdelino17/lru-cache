from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def put(self, key: str, value: str) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

    def get(self, key: str) -> int | str:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def show_entries(self) -> None:
        print(self)

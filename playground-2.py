class Node:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)


class Skiplist:

    def __init__(self, max_level, partition):
        self.max_level = max_level
        self.partition = partition
        self.level = 0
        self.header = Node(-1, max_level)

    def search(self, target: int) -> bool:
        pass

    def add(self, num: int) -> None:
        update = [None] * (self.max_level + 1)
        current = self.header

    def erase(self, num: int) -> bool:
        pass

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
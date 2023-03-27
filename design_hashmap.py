class MyHashMap:

    def __init__(self):
        self._size = 1000000+1
        self.hash_map = [-1 for i in range(self._size)]
        

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        return self.hash_map[key] if key < self._size else -1
        

    def remove(self, key: int) -> None:
        self.hash_map[key] = -1 if key < self._size else None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
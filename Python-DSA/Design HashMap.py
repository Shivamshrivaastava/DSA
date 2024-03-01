# Design a HashMap without using any built-in hash table libraries.

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        hash_key = self._hash(key)
        found = False
        for i, pair in enumerate(self.map[hash_key]):
            if pair[0] == key:
                self.map[hash_key][i] = (key, value)
                found = True
                break
        if not found:
            self.map[hash_key].append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        for k, v in self.map[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        hash_key = self._hash(key)
        for i, pair in enumerate(self.map[hash_key]):
            if pair[0] == key:
                del self.map[hash_key][i]
                break


# Example usage:
hash_map = MyHashMap()
hash_map.put(1, 'Hello')
hash_map.put(2, 'World')
print(hash_map.get(1))  # Output: 'Hello'
print(hash_map.get(3))  # Output: -1
hash_map.put(2, 'Python')
print(hash_map.get(2))  # Output: 'Python'
hash_map.remove(2)
print(hash_map.get(2))  # Output: -1


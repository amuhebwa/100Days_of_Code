class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        hashmap_s, hashmap_t = {}, {}
        for char_s, char_t in zip(s, t):
            if (char_s in hashmap_s and hashmap_s[char_s] != char_t) or (char_t in hashmap_t and hashmap_t[char_t] != char_s):
                return False
            hashmap_s[char_s] = char_t
            hashmap_t[char_t] = char_s
        
        print(hashmap_s)
        print('-'*20)
        print(hashmap_t)
        return True
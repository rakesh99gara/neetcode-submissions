class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1

        for c in t:
            if (s_dict.get(c)):
                s_dict[c] = s_dict.get(c) - 1
            else:
                return False
        return (not any(x > 0 for x in s_dict.values()))


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        b = {}
        w = set()

        if len(pattern) != len(s):
            return False

        for i,ch in enumerate(pattern):
            if ch in b:
                if b[ch] != s[i]:
                    return False
            else:
                if s[i] in w:
                    return False
                else:
                    b[ch] = s[i]
            w.add(s[i])

        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        schar = {}
        tchar = {}
        for c in s:
            if c not in schar.keys():
                schar.update({c:1})
            else:
                schar[c] += 1

        for c in t:
            if c not in tchar.keys():
                tchar.update({c:1})
            else:
                tchar[c] += 1

        return schar == tchar
        
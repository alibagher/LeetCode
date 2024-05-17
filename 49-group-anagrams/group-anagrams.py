class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        m = dict()

        for word in strs:
            ordered = ''.join(sorted(word))
            if ordered in m:
                m[ordered].append(word)
            else:
                m[ordered] = [word]
        
        return list(m.values())
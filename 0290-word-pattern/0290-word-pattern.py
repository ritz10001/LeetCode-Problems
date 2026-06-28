class Solution(object):
    def wordPattern(self, pattern, s):
        mapper = {}
        seen = set()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if char in mapper:
                if mapper[char] != word:
                    return False
            else:
                if word in seen:
                    return False
                mapper[char] = word
                seen.add(word)
        return True
        
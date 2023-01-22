from collections import Counter


class Solution(object):

    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    print(Solution().isAnagram(s, t))

from collections import Counter # <-- Import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        odd_found = False

        for c in counts.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                odd_found = True

        if odd_found:
            length += 1

        return length # <-- Correctly indented to be inside the function
class Solution:
    def firstOccurence(self, s, p):

        for i in range(len(s)):

            j = 0

            while j < len(p):

                if i + j >= len(s):
                    break

                if s[i + j] != p[j]:
                    break

                j += 1

            if j == len(p):
                return i

        return -1
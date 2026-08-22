class Solution:
    def isSubset(self, a, b):
        count = {}

        for x in a:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        for x in b:
            if x not in count or count[x] == 0:
                return False

            count[x] -= 1

        return True
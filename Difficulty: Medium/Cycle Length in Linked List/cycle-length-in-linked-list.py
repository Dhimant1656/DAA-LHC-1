''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):

            visited = set()
            current = head
            count = 0

            while current is not None:

                if current in visited:
                    startOfLoop = current

                    while True:
                        count += 1
                        current = current.next

                        if current == startOfLoop:
                            break

                    return count

                visited.add(current)
                current = current.next

            return 0


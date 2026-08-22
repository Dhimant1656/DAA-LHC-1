class Solution:
    def reverseList(self, head):

        previous = None
        current = head

        while current is not None:

            nextNode = current.next
            current.next = previous

            previous = current
            current = nextNode

        return previous
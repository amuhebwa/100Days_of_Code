class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def addNode(self, item):
        if self.head is None:
            self.head = Node(item)
        elif self.head.next is None:
            self.head.next = Node(item)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(item)

    def print(self):
        if self.head is None:
            print('List is empty')
            return
        current = self.head
        while current != None:
            print('->>>', current.value)
            current = current.next

    def findMiddle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle is ", slow.value)

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next # variable to hold current.next
            current.next = prev # current.next points to back
            prev = current # update prev
            current = next # update current
        self.head = prev


if __name__=="__main__":
    linked = LinkedList()
    linked.addNode('Monday')
    linked.addNode('Tuesday')
    linked.addNode('Wednesday')
    linked.addNode('Thursday')
    #linked.addNode('Friday')
    # linked.print()
    linked.findMiddle()
    #linked.reverse()
    #linked.print()

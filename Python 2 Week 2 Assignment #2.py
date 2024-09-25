class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove(self, data):
        if not self.head:
            return

        # Check if the head node contains the data
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()
    llist.remove(2)
    print()
    llist.printList()
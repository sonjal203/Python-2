class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, item):
        """Append item to the end of the list."""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def insert_at_beginning(self, item):
        """Insert an item at the beginning of the list."""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        """Print all items in the list."""
        current = self.head
        while current:
            print(current.item, end=" ")
            current = current.next
        print()  # For new line at the end of the print.
if __name__ == '__main__':
    linked_list = LinkedList()
    # Append items
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    # Insert at the beginning
    linked_list.insert_at_beginning(0)
    # Print the linked list item
    linked_list.print_list()  # Output should be: 0 1 2 3
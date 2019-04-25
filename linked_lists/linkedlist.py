class LinkedList:
    def __init__(self, head_node):
        self.headNode = head_node

    def append(self, node):
        if node.next is not None:
            return
        current_node = self.headNode
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    # Print the linked list
    def listprint(self):
        node = self.headNode
        while node is not None:
            print(node.val)
            node = node.next

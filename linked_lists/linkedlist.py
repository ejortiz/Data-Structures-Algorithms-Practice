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

    def prepend(self, node):
        temp_node = self.headNode
        self.headNode = node
        node.next = temp_node

    def insert(self, node, existing_node):
        right_node = existing_node.next
        existing_node.next = node
        node.next = right_node

    def remove(self, node_to_remove):
        current_node = self.headNode
        while current_node.next is not node_to_remove:
            current_node = current_node.next
        right_node = node_to_remove.next
        current_node.next = right_node
        del node_to_remove

    def reverse(self):
        prev = None
        curr = self.headNode
        nex = curr.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            if nex:
                nex = nex.next

        self.headNode = prev



    # Print the linked list
    def listprint(self):
        node = self.headNode
        while node is not None:
            print(node.val)
            node = node.next

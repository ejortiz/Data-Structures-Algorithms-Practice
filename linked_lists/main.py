from linkedlist import LinkedList
from node import Node

node_0 = Node(0)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(-1)
node_4 = Node(1.5)
linked_list = LinkedList(node_0)
linked_list.append(node_1)
linked_list.append(node_2)

linked_list.prepend(node_3)
linked_list.insert(node_4, node_1)
linked_list.remove(node_0)
linked_list.listprint()

# Reverse a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Reverse
head = reverse_linked_list(head)

# Print linked list
current = head

while current:
    print(current.data, end=" → ")
    current = current.next

print("None")
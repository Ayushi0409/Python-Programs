class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Create linked list: 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node(4))))

print("Original list:")
print_list(head)

# Reverse the linked list
head_reverse = reverse(head)

print("Reversed list:")
print_list(head_reverse)

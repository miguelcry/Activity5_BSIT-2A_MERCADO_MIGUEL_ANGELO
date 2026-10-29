class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError(
                "Stack underflow: stack is empty."
            )

        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError(
                "Stack underflow: stack is empty."
            )
        return self.head.data

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def __str__(self):
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        return "Top -> " + " -> ".join(values) + " -> None"

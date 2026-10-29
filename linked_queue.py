class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError(
                "Queue underflow: queue is empty."
            )

        item = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError(
                "Queue underflow: queue is empty."
            )
        return self.head.data

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # No fixed capacity.
        return False

    def __str__(self):
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        return "Front -> " + " -> ".join(values) + " -> Rear"
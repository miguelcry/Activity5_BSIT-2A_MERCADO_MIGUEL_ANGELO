class ArrayStack:
    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.items = []

    def push(self, item):
        if self.is_full():
            raise OverflowError(
                "Stack overflow: stack is full."
            )
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError(
                "Stack underflow: stack is empty."
            )
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError(
                "Stack underflow: stack is empty."
            )
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def __str__(self):
        return f"Bottom -> {self.items} <- Top"
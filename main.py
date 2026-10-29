def show_state(structure):
    print("Current state:", structure)
    print("Empty:", structure.is_empty())
    print("Full:", structure.is_full())


def run_stack(stack):
    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Back")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                item = input("Enter item: ")
                stack.push(item)
                print("Item pushed.")

            elif choice == "2":
                print("Popped item:", stack.pop())

            elif choice == "3":
                print("Top item:", stack.peek())

            elif choice == "4":
                break

            else:
                print("Invalid choice.")
                continue

            show_state(stack)

        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_state(stack)


def run_queue(queue):
    while True:
        print("\n--- QUEUE MENU ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek Front")
        print("4. Back")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                item = input("Enter item: ")
                queue.enqueue(item)
                print("Item added.")

            elif choice == "2":
                print("Removed item:", queue.dequeue())

            elif choice == "3":
                print("Front item:", queue.peek_front())

            elif choice == "4":
                break

            else:
                print("Invalid choice.")
                continue

            show_state(queue)

        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_state(queue)


def balanced_parentheses(expression):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.append(character)

        elif character in ")]}":
            if not stack or stack.pop() != pairs[character]:
                return False

    return len(stack) == 0


def print_queue_demo():
    jobs = []

    try:
        count = int(input("Number of print jobs: "))
        if count < 0:
            print("Number of jobs cannot be negative.")
            return
    except ValueError:
        print("Please enter a whole number.")
        return

    for i in range(count):
        print(f"\nJob {i + 1}")
        job_id = input("Job ID: ")

        try:
            pages = int(input("Number of pages: "))
            if pages < 0:
                print("Page count cannot be negative.")
                continue
        except ValueError:
            print("Invalid page count. Job skipped.")
            continue

        jobs.append((job_id, pages))

    print("\nPrint waiting order (FIFO):")

    for position, (job_id, pages) in enumerate(jobs, start=1):
        print(
            f"{position}. Job ID: {job_id}, "
            f"Pages: {pages}"
        )

    while jobs:
        job_id, pages = jobs.pop(0)
        print(f"Printing job {job_id} ({pages} pages)")


def ask_capacity():
    try:
        capacity = int(input("Enter capacity: "))
        if capacity <= 0:
            print("Capacity must be greater than zero.")
            return None
        return capacity
    except ValueError:
        print("Please enter a whole number.")
        return None


def main():
    while True:
        print("\n=== STACKS AND QUEUES ===")
        print("1. ArrayStack")
        print("2. LinkedStack")
        print("3. Circular ArrayQueue")
        print("4. LinkedQueue")
        print("5. Check Balanced Parentheses")
        print("6. Simulate Print Queue")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            capacity = ask_capacity()
            if capacity is not None:
                run_stack(ArrayStack(capacity))

        elif choice == "2":
            run_stack(LinkedStack())

        elif choice == "3":
            capacity = ask_capacity()
            if capacity is not None:
                run_queue(ArrayQueue(capacity))

        elif choice == "4":
            run_queue(LinkedQueue())

        elif choice == "5":
            expression = input("Enter an expression: ")

            if balanced_parentheses(expression):
                print("The parentheses are balanced.")
            else:
                print("The parentheses are not balanced.")

        elif choice == "6":
            print_queue_demo()

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

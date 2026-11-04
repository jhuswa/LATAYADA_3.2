# Assessment 3.2 - Stack Implementation (LIFO)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def main():
    stack = Stack()

    print("--- Pushing Elements onto Stack ---")
    elements = ['L', 'A', 'T', 'A', 'Y', 'A', 'D', 'A']
    for item in elements:
        stack.push(item)
        print(f"Pushed '{item}' into Stack | Top of Stack: '{stack.peek()}' | Stack: {stack.items}")

    print("\n--- Popping Elements from Stack ---")
    while not stack.is_empty():
        popped = stack.pop()
        top_str = f"'{stack.peek()}'" if not stack.is_empty() else "None"
        print(f"Popped '{popped}' from Stack | Top of Stack: {top_str} | Stack: {stack.items}")

    print("\nStack is now Empty. End.")

if __name__ == "__main__":
    main()
# Assessment 3.2 - Queue Implementation (FIFO)
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

def main():
    queue = Queue()

    print("--- Enqueueing Elements into Queue ---")
    elements = ['L', 'A', 'T', 'A', 'Y', 'A', 'D', 'A']
    for item in elements:
        queue.enqueue(item)
        print(f"Enqueued '{item}' into Queue | Front of Queue: '{queue.front()}' | Queue: {list(queue.items)}")

    print("\n--- Dequeueing Elements from Queue ---")
    while not queue.is_empty():
        dequeued = queue.dequeue()
        front_str = f"'{queue.front()}'" if not queue.is_empty() else "None"
        print(f"Dequeued '{dequeued}' from Queue | Front of Queue: {front_str} | Queue: {list(queue.items)}")

    print("\nQueue is now Empty. End.")

if __name__ == "__main__":
    main()
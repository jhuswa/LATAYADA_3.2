# Assessment 3.2 - Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_head(self):
        if not self.head:
            return None
        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(elements) + " -> NULL" if elements else "NULL"

def main():
    ll = LinkedList()

    print("--- Inserting Nodes into Linked List ---")
    elements = ['L', 'A', 'T', 'A', 'Y', 'A', 'D', 'A']
    for item in elements:
        ll.insert_end(item)
        print(f"Inserted Node '{item}': Head -> {ll.display()}")

    print("\n--- Deleting Head Nodes from Linked List ---")
    while ll.head is not None:
        deleted = ll.delete_head()
        print(f"Deleted head Node '{deleted}': Head -> {ll.display()}")

    print("\nLinked List is now Empty (Head = NULL). End.")

if __name__ == "__main__":
    main()
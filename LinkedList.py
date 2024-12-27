class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Class to represent the linked list."""
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
           self.head=new_node
           return
        current=self.head
        while current.next:
            current=current.next
        
        current.next=new_node


   

    def display(self):
        """Display the contents of the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    # linked_list.insert_at_beginning(5)

    print("Linked List:")
    linked_list.display()

    # print("\nDeleting a node with data 20:")
    # linked_list.delete_node(20)
    # linked_list.display()
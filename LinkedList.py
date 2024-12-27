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

    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
            
        
        new_node.next=self.head
        self.head=new_node

   
    def insert_at_position(self,data,idx):
        new_node=Node(data)
        current=self.head
        
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        count=0
        
        # Traverse the list to find the node at the given position
        while current and count <idx-1:
            current=current.next
            count+=1
       
 
        if not current:
            print("Position out of range.")
            return

       #link the node from the list
        new_node.next=current.next
        current.next=new_node

    def delete_at_position(self, idx):
       
        # If the list is empty
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        
        # If the position to delete is 0 (i.e., the head node)
        if idx == 0:
            self.head = current.next
            current = None
            return
        
        count = 0
        prev = None

        # Traverse the list to find the node at the given position
        while current and count < idx:
            prev = current
            current = current.next
            count += 1
        
        # Unlink the node from the list
        prev.next = current.next
        current = None
        
    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
            
        return False
            

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
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(100)

    # linked_list.insert_at_position(16,4)
    # linked_list.delete_at_position(2)


    

    print("Linked List:")
    linked_list.display()

    # if linked_list.search(20):
    #     print("Element Founded")
    # else:
    #     print("Not Founded")

    # print("\nDeleting a node with data 20:")
    # linked_list.delete_node(20)
    # linked_list.display()
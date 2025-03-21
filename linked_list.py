class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertatbeginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next 


    def insert_at_index():
        pass      
             

if __name__ == "__main__":

    lst = LinkedList()

    lst.insertatbeginning(1)
    lst.insertatbeginning(5)
    lst.print()



# Hi, here's your problem today. This problem was recently asked by Google:

# Given a singly-linked list, reverse the list.
# This can be done iteratively or recursively. Can you get both solutions?

# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlinkedlist(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def reverseList(self):
        temp = self.head
        self.head = None
        while (temp):
            reversed_list = Node(temp.data)
            reversed_list.next = self.head
            self.head = reversed_list
            temp = temp.next

        self.printlinkedlist()


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert("1")
    new_list.insert("2")
    new_list.insert("3")
    new_list.insert("4")

    print("The original list is")
    new_list.printlinkedlist()

    print("\nThe reversed list is")
    new_list.reverseList()

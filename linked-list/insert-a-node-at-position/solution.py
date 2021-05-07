class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, val):
        new_node = SinglyLinkedListNode(val)

        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node            

def print_singly_linked_list(head):
    if head == None:
        print("empty list")
    else:
        current_node = head
        print(head.data, end='')
        while current_node.next != None:
            current_node = current_node.next
            print(' -> ', current_node.data, end='')
        print()

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if head == None:
        return new_node
    elif position == 0:
        new_node.next = head
        return new_node
    else:
        current_node = head
        count = 0
        while current_node != None and count < position - 1:
            current_node = current_node.next
            count += 1
        new_node.next = current_node.next
        current_node.next = new_node
        return head
    
if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)
    
    print_singly_linked_list(llist.head)




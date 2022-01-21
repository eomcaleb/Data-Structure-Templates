# Linked List
# ------------
# Linear collection of data that consists of linked nodes that represent the data itself
# and a reference to the next node.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def count(self):
        if self.head is None:
            return 0

        count = 1
        curr = self.head
        while curr.next is not None:
            count = count + 1
            curr = curr.next
        return count

    def pop(self):
        if self.head is None:
            raise IndexError
        else:
            self.head = self.head.next

    def search(self, data):
        lst = self.head
        position = 1
        while lst.data != data and lst.next is not None:
            position += 1
            lst = lst.next

        if lst.data == data:
            return position
        return -1

    # delete
    # insert inbetween
    # insert before
    # insert a pos
    # sort
    # merge
    # delete at the end
    # trim - empty nodes

    def print(self):
        print("-------------")
        print("Singly Linked List: Contents")
        lst = self.head
        while lst is not None:
            print(lst.data)
            lst = lst.next
        print ("------------")

    def delete(self, data):
        # Approach: Loop through the LL first and STOP when it reaches either end or match
        lst = self.head
        previous = None
        while lst.data != data and lst.next:
            previous = lst
            lst = lst.next
        if lst.data == data:
            if previous:
                # This is if deletion happens after 1st item
                # previous item's next points straight to current next item
                previous.next = lst.next
            else:
                # This is if deletion happens on first item
                self.head = lst.next

    def insertposition(self, data, pos):
        counter = 1
        lst = self.head
        while lst.next:
            if counter == pos:
                node = Node(data)
                node.next = lst.next
                lst.next = node
                break
            counter += 1
            lst = lst.next

    def insertback(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            lst = self.head
            while lst.next:
                lst.head = lst.next
            lst.next = node

    def clear(self):
        while self.head:
            hold = self.head
            self.head = self.head.next
            hold = None

    def deleteoccurance(self, data):
        lst = self.head
        previous = None

        # Catch beginning occurance(s)
        while lst and lst.data == data:
            self.head = lst.next
            lst = self.head

        # Catch rest
        while lst:
            while lst and lst.data is not data:
                previous = lst
                lst = lst.next

            if lst is None:
                break

            previous.next = lst.next
            lst = previous.next

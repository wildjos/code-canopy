import unittest
import io
from contextlib import redirect_stdout


class Node:
    
    def __init__(self, id: int):

        self.id = id
        self.next = None

    def __repr__(self):
        return(f"id: {self.id}, next: {self.next}")
    

class LinkedList:

    def __init__(self):
        self.head = None

    
    def append(self, node: Node):


        # if the list is empty, then set the head and return
        if self.head == None:
            self.head = node
            return

        # else traverse the list until get to the end (.next is None)
        # and add the new node at the end!
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node


    def print_list(self):
        """Print all nodes in the linked list."""
        current = self.head
        while current:
            print(f"{current.id} -> ", end="")
            current = current.next
        print("None")  # End of list marker


    # T: O(N)
    # S: O(1)
    def reverse_list(self):

        current = self.head
        prev = None

        while current:

            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev



    # S: O(1)
    # T: O(N)
    def reverse_between(self, m, n):

        if not self.head:
            return 
        
        current = self.head
        position = current.id
        start = current

        while position < m:
            start = current
            current = current.next
            position += 1
            
        end = current
        prev = None

        while position >= m and position <= n: 

            next = current.next
            current.next = prev
            prev = current
            current = next
            position += 1

        start.next = prev
        end.next = current 

        if m <= 1:
            self.head = prev




class TestLinkedList(unittest.TestCase):

    def test_Node(self):
        id = 1
        n = Node(id)
        self.assertIsNone(n.next)
        self.assertEqual(n.id, id)

    def test_Empty_LinkedList(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        

    def test_Create_10(self):

        ll = LinkedList()
        for id in range(10):
            ll.append(Node(id))
        
        self.assertIsNotNone(ll.head)

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            ll.print_list()
        output = captured_output.getvalue().strip()
        expected_output = "0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None"
        self.assertEqual(output, expected_output)

        # print(output)


    def test_Reverse_5(self):
        
        ll = LinkedList()
        for id in range(5):
            ll.append(Node(id))

        ll.reverse_list()

        captured_io = io.StringIO()
        with redirect_stdout(captured_io):
            ll.print_list()

        output = captured_io.getvalue().strip()
        expected_output = "4 -> 3 -> 2 -> 1 -> 0 -> None"

        # print(output)
        self.assertEqual(output, expected_output)

    def test_Reverse_m_n(self):

        ll = LinkedList()
        for id in range(1,6):
            ll.append(Node(id))

        ll.reverse_between(2, 4)

        captured_io = io.StringIO()
        with redirect_stdout(captured_io):
            ll.print_list()

        output = captured_io.getvalue().strip()
        expected_output = "1 -> 4 -> 3 -> 2 -> 5 -> None"

        print(output)
        self.assertEqual(output, expected_output)


    def test_Reverse_all(self):

        ll = LinkedList()
        for id in range(1,6):
            ll.append(Node(id))

        ll.reverse_between(1, 5)

        captured_io = io.StringIO()
        with redirect_stdout(captured_io):
            ll.print_list()

        output = captured_io.getvalue().strip()
        expected_output = "5 -> 4 -> 3 -> 2 -> 1 -> None"

        print(output)
        self.assertEqual(output, expected_output)

    def test_Reverse_1(self):

        ll = LinkedList()
        for id in range(1, 2):
            ll.append(Node(id))
        ll.print_list()

        ll.reverse_between(1, 1)

        captured_io = io.StringIO()
        with redirect_stdout(captured_io):
            ll.print_list()

        output = captured_io.getvalue().strip()
        expected_output = "1 -> None"

        print(output)
        self.assertEqual(output, expected_output)

    def test_Reverse_none(self):

        ll = LinkedList()

        ll.reverse_between(0, 0)

        captured_io = io.StringIO()
        with redirect_stdout(captured_io):
            ll.print_list()

        output = captured_io.getvalue().strip()
        expected_output = "None"

        print(output)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":

    unittest.main()

    # id = 1
    # n = Node(id)

    # print(n)

    # my_ll = LinkedList() 
    # print(my_ll)
    # my_ll.append(n)
    # my_ll.print_list()

    # n = Node(2)
    # my_ll.append(n)
    # my_ll.print_list()



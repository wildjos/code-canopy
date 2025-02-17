import unittest
import io
from contextlib import redirect_stdout

class Node:
    def __init__(self, id: int):
        self.id = id
        self.next = None

    def __repr__(self):
        return(f"id: {self.id}, next: {self.next}")
    

class TestLinkedList(unittest.TestCase):

    def test_Node(self):
        id = 1
        n = Node(id)
        self.assertIsNone(n.next)
        self.assertEqual(n.id, id)

        captured_io = io.StringIO()
        with redirect_stdout(captured_io):
           print(n)
        output = captured_io.getvalue().strip()

        self.assertEqual("id: 1, next: None", output )
        


if __name__ == "__main__":
    unittest.main()  

# Constraints are well explained: 
# Given a string, determine if it is a pallindrome
#  consider only alphanumeric characters, 
#  ignore case sensitivity


import unittest
import re
import math

# 2 pointers, one each end
def is_it_palindrome( s: str) -> bool:

    s = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()

    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

# reverse string and compare
def is_it_palindrome_2( s: str ) -> bool:

    s1 = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    s2 = s1[::-1]

    return s1 == s2



#  2 pointers, start in middle
def is_it_palindrome_3(s: str) -> bool:
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()

    length = len(s)
    p2 = math.floor(length/2)
    p1 = p2

    # if even
    if length % 2 == 0:
        p1 = p2 - 1

    while p1 >= 0:
        if s[p1] != s[p2]:
            return False
        p1 -= 1
        p2 += 1

    return True
    
     

class TestIsAPalindrome(unittest.TestCase):

    def run_test_palindromes(self, func):
        self.assertTrue(func("aabaa"))
        self.assertTrue(func("aabbaa"))
        self.assertTrue(func("a"))
        self.assertTrue(func("noon"))

    def run_test_non_palindromes(self, func):
        self.assertFalse(func("abc"))

    def run_test_edge_cases(self, func):
        self.assertTrue(func(""))
        self.assertTrue(func(" "))
        self.assertTrue(func("A man, a plan, a canal: Panama"))

    def test_solution_1(self):
        self.run_test_palindromes(is_it_palindrome)
        self.run_test_non_palindromes(is_it_palindrome)
        self.run_test_edge_cases(is_it_palindrome)

    def test_solution_2(self):
        self.run_test_palindromes(is_it_palindrome_2)
        self.run_test_non_palindromes(is_it_palindrome_2)
        self.run_test_edge_cases(is_it_palindrome_2)

    def test_solution_3(self):
        self.run_test_palindromes(is_it_palindrome_3)
        self.run_test_non_palindromes(is_it_palindrome_3)
        self.run_test_edge_cases(is_it_palindrome_3)

if __name__ == "__main__":
    unittest.main()
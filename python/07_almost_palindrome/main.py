

import unittest
from typing import Tuple


def compare( left: int, right: int, s: str ) -> Tuple[bool, int, int] :

    while left <= right:
        if s[left] != s[right]:
            return False, left, right
        left += 1
        right -= 1
    return True, left, right

# NB: no string processing as assume it is an alphanumeric string
def almost_a_palindrome(s: str) -> bool:

    length = len(s)
    if length <= 2:
        return True

    left = 0
    right = len(s) - 1

    res = compare(left, right, s)

    if res[0] == True:
        return True
    
    # create s1 and s2 by slicing
    s1 = s[:res[1]] + s[res[1] + 1:]
    s2 = s[:res[2]] + s[res[2] + 1:]

    left = 0
    right = len(s1) - 1
    res = compare(left, right, s1)
    if res[0] == True:
        return True

    res = compare(left, right, s2)
    if res[0] == True:
        return True

    return False

# -------------------------------------------------------------------------

# Sub-palindrome checker function
def sub_palindrome( s: str, left: int, right: int ) -> False :

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Again, assume the string has been pre-processed 
#  - this time, don't repeat the work of comparing the whole string. 
#    we want to carry on checking the string from the left|right pointers
def almost_a_p_efficient( s: str ) -> bool:

    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] != s[right] :
            
            # by skipping a character we achieve the same as slicing the string!
            # return the OR of the two sub-problems
            return sub_palindrome(s, left+1, right) or sub_palindrome(s, left, right-1)
        left += 1
        right -= 1

    return True




class TestAlmostPalindrome(unittest.TestCase):

    def run_is_almost(self, func):
        self.assertTrue(func("raceacar"))
        self.assertTrue(func("abccdba"))

    def run_is_not(self, func):
        self.assertFalse(func("abcdefdba"))

    def run_edge_cases(self, func):
        self.assertTrue(func(""))
        self.assertTrue(func("a"))
        self.assertTrue(func("ab"))

    def test_almost_a_palindrome(self):
        self.run_is_almost(almost_a_palindrome)
        self.run_edge_cases(almost_a_palindrome)
        self.run_is_not(almost_a_palindrome)

    def test_almost_a_p_efficient(self):
        self.run_is_almost(almost_a_p_efficient)
        self.run_edge_cases(almost_a_p_efficient)
        self.run_is_not(almost_a_p_efficient)


if (__name__) == "__main__" :
    unittest.main()


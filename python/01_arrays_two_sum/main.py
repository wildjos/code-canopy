import unittest

# Solution 1: Brute Force Approach
# This approach uses a nested loop to check all pairs of numbers 
# to find the two that add up to the target.
def two_sum(test_array, target):

    len_test_array = len(test_array) 

    for p1 in range(len_test_array):
        p2 = p1 + 1
        
        diff = target - test_array[p1]
        while p2 < len_test_array:        
            if test_array[p2] == diff:
                return [p1, p2]
            
            p2 += 1
    
    return None



# Solution 2: Optimized Approach 1
# This approach calculates the complement and
# stroes in the hashmap
def two_sum_optimised(test_array, target):

    len_test_array = len(test_array) 

    hashmap = {}
    for p1 in range(len_test_array):
        hashmap[target - test_array[p1]] = p1

    for p2 in range(len_test_array):
        value = test_array[p2]
        if value in hashmap:
            if hashmap[value] != p2:
                return [p2, hashmap[value]]

    return None


# Best solution, T: O(N) and S: 0(N)
# This approach combines the hashmap creation 
# and checking into a single loop
def two_sum_optimised_final(test_array, target):

    hashmap = {}
    len_test_array = len(test_array)

    for p1 in range(len_test_array):
        currentVal = test_array[p1]

        if currentVal in hashmap:
            return [hashmap[currentVal], p1]
        
        else: 
            ntf = target - currentVal 
            hashmap[ntf] = p1
        
    return None


class TestTwoSum(unittest.TestCase):

    def run_tests(self, func):
        self.assertEqual(func([1, 3, 7, 9, 2], 11), [3, 4])
        self.assertIsNone(func([], 3))
        self.assertIsNone(func([1], 3))
        self.assertIsNone(func([2, 4, 5, 6], 3))
        self.assertEqual(func([1, 5, 8, 2, 3], 5), [3, 4])

    def test_two_sum(self):
        self.run_tests(two_sum)

    def test_two_sum_optimised(self):
        self.run_tests(two_sum_optimised)

    def test_two_sum_optimised_final(self):
        self.run_tests(two_sum_optimised_final)

if __name__ == "__main__":
    unittest.main()


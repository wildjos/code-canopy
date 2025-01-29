from typing import List
import unittest

# Brute Force Approach
# Analysis: T: O(N^2)  S: O(1)
def calc_area_by_brute_force( test_array: List[int] ) -> int: 

    # p1 and p2 are indexes into the array
    # test_array[p] will be value(i.e, y-axis of area)
    
    largest_area = 0
    # coords = () 

    for p1 in range(0, len(test_array)):
        for p2 in range(p1+1, len(test_array)):
            x1 = test_array[p1]
            x2 = test_array[p2]

            x = p2 - p1
            y = min(x1, x2)
            area = x * y
            if area > largest_area:
                largest_area = area
                coords = (x1, x2)

    # print(f"The largest area is {largest_area}")
    # if largest_area > 0:
    #     print(f"\twhere x1 = {coords[0]} and x2 = {coords[1]}")
    return largest_area


# Efficient approach: start with pointer at each end, 
# always move the shorter of the two pointers inwards
#  - because moving the taller of the two pointer has no effect on the area
# efficiency: S: O(1)  T: O(N)
def calc_area_efficient( test_array: List[int] ) -> int:
 
    largest_area = 0

    if len(test_array) < 2:
        return 0

    p1 = 0
    p2 = len(test_array) -1
    while p1 < p2:
        
        # calculate the area
        x = p2 - p1
        y = min(test_array[p1], test_array[p2]) 
        area = x * y
        largest_area = max(area, largest_area)

        if test_array[p1] < test_array[p2]:
            p1 += 1
        else:
            p2 -= 1
        
    return largest_area



class TestWaterArea(unittest.TestCase) : 

    def run_area(self, func):
        self.assertEqual(func( [3, 5, 2, 8, 3] ), 12)
        self.assertEqual(func( [7, 1, 2, 3, 9] ), 28)
        self.assertEqual(func( [4, 8, 1, 2, 3, 9] ), 32)

    def run_edge_cases(self, func):
        self.assertEqual(func( [] ), 0)
        self.assertEqual(func( [1] ), 0)

    def test_brute_force(self):
        self.run_area(calc_area_by_brute_force)
        self.run_edge_cases(calc_area_by_brute_force)

    def test_efficient_way(self):
        self.run_area(calc_area_efficient)
        self.run_edge_cases(calc_area_efficient)

        

if __name__ == "__main__" :
    unittest.main()

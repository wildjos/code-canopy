
from typing import List
import unittest

# Helper function
def max_elevation_to_left( emap: List[int], p) -> int:
    max = 0
    for i in range(0, p):
        if emap[i] > max:
            max = emap[i]

    return max

# Helper function
def max_elevation_to_right( emap: List[int], p) -> int:
    max = 0
    for i in range(p, len(emap)):
        if emap[i] > max:
            max = emap[i]

    return max


# Solution 1:  This is my brute-force solution. 
# Iterate over each position and finding the minimum of the maximum elevations to the left and right, 
# subtracting the current elevation to determine the trapped water. 
# T: O(N^2)
# S: O(1)
def elevation_map_v1( emap: List[int] ) -> int:

    # return 0 in case of less than 3 values
    if len(emap) < 3:
        return 0

    total = 0

    # for each elevation, lets find
    for p in range(0, len(emap)):
        # the greatest elevation to the left, and 
        # the greatest elevation to the right
        # then take the min of pl and pr
        pl = max_elevation_to_left( emap, p )
        pr = max_elevation_to_right( emap, p )

        # print(f"where p = {p}, pl = {pl}, pr = {pr}")

        height_of_water = min(pl, pr)
        # now take away any elevation on this space
        height_of_water = max(0, (height_of_water - emap[p]))


        # print(f"height_of_water = {height_of_water}")
        total += height_of_water
    
    # print(f"total water = {total}")
    return total

 
# Conceptually the same as the previous solution: 
# - Find the min of max left and max right elevations
# - Subtract current position's elevation
# Avoids function call overhead, but less modular.
# No change in time or space complexity.
# T: O(N^2), S: O(1) 
def elevation_map_v2( emap: List[int] ) -> int:

    total = 0

    for p in range(0, len(emap)):

        maxL = 0
        maxR = 0
        
        # Find max left elevation
        pL = p
        while pL >= 0:
            maxL = max(emap[pL], maxL)
            pL -= 1

        # Find max right elevation
        pR = p
        while pR < len(emap):
            maxR = max(emap[pR], maxR)
            pR += 1

       # Calculate water height at current position
        ch = max(0, min(maxL, maxR) - emap[p])

        total += ch

    return total


# This is the optimal solution, using two pointers.
# smaller of 2 pointers is the one that moves in, AND
# smaller of the 2 pointers is the one we take as current height
# S: O(1)   
# T: O(N)
def elevation_map( emap: List[int]) -> int:

    if len(emap) < 3:
        return 0

    total = 0

    pL = 0
    pR = len(emap)-1

    maxL = 0
    maxR = 0 

    # Use two pointers to scan from both ends
    while pL < pR:
        
        # The left side is the working side
        if emap[pL] <= emap[pR]:

            # Do we calculate water or move the pointer?
            currentHeight = emap[pL]
            if currentHeight < maxL:
                currentWater = max(0, maxL - currentHeight)
                total += currentWater
            else:
                maxL = max(maxL, currentHeight)
            pL += 1
            
        # The right side is the working side
        else:
            currentHeight = emap[pR]
            if currentHeight < maxR:
                currentWater = max(0, maxR - currentHeight)
                total += currentWater
            else:
                maxR = max(maxR, currentHeight)
            pR -= 1

    return total



# -------------------------------------------------------------------
# Testing:
#
class Test_Rainwater(unittest.TestCase) :

    def run_happy_path(self, func):
        try:
            rainwater = func( [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2] )
            self.assertEqual(rainwater, 8)
        except AssertionError:
            print(f"Test failed in run_happy_path for {func.__name__}")
            raise

    def run_empty(self, func):
        try:
            rainwater = func( [] )
            self.assertEqual( rainwater, 0 )
        except AssertionError:
            print(f"Test failed in run_empty for {func.__name__}")
            raise
        
    def run_one(self, func):
        try: 
            rainwater = func( [1] )
            self.assertEqual( rainwater, 0 )
        except AssertionError:
            print(f"Test failed in run_one for {func.__name__}")
            raise


    def run_mountain(self, func):
        try: 
            rainwater = func( [3, 4, 3] )
            self.assertEqual( rainwater, 0 )
        except AssertionError:
            print(f"Test failed in run_mountain for {func.__name__}")
            raise
    
    def run_two(self, func):
        try:
            rainwater = func( [2, 0, 2] )
            self.assertEqual( rainwater, 2 )
        except AssertionError: 
            print(f"Test failed in run_two for {func.__name__}")
            raise


    # test brute-force solution
    def test_solution_1(self):
        try: 
            self.run_happy_path(elevation_map_v1)
            self.run_empty(elevation_map_v1)
            self.run_mountain(elevation_map_v1)
            self.run_two(elevation_map_v1)
        except Exception as e:
            print(f"Error occurred during tests: {str(e)}")
            raise

    def test_solution_2(self):
        try: 
            self.run_happy_path(elevation_map_v2)
            self.run_empty(elevation_map_v2)
            self.run_mountain(elevation_map_v2)
            self.run_two(elevation_map_v2)
        except Exception as e:
            print(f"Error occurred during tests: {str(e)}")
            raise


    #  test optimal solution
    def test_elevation_map(self):
        try: 
            self.run_happy_path(elevation_map)
            self.run_empty(elevation_map)
            self.run_mountain(elevation_map)
            self.run_two(elevation_map)
        except Exception as e:
            print(f"Error occurred during tests: {str(e)}")
            raise


# -------------------------------------------------------------------
# Entry point
if __name__ == "__main__":

    unittest.main()

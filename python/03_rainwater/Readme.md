# Trapping Rainwater

[https://leetcode.com/problems/trapping-rain-water/description/](https://leetcode.com/problems/trapping-rain-water/description/)

You are given an integer array representing an elevation map.  The `width` of each bar is `1`. Return how much rainwater can be trapped. 

**Assumptions/Questions:**

1. Do the left and right sides of the graph count as walls?
   * No, the sides are not walls
   
2. Will there be negative integers?
  * No, assume the integers are positive


### Example 1:

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2:

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## To Test:

python3 -m unittest -v main.py
or
python3 main.py


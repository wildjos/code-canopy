# Container With Most Water

[https://leetcode.com/problems/container-with-most-water/description/](https://leetcode.com/problems/container-with-most-water/description/)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

### Notes:

This is a problem of finding an area bounded by vertical lines, and the x-axis.

The `y-axis` will be the `min(l1, l2)`
The `x-axis` will be `(x2 - x1)`

**Assumptions/Questions:**

1. Will the array be guaranteed to have 2 or more integers?
   
   1.a. If not, what should it return if empty or 1 integer in array?  (0)
2. What is the x-coordinate of each integer?
   
   2.a. I'm assuming it's the same as the array position (i.e. 0...len-1)
3. Do we need to keep the `x` and `y` axis of the solution? (to return, print out etc)
4. What if there are 2 equal solutions?  (I'm returning the first one)

### Example 1:

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### Example 2:

```
Input: height = [1,1]
Output: 1
```

## To Test:

python3 -m unittest -v main.py
or
python3 main.py


WaterTrapped Porblem Approach: 2 Pointer Approach
1. Declare l and r as 2 pointers, initializing l to  0 and r to the last index n-1
2. Declare leftMax and rightMax to track the "left max height" and "right max height" respectively and initialize it to 0
3. While l <= r , iterate the array
4. Now if leftMax > rightMax, 
5. Add the trappedWater which will be max(0, rightMax[i] - height[i])
6. Update the rightMax[i] = max(rightMax[i], height[i]), decrement r
7. Else(4) leftMax <= rightMax, 
8. Add the trappedWater which will be max(0, leftMax[i] - height[i])
9. Update the leftMax[i] = max(leftMax[i], height[i]), increment l
10. return back the trappedWater variable after iterating over the loop

![OUTPUT SCREENSHOT:](/problem_statement/waterTrapped.png)
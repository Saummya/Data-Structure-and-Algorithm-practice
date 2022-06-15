'''
Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, 
compute how much water can be trapped between the blocks during the rainy season. 
 

Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10
Explanation: 

Example 2:

Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above 
block of height 4 is 3 units and above 
block of height 0 is 7 units. So, the 
total unit of water trapped is 10 units.
Example 3:

Input:
N = 3
arr[] = {6,9,9}
Output:
0
Explanation:
No water will be trapped.

Your Task:
You don't need to read input or print anything. The task is to complete the function trappingWater() which takes arr[] and N as input parameters and returns the total amount of water that can be trapped.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
3 < N < 106
0 < Ai < 108'''


class Solution:
    def trappingWater(self, arr,n):
        #Code here
        # left[i] contains height of tallest bar to the
        # left of i'th bar including itself
        left = [0]*n
    
        # Right [i] contains height of tallest bar to
        # the right of ith bar including itself
        right = [0]*n
    
        # Initialize result
        water = 0
    
        # Fill left array
        left[0] = arr[0]
        for i in range( 1, n):
            left[i] = max(left[i-1], arr[i])
    
        # Fill right array
        right[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], arr[i]);
    
        # Calculate the accumulated water element by element
        # consider the amount of water on i'th bar, the
        # amount of water accumulated on this particular
        # bar will be equal to min(left[i], right[i]) - arr[i] .
        for i in range(0, n):
            water += min(left[i], right[i]) - arr[i]
    
        return water

  
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends

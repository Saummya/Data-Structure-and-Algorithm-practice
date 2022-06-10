'''
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)

Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes Arr[] and N as input parameters and returns the sum of subarray with maximum sum.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] ≤ 107
'''

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        curr_sum=0
        max_so_far=arr[0]
        
        st=0
        en=0
        poi=0
        
        for i in range(0,N):
            curr_sum+=arr[i]
            
            if max_so_far<curr_sum:
                max_so_far=curr_sum
                st=poi
                en=i
                
            if curr_sum<0:
                curr_sum=0
                poi=i+1
                
        s=0
        for i in range(st,en+1):
            s=s+arr[i]
            
        return s
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
